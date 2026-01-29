# Used to chunk out ebd records in ordder to upload MongoDB
# Scott Anderson Mar 10, 2021
# NC Wildlife Resources Commission
# scott.anderson@ncwildlife.org
# python 3.8

#############################################################################
## THIS SCRIPT:
## Ingests EBD formatted file from eBird
## loads data into a nested dictionary (mongodb format)
## Calculates the date range of the EBD record OBSERVATION DATEs
## Retrieves records from MongoDB instance within the date range
## Loops through MongoDB records, compares "LAST_EDITED_DATE",
##		compares EBD and mongo record
##		updates MongoDB record with EBD record if EBD is newer
## Inserts any records from the EBD that did not match downloaded MongoDB 
## records
## NOTE: trigger on MongoDB site will keep versions of updated documents

## 5/1/2021
## updated to ingest newly formatted EBD File:
##
## 7/20/21
## updated to change formatting of observations from array to dictionary 
## with GUI as key
##
## 2/17/22
## updated OBSERVATION fields to include new EBD field: TAXON CONCEPT ID

## 9/17/24
## restructured to address issue: LAST UPDATED DATE does not change when
## reviewer changes data!
## Since the EBD is not sorted by checklist, each observation must be treated
## independently.

## The script now touches every record each time it runs.

## 1. Download all keys from the Atlas Cache, structures as a dictionary to use
## as a lookup. This allows evaluating if record
## needs update without having to make additional database queries.

## 2. Loop through EBD records (one observation per record). For each record,
## check against the dict in step 1 to determine:

## a. New checklist or updated checklist? (LE date<40d prior to curent version)
## b. New observation, updated observation, or BREEDING_CODE change?

## These evaluations deterine the update code to run on the Atlas Cache.
## Every checklist and observation is updated and evaluated, then marked
## as reviewed on the Atlas Cache by updating the NCBA_EBD_VER field to the
## EBD version (e.g., "Jul-2024")

## If the script is interupted, records marked as reviewed are skipped, and do
## not have to be evaluated again.


#############################################################################
## EXAMPLE MONGODB DOCUMENT: exampleAtlasCacheRecord.json


from datetime import datetime, timedelta
from dateutil import parser
import time
import os
from pymongo.mongo_client import MongoClient
# import mdbconn #stores database connection information
import certifi
import json
# import geopandas as gpd
# from shapely.geometry import Point
import nocturnal
import update_block_info
from ebd_functions import id_observer, get_spp_info 
import math
from mdbconn import connString

# import NCBA_AGOLEBirdBridge_v3

ebird_delim = "\t"
out_delim = ","
nl = "\n"
h = [] # header row list
fmt_dt = "%Y-%m-%d"
max_timeout = 100000000

# set up location of input file - EBD download format
in_drive = (
    "C:/Users/skanderson/State of North Carolina/" + 
    "WRC_NC Bird Atlas - Documents/Science Subcommittee"
    )
# in_file = "ebd_US-NC_202101_202407_relJun-2024.txt"
in_file = "ebd_US-NC_201501_202012_relJul-2025.txt"
current_ebd_ver = in_file[-12:-4]

update_run_dt = datetime.strftime(
    datetime.now(),
    "%Y-%m-%d %H:%M:%S.%f".rstrip("0")
    )

def last_day_of_month(any_day):
    # The day 28 exists in every month. 4 days later, it's always next month
    next_month = any_day.replace(day=28) + timedelta(days=4)
    # subtracting the number of the current day brings us back one month
    return next_month - timedelta(days=next_month.day)

# calculate pertinent dates
ncba_start_dt = datetime.strptime("2021-01-01", fmt_dt)

# get last date of data from filename
fn_data_date = in_file[-12:-8] + "01-" + in_file[-8:-4] # ex: Jun-01-2024
ft_data_dt = datetime.strptime(fn_data_date, "%b-%d-%Y")
last_data_dt = last_day_of_month(ft_data_dt)
days_since_start = (last_data_dt - ncba_start_dt).days

# check any record that has been updated more recently than 40 days ago
le_start_dt = last_data_dt - timedelta(days = 40)
le_start_dt_str = le_start_dt.strftime("%Y-%m-%d")

current_update_dt = last_data_dt.strftime("%Y-%m-%d")
current_update_dt_txt = last_data_dt.strftime("%b %d, %Y")
# # current_update_dt_txt = "Jun 30, 2024"
current_dt = datetime.strftime(datetime.now(), fmt_dt)

