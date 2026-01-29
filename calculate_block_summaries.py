
# Complete block summaries and populate collection with resulting summary data
# Creates a JSON file to upload and replace BLOCK_SUMMARIES collection
##  output: block_summary_data.json
# Created 6/1/2023
# Scott K. Anderson

# Stats to collect

from pymongo.mongo_client import MongoClient
import certifi
import copy
import datetime
import time
import json
from mdbconn import connString

# modules for creating and uploading reports
import create_block_report_pdf
from create_block_report_pdf import PDF
from pdf_to_google import upload_file_to_drive, delete_file_from_drive

nl = "\n"
fmt_dt = "%Y-%m-%d"
max_timeout = 100000000

#####################################################################
## Connect to Mongo


client = MongoClient(
    connString(),
    connectTimeoutMS=max_timeout,
    socketTimeoutMS = max_timeout,
    serverSelectionTimeoutMS=max_timeout,
    tlsCAFile=certifi.where()
    )

## Get Block data
db = client.ebd_mgmt
ebd = db.ebd
blocks = db.blocks
dbs = db.db_status
err = db.ebd_upload_errlog

# PRODUCTION
bsum = db.BLOCK_SUMMARIES
# bsum = db.bs_test
# END PRODUCTION

## GET Current EBD update status
## DEPRECATED
# result = dbs.find_one({"_id": "summary"},{})
# db_stats = dict(result) # type: ignore

# current_ebd_ver = db_stats["NCBA_EBD_VER"] # type: ignore
# recent_ebd_dt = db_stats["MOST_RECENT_EBD_DATE"] # type: ignore
## END


# Function for recording errors on Atlas Cache
def ebdUpdateErrors( msg, err_data = {}):
    # log errors online
    errKey = datetime.datetime.strftime(
        datetime.datetime.now(),
        "%Y-%m-%d %H:%M:%S.%f".rstrip("0")
        )
    errOut = {
        "script" : "calculate_block_summaries.py",
        "errTime" : errKey
    }
    args = locals()
    del args["errOut"]
    for k,v in args.items():
        if v!={}: 
            errOut[k] = v

    err.insert_one(
        errOut
    )


# block completion criteria
minBlockBreedDiurnalHrs = 20
minBlockWinterDiurnalHrs = 5
minBlockBreedVisits = 3
minBlockWinterVisits = 2
minBlockBreedNocturnalVisits = 3
minBlockWinterNocturnalVisits = 1
minBlockWinterDetected = 55
minBlockBreedCoded = 55
minBlockBreedConfirmedPct = 0.25
maxBlockBreedPossiblePct = 0.25


def getJDay (d):
    dt = datetime.datetime.strptime(d, fmt_dt)
    dtt = dt.timetuple()
    return dtt.tm_yday

breeding_start = getJDay("2021-03-01")
breeding_end = getJDay("2021-08-31")
breeding_length = breeding_end - breeding_start
winter_start = getJDay("2021-11-01")
#note this is evaluated to be < winter end (i.e., not including the date)
winter_end = getJDay("2022-03-01")

winter1_end = getJDay("2021-12-31")
winter2_start = winter1_end + 1

## ORIGINAL - split breeding season into three equal parts
# breeding1_end = breeding_start + (breeding_length/3) # 04/25
# breeding2_start = breeding1_end + 1 # 4/26
# breeding2_end = breeding2_start + (breeding_length/3) # 06/21
# breeding3_start = breeding2_end + 1 

# CHANGED 12/17/24 matches field guide suggestion
breeding1_end = getJDay("2021-04-30") # 04/30
breeding2_start = breeding1_end + 1 # 5/1
breeding2_end = getJDay("2021-06-30") # 06/30
breeding3_start = breeding2_end + 1 # 07/01

today = datetime.date.today().strftime(fmt_dt)

breedCatRank = [
    "C0",
    "C1",
    "C2",
    "C3",
    "C4"
]

bcStatusLookup = {
    "C2": "Possible",
    "C3": "Probable",
    "C4": "Confirmed"
}

month_list = [
    "none",
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec"
]

def getBCRank(bc):
    if bc != "":
        return breedCatRank.index(bc)
    else:
        return 0

def getBCStatus(bcRank):

    if bcRank in bcStatusLookup.keys():
        return bcStatusLookup[bcRank]
    else:
        return "Detected"