in_dir = "current_ebd"

print(
    "date checking",
    nl,
    "code_run_dt:", update_run_dt, nl,
    "last_data_dt:", last_data_dt, nl,
    "le_start_dt:", le_start_dt, nl,
    "current_update_dt:", current_update_dt, nl,
    "current_update_dt_txt:", current_update_dt_txt
)

# error file (if needed/testing)
e_drive = os.path.dirname(os.path.abspath(__file__))
e_file = "mongodb_errors.json"
e_fn = "/".join([e_drive, e_file])
e = open(e_fn,"w",encoding="utf-8")
# ac_local file (if needed/testing)

# # TESTING
# ml_file = "mongodb_local.json"
# ml_fn = "/".join([e_drive, ml_file])
# ml_out = open(ml_fn,"r",encoding="utf-8")
# # END TESTING


## SETUP CONNECTION TO MONGODB

client = MongoClient(
    connString(), 
    connectTimeoutMS=max_timeout,
    socketTimeoutMS = max_timeout,
    serverSelectionTimeoutMS=max_timeout,
    tlsCAFile=certifi.where()
    )

db = client.ebd_mgmt
# FOR PRODUCTION
ebd = db.ebd_prencba
ebd_err = db.ebd_upload_errlog
dbs = db.db_status

# clear previous error log
ebd_err.delete_many({})

# # FOR TESTING
# ebd = db.ebd_test
# # END TESTING

# FOR PRODUCTION
# status_query = { "_id" : "summary"}
# db_status = list(dbs.find(status_query))[0]
# db_dt_update = datetime.strptime(
#     db_status["MOST_RECENT_EBD_DATE"],
#     fmt_dt
#     )
# END PRODUCTION


# list of field added to EBD by atlas project
# Does not include NCBA_BC_HISTORY, an array object that holds the history
#   of Breeding Code changes.

atlas_fields = [
  "YEAR",
  "MONTH",
  "GEOM",
  "NCBA_REVIEW_DATE",
  "NCBA_REVIEWED",
  "NCBA_APPROVED",
  "NCBA_REVIEWER",
  "NCBA_COMMENTS",
  "ID_BLOCK_CODE",
  "ID_NCBA_BLOCK",
  "NCBA_BLOCK",
  "PRIORITY_BLOCK",
  "NOCTURNAL",
  "EBD_NOCTURNAL",
  "NCBA_NOCTURNAL",
  "NCBA_NOCTURNAL_DURATION",
  "NCBA_NOCTURNAL_PARTIAL",
  "NCBA_OBSDT_UTC",
  "NCBA_SEASON",
  "NCBA_JULIAN_DAY",
  "NCBA_WEEK",
  "NCBA_UPDATE_DATE",
  "NCBA_EBD_VER"
]

# list of observation fields is used to determine which records 
# belong in the checklist, and which should be copied to a nested 
# observation record
obsFieldsSpaces = [
    "TAXONOMIC ORDER",
    "CATEGORY",
    "COMMON NAME",
    "SCIENTIFIC NAME","SUBSPECIES COMMON NAME",
    "SUBSPECIES SCIENTIFIC NAME",
    "OBSERVATION COUNT",
    "BREEDING CODE",
    "BREEDING CATEGORY",
    "BEHAVIOR CODE",
    "AGE/SEX",
    "HAS MEDIA",
    "APPROVED",
    "REVIEWED",
    "REASON",
    "SPECIES COMMENTS",
    "GLOBAL UNIQUE IDENTIFIER",
    "TAXON CONCEPT ID"
    ]
obsFields = []

numIntFieldsSpaces = [
    "NUMBER OBSERVERS",
    "MONTH",
    "YEAR",
    "OBSERVATION COUNT",
    "APPROVED","REVIEWED",
    "HAS_MEDIA",
    "ALL_SPECIES_REPORTED"
    ]
numIntFields = []

numFloatFieldsSpaces = [
    "DURATION MINUTES",
    "EFFORT AREA HA",
    "EFFORT DISTANCE KM",
    "LATITUDE",
    "LONGITUDE"
    ]
numFloatFields = []

# months -> quarters crosswalk
months = {
    1: "Q1",
    2: "Q1",
    3: "Q1",
    4: "Q2",
    5: "Q2",
    6: "Q2",
    7: "Q3",
    8: "Q3",
    9: "Q3",
    10: "Q4",
    11: "Q4",
    12: "Q4"
    }


for i in range(len(obsFieldsSpaces)):
    obsFields.append(obsFieldsSpaces[i].replace(" ","_"))

# checklist field list, to be populated when header collected
#   = all header fields minus observation fields
checkFields = []

for i in range(len(numIntFieldsSpaces)):
    numIntFields.append(numIntFieldsSpaces[i].replace(" ","_"))


for i in range(len(numFloatFieldsSpaces)):
    numFloatFields.append(numFloatFieldsSpaces[i].replace(" ","_"))

########################################################################
#### CALCULATE SEASON
def getJDay (d):
    dt = datetime.strptime(d, fmt_dt)
    dtt = dt.timetuple()
    return dtt.tm_yday


breeding_start = getJDay("2021-03-01") #day 60
breeding_end = getJDay("2021-08-15") #day 227
winter_start = getJDay("2021-11-01") #day 305
winter_end = getJDay("2022-03-01") #day 60

def getSeason(d):
    jd = getJDay(d)
    r = "interim"
    if (breeding_start <= jd < breeding_end):
        r = "breeding"
    elif (winter_start <= jd or jd < winter_end):
        r = "wintering"

    return r


########################################################################
#### FUNCTIONS FOR GATHERING DATA FROM EBD

def get_check_data(r, checkFields):
    tempCheckDict = {}
    for f in checkFields:
        #checklist fields
        try:
            if f in numFloatFields:
                tempCheckDict[f] = float(r[f])
            elif f in numIntFields:
                tempCheckDict[f] = int(r[f])
            else:
                tempCheckDict[f] = r[f].strip()
        except:
            if f in numFloatFields:
                tempCheckDict[f] = 0
            elif f in numIntFields:
                tempCheckDict[f] = 0
            else:
                tempCheckDict[f] = ""

    tempCheckDict["_id"] = tempCheckDict["SAMPLING_EVENT_IDENTIFIER"]
    tempCheckDict["NCBA_UPDATE_BLOCK"] = "1"
    tempCheckDict.update(calc_ncba_data(tempCheckDict))

    return tempCheckDict

def get_obs_data(r, fprefix = ""):
    tempObsDict = {}
    
    for f in obsFields:

        try:
            if f in numFloatFields:
                tempObsDict[fprefix + f] = float(r[f])
            elif f in numIntFields:
                tempObsDict[fprefix + f] = int(r[f])
            else:
                tempObsDict[fprefix + f] = r[f].strip()
        except:
            if f in numFloatFields:
                tempObsDict[fprefix + f] = 0
            elif f in numIntFields:
                tempObsDict[fprefix + f] = 0
            else:
                tempObsDict[fprefix + f] = ""

        tempObsDict[fprefix + "NCBA_EBD_VER"] = current_ebd_ver
        tempObsDict[fprefix + "NCBA_BREEDING_CODE"] = ""
        tempObsDict[fprefix + "NCBA_BREEDING_CATEGORY"] = ""
        try: 
            tempObsDict[fprefix + "SGCN"] = get_spp_info(r["COMMON NAME"])["SGCN"]
        except: pass

    return tempObsDict