def update_ac(blockId, bd):
    # update BLOCK_SUMMARIES collection
    # NOTE: this will overwrite ebird_web_data info.
    q = {
        "ID_NCBA_BLOCK" : blockId
    }
    p = {
        "$set" : bd
    }
    bsum.update_one(q, p)


def main(current_ebd_ver, recent_ebd_dt, start_block = ""):
    #####################################################################
    ## Get Block Completion Data, load into dict
    
    ## Retrieve priority block data
    query = {
        "PRIORITY": "1"
    }
    filter = {
        "ID_NCBA_BLOCK" : 1,
        "ID_BLOCK_CODE" : 1,
        "GAP_SPP" : 1,
        "COUNTY" : 1,
        "REGION" : 1
    }

    # block_data = blocks.find(query, filter).limit(100) # TESTING
    block_data = blocks.find(query, filter)
    
    print(nl + "block records retrieved...")

    #####################################################################
    ## Loop through block records, calculate fields
    blankSpp = {
        "COMMON_NAME" : "",
        "breedMaxCategory" : "",
        "breedStatus" : "",
        "breedDetected" : 0,
        # "winterStatus" : "",
        "winterDetected" : 0,
        "interimDetected" : 0,
        "breedingCodesTxt" : "",
        "breedingCodes": [],
        "s7EligibleChecklists" : []
    }

    blockcount = 0
    blockreviewcount = 0
    checkcount = 0
    block_summaries = []
    collect_block = False

    for b in block_data:
        blockreviewcount += 1
        group_checklists = set()

        block_id = b["ID_NCBA_BLOCK"]
        if (start_block == block_id or
            start_block == ""):
            collect_block = True

        # start block compilation after matching start_block
        if collect_block:
            # get ebd data for block
            # set up dicts for coallating data

            s7_list_temp = {}
            # holding space for s7 list
            # format
            # {COMMON_NAME : [{"SEI": SEI, "OBS_DATE": OBS_DATE, "LATITUDE":LATITUDE, "LONGITUDE": LONGITUDE}]}

            print (
                nl + 
                "=================================" + 
                nl + 
                "retrieving " + 
                block_id + 
                " data"
                )
            update_date = today

            query = {
                "ID_NCBA_BLOCK" : block_id,
                "PROJECT_CODE" : "EBIRD_ATL_NC" #get portal records only.
            }

            filter = {
                "PROJECT_CODE" : 1,
                "DURATION_MINUTES" : 1,
                "ALL_SPECIES_REPORTED" : 1,
                "EBD_NOCTURNAL" : 1,
                "PROTOCOL_TYPE" : 1,
                "OBSERVER_ID" : 1,
                "OBSERVATION_DATE" : 1,
                "NCBA_JULIAN_DAY" : 1,
                "PROTOCOL_CODE" : 1,
                "LATITUDE" : 1,
                "LONGITUDE" : 1,
                "YEAR" : 1,
                "GROUP_IDENTIFIER" : 1,
                "OBSERVATIONS.COMMON_NAME": 1,
                "OBSERVATIONS.BREEDING_CODE" : 1,
                "OBSERVATIONS.BREEDING_CATEGORY" : 1,
                "OBSERVATIONS.CATEGORY" : 1,
                "NCBA_HIDDEN" : 1
            }

            ebd_data = ebd.find(query, filter)    

            # summary stat variables - blank record
            bs = {
                "_id" : b["ID_NCBA_BLOCK"],
                "ID_NCBA_BLOCK" : b["ID_NCBA_BLOCK"],
                "ID_BLOCK_CODE" : b["ID_BLOCK_CODE"],
                "updateDate" : update_date,
                "county" : b["COUNTY"],
                "region" : b["REGION"],
                "breedCountConfirmed" : 0,
                "breedCountProbable" : 0,
                "breedCountPossible" : 0 ,
                "breedCountCoded" : 0 ,
                "breedCountDetected" : 0 ,
                # "breedCountTotal" : 0 ,
                "breedHrsDiurnal" : 0 ,
                "breedMinNocturnal" : 0 ,
                "breedMinDiurnal" : 0 ,
                "breedHrsNocturnal" : 0 ,
                "breedPctConfirmed" : 0 ,
                "breedPctProbable" : 0 ,
                "breedPctPossible" : 0 ,
                "breedCountDiurnalChecklists" : 0 ,
                "breed1CountDiurnalChecklists" : 0 ,
                "breed2CountDiurnalChecklists" : 0 ,
                "breed3CountDiurnalChecklists" : 0 ,
                "breedJunCountChecklists" : 0 ,
                "breedCountNocturnalChecklists" : 0 ,
                "breed1CountNocturnalChecklists" : 0 ,
                "breed2CountNocturnalChecklists" : 0 ,
                "breed3CountNocturnalChecklists" : 0 ,
                "bbcgCoded" : 0,
                "bbcgConfirmed" : 0,
                "bbcgPossible" : 0,
                "bbcgTotalEffortHrs" : 0,
                "bbcgDiurnalVisits" : 0,
                "bbcgNocturnalVisits" : 0,
                "winterCountDetected" : 0 ,
                "winterMinDiurnal" : 0 ,
                "winterMinNocturnal" : 0 ,
                "winterHrsDiurnal" : 0 ,
                "winterHrsNocturnal" : 0 ,
                "winterCountDiurnalChecklists" : 0 ,
                "winter1CountDiurnalChecklists" : 0 ,
                "winter2CountDiurnalChecklists" : 0 ,
                "winterJanCountChecklists" : 0 ,
                "winterDecCountChecklists" : 0 ,
                "winterCountNocturnalChecklists" : 0 ,
                "winter1CountNocturnalChecklists" : 0 ,
                "winter2CountNocturnalChecklists" : 0 ,
                "wbcgDetected" : 0,
                "wbcgTotalEffortHrs" : 0,
                "wbcgDiurnalVisits" : 0,
                "wbcgNocturnalVisits" : 0,
                "NCBA_STAFF_PRIORITY" : "", # HIGH FOR SURVEY YEARS
                "NCBA_EBD_VER" : current_ebd_ver,
                "MOST_RECENT_EBD_DATE" : recent_ebd_dt,
                "sppList" : [],
                "s7EligibleChecklists" : {}
            }
            
            blockSpp = [] # count list for block species
            tod = "Diurnal"

            # Loop through checklists and compile stats
            for e in ebd_data:
                
                ################################################################
                ## set category fields

                # check to see if this is a portal record
                if e["PROJECT_CODE"] == "EBIRD_ATL_NC":
                    bPortal = True
                else:
                    bPortal = False

                # do not count multiple group checklists
                count_checklist = True
                if e["GROUP_IDENTIFIER"] != "":
                    if e["GROUP_IDENTIFIER"] in group_checklists:
                        count_checklist = False
                    else:
                        group_checklists.add(e["GROUP_IDENTIFIER"])

                # what season is the checklist in?
                jday = e["NCBA_JULIAN_DAY"]
                season_part = ""
                month = int(e["OBSERVATION_DATE"][5:7])
                if (breeding_start <= jday < breeding_end):
                    season = "breed"
                    if (jday >= breeding3_start):
                        season_part = "breed3"
                    elif (jday >= breeding2_start):
                        season_part = "breed2"
                    else:
                        season_part = "breed1"

                elif (jday >= winter_start or jday < winter_end):
                    season = "winter"
                    if (jday < winter_end):
                        season_part = "winter2"
                    else:
                        season_part = "winter1"
                else:
                    season = "interim"

                if e["EBD_NOCTURNAL"] == "1":
                    tod = "Nocturnal"
                
                if (season != "interim"):
                    
                    # do not count incidental checklists in the checklist count
                    # also exclude multiple checklists in group
                    if count_checklist:
                        
                        # add minutes
                        if e["PROTOCOL_TYPE"] != "Incidental":
                            tField = season + "Min" + tod
                            bs[tField] = bs[tField] + e["DURATION_MINUTES"]
                            tField = "" 

                        # count checklists
                        tField = season + "Count" + tod + "Checklists"
                        bs[tField] = bs[tField] + 1
                        tField = ""

                        # count season part checklists
                        tField = season_part + "Count" + tod + "Checklists"
                        bs[tField] = bs[tField] + 1
                        tField = ""

                        if (month in [6, 12, 1]):
                            tField = (season + month_list[month] +
                                "CountChecklists")
                            bs[tField] = bs[tField] + 1
                            tField = ""
                    
                # compile spp-level stats
                for o in e["OBSERVATIONS"]:
                    if o["CATEGORY"] in ["species", "issf", "hybrid", "domestic"]:
                        cn = o["COMMON_NAME"]
                        # check if already in list
                        # keep track of gap spp data in temp blockSppTally dict
                        if bPortal:
                            if cn not in blockSpp:
                                bs["sppList"].append(copy.deepcopy(blankSpp))
                                blockSpp.append(cn)
                                bs["sppList"][blockSpp.index(cn)]["COMMON_NAME"] = cn

                            sppInd = blockSpp.index(cn)

                            # add to array of observations
                            currBCode = o["BREEDING_CODE"]
                            if currBCode: 
                                # breeding code is not ""
                                # if "S" add to upgrade eligible list
                                if (currBCode == "S" and
                                    e["PROTOCOL_CODE"] in [
                                        "P20", "P21", "P67", "P73", "P88",
                                        "P87", "P89", "P82"] and
                                    e["YEAR"] == 2025 and
                                    season == "breed" and 
                                    e["NCBA_HIDDEN"] == 0
                                    ):

                                    # new version
                                    # checks if spp in temp dict, then adds
                                    if o["COMMON_NAME"] not in s7_list_temp.keys():
                                        s7_list_temp[o["COMMON_NAME"]] = []
                                    
                                    s7_list_temp[o["COMMON_NAME"]].append(
                                        {
                                            "SEI" : e["_id"],
                                            "OBS_DATE" : e["OBSERVATION_DATE"],
                                            "LATITUDE" : e["LATITUDE"],
                                            "LONGITUDE" : e["LONGITUDE"],
                                            "BREEDING_CODE" : currBCode
                                        }
                                    )

                        # populate indicator if species detected in season
                        cnIndex = blockSpp.index(cn)
                        bs["sppList"][cnIndex][season + "Detected"] = 1

                        if (season == "breed" or
                            (o["BREEDING_CATEGORY"] not in ["C0", "C1", "C2"] and
                            season != "breed"
                            )
                            ):
                            currBc = o["BREEDING_CATEGORY"]
                            currBCRank = getBCRank(currBc)
                            prevBCRank = getBCRank(
                                bs["sppList"][cnIndex]["breedMaxCategory"]
                                )
                            if currBCRank >= prevBCRank:
                                bs["sppList"][cnIndex]["breedMaxCategory"] = currBc
                                bs["sppList"][cnIndex]["breedStatus"] = getBCStatus(currBc)
                    
                    cn = ""

                checkcount += 1
                season = ""
                tod = "Diurnal" #Diurnal or Nocturnal

            # summarize block stats
            ## repeat for breeding and non-breeding

            ##################################################################
            # BLOCK SUMMARY STATS
            # loop through bsSpp to compile stats

            # tally breeding status
            for i in bs["sppList"]:
                #tally breeding status
                if i["breedStatus"] != "":
                    bs["breedCount" + i["breedStatus"]] += 1

                # re-compile S7_list
                if (i["breedStatus"] == "Possible" and
                    i["COMMON_NAME"] in s7_list_temp.keys()
                    ):
                    # species is possible and in s7_list
                    # loop through checklists
                    for c in s7_list_temp[i["COMMON_NAME"]]:
                        if c["SEI"] not in bs["s7EligibleChecklists"]:
                            bs["s7EligibleChecklists"][c["SEI"]] = {
                                    "SEI" : c["SEI"],
                                    "OBS_DATE" : c["OBS_DATE"],
                                    "LATITUDE" : c["LATITUDE"],
                                    "LONGITUDE" : c["LONGITUDE"],
                                    "SPP_LIST" : []
                                }
                        
                        bs["s7EligibleChecklists"][c["SEI"]]["SPP_LIST"].append(
                            i["COMMON_NAME"]
                        )
                
                #tally detected
                bs["winterCountDetected"] += i["winterDetected"]

            #tally hours
            bs["breedHrsDiurnal"] = bs["breedMinDiurnal"]/60
            bs["breedHrsNocturnal"] = bs["breedMinNocturnal"]/60
            bs["winterHrsDiurnal"] = bs["winterMinDiurnal"]/60
            bs["winterHrsNocturnal"] = bs["winterMinNocturnal"]/60

            ##############################
            # block completion requirements

            ## BREEDING
            ## coded spp
            bs["breedCountCoded"] = (
                bs["breedCountConfirmed"] +
                bs["breedCountPossible"] +
                bs["breedCountProbable"]
            )

            if bs["breedCountCoded"] >= minBlockBreedCoded:
                bs["bbcgCoded"] = 1

            if bs["breedCountCoded"] != 0:
                ## probable    
                bs["breedPctProbable"] = (
                    bs["breedCountProbable"]/bs["breedCountCoded"]
                )
                ## confirmed    
                bs["breedPctConfirmed"] = (
                    bs["breedCountConfirmed"]/bs["breedCountCoded"]
                )

                if bs["breedPctConfirmed"] >= minBlockBreedConfirmedPct:
                    bs["bbcgConfirmed"] = 1

                ## Possible
                bs["breedPctPossible"] = (
                    bs["breedCountPossible"]/bs["breedCountCoded"]
                )
                if bs["breedPctPossible"] <= maxBlockBreedPossiblePct:
                    bs["bbcgPossible"] = 1
            else:
                bs["breedPctConfirmed"] = 0
                bs["breedPctPossible"] = 0
    


            ## Total Breeding Effort Hrs
            if bs["breedHrsDiurnal"] >= minBlockBreedDiurnalHrs:
                bs["bbcgTotalEffortHrs"] = 1

            ## total breeding visits
            if bs["breedCountDiurnalChecklists"] >= minBlockBreedVisits:
                bs["bbcgDiurnalVisits"] = 1

            ## total nocturnal visits
            if bs["breedCountNocturnalChecklists"] >= minBlockBreedNocturnalVisits:
                bs["bbcgNocturnalVisits"] = 1

            ## WINTERING
            ## total detected
            if bs["winterCountDetected"] >= minBlockWinterDetected:
                bs["wbcgDetected"] = 1

            ## total Diurnal Hours
            if bs["winterHrsDiurnal"] >= minBlockWinterDiurnalHrs:
                bs["wbcgTotalEffortHrs"] = 1

            ## total Diurnal Visits
            if bs["winterCountDiurnalChecklists"] >= minBlockWinterVisits:
                bs["wbcgDiurnalVisits"] = 1

            ## total Nocturnal Checklists
            if bs["winterCountNocturnalChecklists"] >= minBlockWinterNocturnalVisits:
                bs["wbcgNocturnalVisits"] = 1

            # get block status
            rec = bsum.find_one(
                {"ID_NCBA_BLOCK" : block_id},
                {"STATUS" : 1, "REPORT_URL": 1}
            )
            bs["STATUS"] = rec["STATUS"] # type: ignore
            
            # ##########################################################
            # ## Create PDF Block Report
            # # delete old report from google
            url = rec["REPORT_URL"] # type: ignore
            file_id = url.split("/")[-2]
            try:
                delete_file_from_drive(file_id)
            except:
                print("file could not be found for deletion")
            # create and upload new report to google
            pdf = PDF(bs)
            file_name = f'{bs["ID_NCBA_BLOCK"]}_Report.pdf'
            file_path = f'block_reports/{file_name}'
            pdf.output(file_path)

            file_url = upload_file_to_drive(file_path, file_name)
            bs["REPORT_URL"] = file_url
            # remove status so it doesn't get overwritten
            status = bs.pop("STATUS")

            ##########################################################
            ## Update the Atlas Cache
            #add to block summaries dict
            block_summaries.append(bs)

            # upload to MongoDB
            try:
                update_ac(
                    bs["ID_NCBA_BLOCK"],
                    bs
                )

                blockcount += 1 
                print (
                    nl + 
                    "Completed " + 
                    block_id + 
                    " data" + 
                    nl + 
                    str(blockcount) + 
                    " blocks completed" +  nl +
                    str(blockreviewcount) + " blocks reviewed" + nl +
                    "=================================" + 
                    nl
                    )
                # give the database time to catch up?
                time.sleep(15)

            except Exception as errmsg:
                print(
                    bs["ID_NCBA_BLOCK"],
                    "failed to update", nl,
                    repr(errmsg)
                )
                ebdUpdateErrors(
                    repr(errmsg),
                    bs
                )

if __name__=="__main__":
	main();