def calc_ncba_data(tempCheckDict):
    # adds the NCBA fields to the record

    # print(json.dumps(tempCheckDict))
    tempNcbaDict = {}
    currCheckId = tempCheckDict["SAMPLING_EVENT_IDENTIFIER"]
    currObsDate = tempCheckDict["OBSERVATION_DATE"]
    
    #add checklist as ID
    tempNcbaDict["_id"] = currCheckId
    #ADD NCBA FIELDS YEAR
    tempNcbaDict["YEAR"] = int(currObsDate[:4])
    #ADD NCBA FIELDS MONTH
    tempNcbaDict["MONTH"] = int(currObsDate[5:7])
    #add geoJSON field for point location
    tempNcbaDict["GEOM"] = {
        "type":"Point",
        "coordinates":[
            float(tempCheckDict["LONGITUDE"]),
            float(tempCheckDict["LATITUDE"])
            ]
        }
    
    #ADD NOCTURNAL FIELDS
    noc_data = nocturnal.getNocStatus(
        currCheckId,
        currObsDate,
        tempCheckDict["TIME_OBSERVATIONS_STARTED"],
        nocturnal.li,
        tempCheckDict["DURATION_MINUTES"]
    )

    tempNcbaDict[
        "NCBA_OBSDT_UTC"
        ] = noc_data["check_start_utc"]

    if len(tempCheckDict["TIME_OBSERVATIONS_STARTED"]) > 0:

        tempNcbaDict["EBD_NOCTURNAL"] = noc_data["noc_ebird"]
        tempNcbaDict["NCBA_NOCTURNAL"] = noc_data["noc_ncba"]
        tempNcbaDict[
            "NCBA_NOCTURNAL_DURATION"
            ] = noc_data["noc_duration"]
        tempNcbaDict[
            "NCBA_NOCTURNAL_PARTIAL"
            ] = noc_data["noc_partial"]
    
    else:
        tempNcbaDict["EBD_NOCTURNAL"] = ""
        tempNcbaDict["NCBA_NOCTURNAL"] = ""
        tempNcbaDict["NCBA_NOCTURNAL_DURATION"] = ""
        tempNcbaDict["NCBA_NOCTURNAL_PARTIAL"] = ""
        
    # ADD NCBA_SEASON, NCBA_QUARTER
    
    tempNcbaDict["NCBA_SEASON"] = getSeason(currObsDate)
    tempNcbaDict["NCBA_QUARTER"] = currObsDate[:4] + months[tempNcbaDict["MONTH"]]
    tempNcbaDict["NCBA_JULIAN_DAY"] = getJDay(currObsDate)
    tempNcbaDict["NCBA_WEEK"] = min([math.ceil(getJDay(currObsDate)/7),52])
    tempNcbaDict["NCBA_DATE_LAST_UPDATE"] = current_dt
    tempNcbaDict["NCBA_EBD_VER"] = current_ebd_ver

    # add volunteer/staff status

    tempNcbaDict["NCBA_OBSERVER"] = "volunteer"
    # tempNcbaDict["NCBA_OBSERVER"] = id_observer(
    #     tempCheckDict["OBSERVER_ID"],
    #     tempNcbaDict["NCBA_SEASON"],
    #     tempNcbaDict["YEAR"]
    # )
    return tempNcbaDict

def buildHistoryPush(ac, guid, ind={}):
    try:
        result = {
            "OBSERVATIONS.$[elem].NCBA_BC_HISTORY" : {
                "BREEDING_CODE" : ac["OBSERVATIONS"][guid]["BREEDING_CODE"],
                "BREEDING_CATEGORY" : ac["OBSERVATIONS"][guid]["BREEDING_CATEGORY"],
                "BEHAVIOR_CODE" : ac["OBSERVATIONS"][guid]["BEHAVIOR_CODE"],
                "NCBA_UPDATE_DATE" : current_update_dt,
                "NCBA_EBD_VER": ac["OBSERVATIONS"][guid]["NCBA_EBD_VER"]
                }
        }
    except Exception as errOut:
        msg = "buildHistoryPush err: " +  repr(errOut)
        ebdUpdateErrors(
            msg,
            ind,
            {},
            ac
        )
    return result

def checkBcUpdate(ac, rd):

    if (
        rd["BREEDING_CATEGORY"] != ac["BREEDING_CATEGORY"] or
        rd["BREEDING_CODE"] != ac["BREEDING_CODE"]
    ):
        result = True
    else:
        result = False
    return result

def ebdUpdateErrors(
        msg, # err msg
        ind, # indicator dict
        rd = {}, # row dict
        ac = {}, # atlas cache
        setCode = {}, 
        filterCode = {},
        arrayFilter = {}
        ):
    # pass results object, log error, return result
    # assemble record, remove empty components
    errOut = {}
    args= locals()
    del args["errOut"]

    for k,v in args.items():
        if v!= {}: errOut[k] = v
    

    errKey = datetime.strftime(
        datetime.now(),
        "%Y-%m-%d %H:%M:%S.%f".rstrip("0")
        )
    errOut.update(
        {
            "scriptRun": update_run_dt,
            "errTime": errKey
        }
    )

    # upload to Atlas Cache
    ebd_err.insert_one(
        errOut
    )

########################################################################
#### LOAD FROM ATLAS CACHE DOWNLOADED FILE
#### ebd_mgmt.EBD_PRENCBA_RECORD_INFO.json

mdb_record_list = json.load(
    open("ebd_mgmt.EBD_PRENCBA_RECORD_INFO.json", "r", encoding = "utf-8-sig")
)

# load into local dictionary for reference
ac_local = {}
ac_n_checklists = 0
ac_rev_checklists = 0 # num checklists reviewed for this ebd ver
ac_n_observations = 0
ac_rev_observations = 0 # num observations reviewed for this ebd ver
for i in mdb_record_list:
    ncbacheckebdver = ""
    if "NCBA_EBD_VER" in i.keys(): ncbacheckebdver = i["NCBA_EBD_VER"]
    if ncbacheckebdver == current_ebd_ver:
        ac_rev_checklists += 1

    ac_local[i["_id"]] = {
        "NCBA_EBD_VER" : ncbacheckebdver,
        "LAST_EDITED_DATE" : i["LAST_EDITED_DATE"],
        "OBSERVATIONS" : {}
    }
    ac_n_checklists += 1
    for o in i["OBSERVATIONS"]:
        to = o #temp dict to mess with
        try:
            if "NCBA_EBD_VER" not in to.keys(): 
                # add NCBA_EBD_VER element if it doesn't exist
                to["NCBA_EBD_VER"] = ""

            #add new obs to ac_local for this checklist
            ac_local[i["_id"]]["OBSERVATIONS"][to.pop("GLOBAL_UNIQUE_IDENTIFIER")] = to

            if to["NCBA_EBD_VER"] == current_ebd_ver:
                ac_rev_observations += 1
            ac_n_observations += 1
        except Exception as errOut:
            ebdUpdateErrors(
                repr(errOut),
                o
            )

# END FOR PRODUCTION


avg_observations_day = 8812
num_observations_total = avg_observations_day * days_since_start 
print(
    "ac_local populated",
    nl,
    "ac_local observations", nl,
    str(ac_n_observations),nl,
    "ac_local reviewed observations", nl,
    str(ac_rev_observations), nl,
    "days since NCBA start",
    str(days_since_start),
    nl,
    "estimated",
    str(num_observations_total),
    "observations to check." 
)

# # FOR TESTING
# # ADD TO LOCAL FILE
# # ml_out.write(json.dumps(ac_local))
# # print("ac_local written to local ml_out file")
# # exit()
# # END TESTING

########################################################################
#### MAIN FUNCTION

def main():
    now = datetime.utcnow()
    now = now.replace(tzinfo=None)

    # # TESTING
    # # monitor execution times

    # # END TESTING

    count = 0 #count observations
    countc = 0 #count checklists
    countu = 0 #count observations updated
    countf = 0 #count observations failed to update
    counts = 0 #count observations skipped

    start = time.perf_counter()
    start_dt = datetime.now()
    loop_time = start
    currCheckId = "" #stores the current SAMPLING EVENT IDENTIFIER
    checksChecked = set() #records marked with current EBD VER or have been processed.

    print(
        "begin looping through records:",
        start_dt
    )

    i_fn = "/".join([in_drive,in_dir,"2020_EBD_Records_PreAtlas",in_file])
    ind = {
        "countRecs": {
            "cNew" : 0,
            "cUpdate" : 0,
            "cSkip" : 0,
            "cRevSkip" : 0,
            "oNew" : 0,
            "oUpdate" : 0,
            "oUpdateBc" : 0,
            "oSkip" : 0,
            "oRevSkip" : 0
        }
    }
    ind_blank = {
        "checkNewUpdateSkip" : "skip", # New, Update, or Skip checklist
        "checkNotReviewed" : True,  # assume not reviewed, change otherwise
        "obsNotReviewed" : True,  # assume not reviewed, change otherwise
        "obsNewUpdateSkip" : "skip", # New, Update, or Skip Obs
        "leNew" : False, #last edit date newer than Atlas Cache
        "obsBcChanged" : False, # Behavior Code changed
        "updateACData" : False, # True if data to be updated, False for jsut review
        "upsert" : False
    }
    obsBatchUpdate = set()
    checkBatchUpdate = set()
    ##########################################################################
    ##########################################################################
    ## LOOP THROUGH EBD
    with open(i_fn, "r", encoding="utf-8") as f:
        for line in f:
            line = line.replace(
                ebird_delim + "\n" , ""
                ).replace(
                    "\n",""
                    ).replace(
                        "'",""
                        ) #remove final delimiter
            r = line.split(ebird_delim) #split by EBD delimiter (tab)
            if count == 0: # header row
                # collect header row as array,
                # set index variables for important fields
                line = line.replace(" ","_")
                h = line.split(ebird_delim)

                # set checkFields array, used in get_check_data function
                checkFields = list(set(h) - set(obsFields))
                print("\n==============\nHEADERS:\n", h)

            else: # all other lines

                # loop through data, populate row_dict
                row_dict = {}
                for i,d in enumerate(r): row_dict[h[i]] = d.strip()

                ###########################################################
                ## Reset variables
                #SAMPLING EVENT IDENTIFIER
                currCheckId = row_dict["SAMPLING_EVENT_IDENTIFIER"]
                #GLOBAL UNIQUE IDENTIFIER
                currGlobalId = row_dict["GLOBAL_UNIQUE_IDENTIFIER"]
                currACLocal = {} #holds the keys for AC record (if exists)
                setCode = {}
                
                # reset indicators
                ind.update(ind_blank)
                ind["sei"] = currCheckId
                ind["guid"] = currGlobalId
                # check last edited date
                le_dt_fmt = datetime.strptime(
                    row_dict["LAST_EDITED_DATE"][:10],
                    fmt_dt
                )

                ###########################################################
                # calculate indicator data for current record
                
                # DETERMINE CHECKLIST STATUS

                # does this checklist exist on atlas cache?
                if currCheckId in ac_local.keys():
                    # load current checklist record
                    currACLocal = ac_local[currCheckId]


                # has checklist been reviewed during this code run?
                if currCheckId in checksChecked:
                    ind["checkNotReviewed"] = False # type: ignore

                else: # not reviewed this code run
                    # is the checklist in the atlas cache?
                    if currACLocal:
                        # checklist in atlas cache, has it been reviewed
                        #   on a previous code run?

                        if currACLocal["NCBA_EBD_VER"] != current_ebd_ver:
                            # checklist in atlas cache, has not been reviewed

                            # has it been updated?
                            if le_dt_fmt > le_start_dt:
                                # last edit date after start date
                                # checklist and observation updated.
                                ind["checkNewUpdateSkip"] = "update" # type: ignore
                                ind["leNew"] = True # type: ignore
                        else:
                            # checklist reviewed on previous code run
                            ind["checkNotReviewed"] = False # type: ignore
                            ind["countRecs"]["cRevSkip"] += 1

                    else:
                        # checklist not on AC, not reviewed during this code run
                        # create new checklist and obs record
                        ind["checkNewUpdateSkip"] = "new" # type: ignore


                # DETERMINE OBSERVATION STATUS
                # note: no observations from ebd have been reviewed
                #       this code run.

                # check to see if this observation exists on atlas cache

                if currACLocal and currGlobalId in currACLocal["OBSERVATIONS"].keys():
                    # observation exists on atlas cache.
                    # has this record been reviewed on a previous code run?
                    if currACLocal["OBSERVATIONS"][currGlobalId]["NCBA_EBD_VER"] != current_ebd_ver:
                        # obs not reviewed on previous code run
                        # only update if LE date new
                        if ind["leNew"]:
                            ind["obsNewUpdateSkip"] = "update" # type: ignore
                        
                        # regardless of LE date,
                        # see if the breeding codes have changed
                        # if so, make sure to add bchistory record
                        ind["obsBcChanged"] = checkBcUpdate( # type: ignore
                            row_dict,
                            currACLocal["OBSERVATIONS"][currGlobalId]
                        )
                    else:
                        # obs reviewed in previous code run
                        ind["obsNotReviewed"] = False # type: ignore
                        ind["countRecs"]["oRevSkip"] += 1


                else:
                    # observation does not exist on atlas cache
                    ind["obsNewUpdateSkip"] = "new" # type: ignore



                ###########################################################
                ###########################################################
                ###########################################################
                # process record
                # has this record been reviewed for this EBD_VER?
                # if so, skip
                if ind["obsNotReviewed"]:
                
                    # This Observation has not been reviewed
                    # under this EBD version yet.
                    # The checklist may or may not have been reviewed.
                    # will never have the case of the obs reviewed and 
                    #   checklist not reviewed!

                    # populate default values for update code
                    # default code updates check field "NCBA_EBD_VER"
                   
                    filterCode = {
                        "OBSERVATIONS.GLOBAL_UNIQUE_IDENTIFIER" : currGlobalId
                    }
                    setCode = {
                        "$set" : {
                            "NCBA_EBD_VER" : current_ebd_ver
                        },
                        "$push" : {}
                    }
                    arrayfilterCode = [
                        {"elem.GLOBAL_UNIQUE_IDENTIFIER" : currGlobalId}
                    ]
                    
                    ###########################################
                    ## CHECKLIST REVIEW
                    if ind["checkNotReviewed"]:
                        # checklist not reveiwed
                        match ind["checkNewUpdateSkip"]:
                            case "new" | "update":
                                # new or updated checklist since last update
                                # add EBD fields to the update code
                                setCode["$set"].update(
                                    get_check_data(
                                        row_dict,
                                        checkFields
                                    )
                                )

                                if ind["checkNewUpdateSkip"] == "new":
                                    ind["countRecs"]["cNew"] += 1
                                    ind["upsert"] = True # type: ignore
                                else:
                                    ind["countRecs"]["cUpdate"] +=1

                            case "skip":
                                # update EBD with NCBA_EBD_VER = curr ebd ver
                                # already in default setCode dict
                                pass

                        # add to list of checklists checked during code run
                        checksChecked.add(currCheckId)

                    ###########################################
                    ## OBSERVATION REVIEW

                    # checklist update sorted, move on to observation
                    match ind["obsNewUpdateSkip"]:
                        case "new":
                            # new observation to push, change
                            # filter code to look for checklist, not obs
                            filterCode = {
                                "SAMPLING_EVENT_IDENTIFIER" : currCheckId
                            }
                            # if new checklist
                            if ind["checkNewUpdateSkip"] == "new":
                                # add new observation to set code
                                tObs = get_obs_data(row_dict)
                                tObs["NCBA_BC_HISTORY"] = []
                                setCode["$set"]["OBSERVATIONS"]= []
                                setCode["$set"]["OBSERVATIONS"].append(
                                    tObs
                                )

                                arrayfilterCode = []
                                ind["updateACData"] = True # type: ignore
                            else:
                                #existing checklist, new obs
                                #push new record to existing observations

                                setCode["$push"] = {
                                    "OBSERVATIONS" : get_obs_data(
                                        row_dict
                                        )
                                    }
                                arrayfilterCode = []

                                ind["updateACData"] = True # type: ignore

                            ind["countRecs"]["oNew"] += 1
                            
                        case "update":
                            # update existing observation

                            setCode["$set"].update(
                                get_obs_data(
                                    row_dict,
                                    fprefix = "OBSERVATIONS.$[elem]."
                                    )
                            )

                            # if BC changed, add history record
                            if ind["obsBcChanged"]:
                                setCode["$push"].update(
                                    buildHistoryPush(
                                        currACLocal,
                                        currGlobalId,
                                        ind
                                    )
                                )
                                ind["countRecs"]["oUpdateBc"] += 1

                            ind["updateACData"] = True # type: ignore
                            ind["countRecs"]["oUpdate"] += 1

                        case "skip":
                            # existing obs record,
                            # no changes since last review,
                            # set NCBA_EBD_VER indicator
                            setCode["$set"].update(
                                {"OBSERVATIONS.$[elem].NCBA_EBD_VER" : current_ebd_ver}
                            )
                            ind["updateACData"] = False

                            # if BC changed, add code
                            if ind["obsBcChanged"]:
                                setCode["$set"].update(
                                    {
                                    "OBSERVATIONS.$[elem].BREEDING_CODE" : row_dict["BREEDING_CODE"], 
                                    "OBSERVATIONS.$[elem].BREEDING_CATEGORY" : row_dict["BREEDING_CATEGORY"]
                                    }
                                )

                                setCode["$push"].update(
                                    buildHistoryPush(
                                        currACLocal,
                                        currGlobalId,
                                        ind
                                    )
                                )
                                ind["updateACData"] = True
                                ind["countRecs"]["oUpdateBc"] += 1

                            ind["countRecs"]["oSkip"] += 1
                            counts += 1

                    ###########################################################
                    ### Query code built, run to update AC  
                    if ind["updateACData"]:
                        try:
                            ebd.update_one(
                                filterCode,
                                setCode,
                                upsert = ind["upsert"], # type: ignore
                                array_filters = arrayfilterCode
                            )
                            countu += 1 # count updated bc data obs    
                        except Exception as errOut:
                            msg = "Update Failed: " + repr(errOut)
                            ebdUpdateErrors(
                                msg,
                                ind,
                                row_dict,
                                currACLocal,
                                setCode,
                                filterCode,
                                arrayfilterCode
                            )
                            countf += 1
                    else:
                        # no data to update,
                        # add to set to update NCBA_EBD_VER as a batch
                        obsBatchUpdate.add(currGlobalId)
                        checkBatchUpdate.add(currCheckId)
                else:
                    counts += 1

            count += 1 #count observations

            # display some info to know it is running!
            count_prompt = count % 10000
            if count_prompt == 0:

                ## Calculate time
                nowt = time.perf_counter()
                elapsed_time = nowt - start
                elapsed_time_str = str(round(elapsed_time,1))
                secs_per_rec = elapsed_time/count
                est_total_sec = secs_per_rec * num_observations_total
                est_hrs_remaining = round(
                    ((est_total_sec - elapsed_time)/60)/60,
                    1)
                est_end_time = start_dt + timedelta(
                    seconds = est_total_sec
                    )
                
                ###################################
                ## BATCH Update NCBA_EBD_VER
                checkBatchList = list(checkBatchUpdate)
                obsBatchList = list(obsBatchUpdate)

                ebd.update_many(
                    {u"_id": {
                        "$in" : checkBatchList
                    }},
                    {
                        "$set": {
                            "NCBA_EBD_VER" : current_ebd_ver
                        }
                    }
                )

                ebd.update_many(
                    {"OBSERVATIONS.GLOBAL_UNIQUE_IDENTIFIER": {
                        "$elemMatch": {
                            "$in" : obsBatchList
                            }
                        }
                    },
                    {
                        "$set": {
                            "OBSERVATIONS.$[elem].NCBA_EBD_VER" : current_ebd_ver
                        }
                    },
                    upsert = False,
                    array_filters=[
                        {
                            "elem.GLOBAL_UNIQUE_IDENTIFIER": {
                                "$in" : obsBatchList
                            }
                        }
                    ]
                )
                
                # update counts
                ind["countRecs"]["cSkip"] += len(checkBatchList)
                ind["countRecs"]["oSkip"] += len(obsBatchList)
                # empty the sets
                obsBatchUpdate = set()
                checkBatchUpdate = set()

                ###################################
                ## Print out progress info
                print (nl + "== " + str(count) + " ==")
                print (
                    "== ",
                    "elapsed time: ",
                    elapsed_time_str,
                    "s loop time: ",
                    str(round(nowt - loop_time,1)),
                    "s ==",
                    nl,
                    "Current Record: ", 
                    currGlobalId,
                    nl, 
                    "Est Hrs Remaining: ",
                    str(est_hrs_remaining), nl,
                    "Est End Time: ",
                    str(est_end_time),
                    nl,
                    "Records Updated:",
                    str(countu),
                    nl,
                    "Failed Updates:",
                    str(countf),
                    nl,
                    "Obs Skipped:",
                    str(counts)
                    )
                print(
                    "Rec Count:", nl,
                    json.dumps(ind["countRecs"])
                )
                loop_time = nowt

    ###########################################################################
    ## completed loop through all EBD records
    ## update block information for new records
    
    #print results
    print (
        nl +
        "== " +
        str(count) +
        " rows evaluated - " +
        str(countc) +
        " checklists found ==" + 
        nl + 
        "== " +
        str(countu) + 
        " observations updated ==", nl,
        "final count stats:", nl,
        json.dumps(ind["countRecs"])
        )
    
    print (nl + "============================================================")

    ###########################################################################
    ## code for incorporating block names - retrieve using geopandas
    ## from a copy of the AtlasCache blocks table (transformed to geojson)
    ## perform spatial join    
    try:
        update_block_info.main()
    except:
        print(
            "Block update failed!"
        )
        
    ## THIS FUNCTION IS BROKEN
    ## update the ArcGIS Layer online (see other script for details)
    # print(nl + "== Updating ArcGIS =="+ nl)

    # NCBA_AGOLEBirdBridge_v3.main()

    # print(nl + "== ArcGIS Update Complete =="+ nl)
    ## END BROKEN SECTION
    
    ## update database status
    # dbs.update_one(
    #     {u"_id" : "summary"},
    #     {
    #         "$set" : {
    #             "MOST_RECENT_EBD_DATE" : current_update_dt,
    #             "MOST_RECENT_EBD_DATE_TEXT": current_update_dt_txt,
    #             "NCBA_EBD_VER" : current_ebd_ver
    #         }
    #     }
    # )


if __name__=="__main__":
    main();
