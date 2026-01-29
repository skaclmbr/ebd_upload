##########################################################################
## Code to import monthly hiddent checklist file from Cornell
## Format differs from EBD
## only contains NC Bird Atlas project records (EBIRD_ATL_NC)

## Scott K. Anderson
## github.com/skaclmbr
## 2025-04-22

## IMPORTANT NOTES #######################################################
## FIELD NAMES
## do not match standard EBD format
##
## SPECIES
## some species observations are on more than one line
##
## DURATION
## duration given in hours, not minutes
##
## USER
## first name and last name provided

from datetime import datetime, timedelta
import time
from pymongo.mongo_client import MongoClient
import certifi
import json
from weekly_functions import get_update_dates, Checklist, Observation, bc_xwalk
from mdbconn import connString

ebird_delim = "\t"
out_delim = ","
nl = "\n"
h = [] # header row list
fmt_dt = "%Y-%m-%d"
max_timeout = 100000000


##############################################################################
## SETUP INPUT FILE
# set up location of input file
# monthly, the eBird Dataset (EBD) is available. It contains all records in
#   eBird (both Atlas and regular)
#
# weekly, the weekly download is available. It differs from the EBD in several
#   ways:
#   - only portal/project records (PROJECT_CODE = "EBIRD_ATL_NC")
#   - only observations with species records present (e.g., no sp., hybrids)
#   - only observations where BREEDING_CODE is recorded (i.e., never blank)
#   - first and last name of observer provided
#   - column headings are different, columns have different data
#   - "obs_id" field has the last component of the GLOBAL_UNIQUE_IDENTIFIER
#   - can have one observation record spread across multiple rows

in_drive = (
    "C:/Users/skanderson/State of North Carolina/" + 
    "WRC_NC Bird Atlas - Documents/Science Subcommittee"
    )
in_dir = "current_ebd"

# in_file = "North Carolina Bird Atlas _full data_-2025_06_03-03_02_04_458-JICeK-110-102.tsv"
# HIDDEN FILE FORMAT
# in_file = "North Carolina BBA User-hidden records-2025_06_01-04_11_14_412-Eed7E-80-37.tsv"
# in_file = "North Carolina BBA User-hidden records-2025_06_17-03_10_55_859-asnMt-80-37.tsv"
# in_file = "North Carolina BBA User-hidden records-2025_10_01-04_01_19_393-gZTDf-80-37.tsv"
in_file = "North Carolina BBA User-hidden records-2025_11_01-04_00_55_207-QVWHo-80-37.tsv"
input_file_weekly = True

h_to_w_xwalk = {
    "global_unique_identifier" : "obs_id",
    "sampling_event_identifier" : "sub_id",
    "orig_species_code" : "orig_species_code",
    "common_name" : "primary_com_name",
    "reviewed" : "reviewed",
    "how_many_atleast" : "how_many_atleast",
    "how_many_atmost" : "how_many_atmost",
    "behavior_code" : "aux_code",
    "species_comments" : "obs_comments",
    "group_identifier" : "group_id",
    "protocol_code" : "protocol_id",
    "locality_id" : "loc_id",
    "atlas_block" : "region_code",
    "state_code" : "subnational1_code",
    "observer_id" : "user_id",
    "last_name" : "last_name",
    "first_name" : "first_name",
    "duration_hrs" : "duration_hrs",
    "all_species_reported" : "all_obs_reported",
    "trip_comments" : "sub_comments",
    "to_char" : "date_observed",
    "last_edited_dt" : "date_last_edited",
    "obs_time_valid" : "obs_time_valid",
    "checklist_id" : "checklist_id",
    "number_observers" : "num_observers",
    "effort_distance_km" : "effort_distance_km",
    "latitude" : "latitude",
    "longitude" : "longitude"
}
## FOR TESTING ###############################################################

# REFERENCE - EBD FILE FORMAT
# in_file = "ebd_US-NC_202101_202504_relMar-2025.txt" 

# WEEKLY FILE FORMAT
# in_file = "North Carolina Bird Atlas _test data_-2025_04_29-03_01_16_151-hDMGw-110-102.tsv"

# DOES THE IMPUT FILE INCLUDE ALL OBSERVATIONS FOR THE CHECKLIST? NO!
# REMOVED OBSERVATIONS WILL NOT BE CAPTURED UNTIL MONTHLY EBD UPDATE
# S138163379 - le 5/1/25, OBS1730385505 aux_code changed to S7
# S222172917 - in AC, le 5/1/25, add bhvi observation 
# S222041503 - in AC, LE 3/31/25, OBS3011201146 bc update only
# S224098138 - new checklist
# S223857343 - new checklist
# S112979937 - in AC, LE update date = 3/18/25 - NOT IN FILE
# S138204623 - in AC, LE update date = 3/18/25 - NOT IN FILE
# S148217336 - in AC, LE update date = 3/18/25 - NOT IN FILE
# S93467687 - in AC, LE update date = 3/18/25 - NOT IN FILE

# ["S138163379", "S148217336", "S138204623", "S112979937", "S112979937", "S112979937", "S112979937", "S93467687", "S222172917", "S222041503"]
## END TESTING ###############################################################

# is the file format weekly (true) or EBD (false)?


##############################################################################
## Calculate pertinent dates
# used to track when records have been updated

# current_ebd_ver = YYYY-MM-DD for weeklies, Mmm-YYYY for EBD
# EBD should update any weekly records prior to last_data_dt
# weeklies should update all relevant records.


update_dates = get_update_dates(in_file.replace("-"," ",1), input_file_weekly)
file_version = update_dates["current_ebd_ver"]

print(
    "Gathering Update Dates",
    nl,
    "file_version:", update_dates["current_ebd_ver"], nl,
    "code_run_dt:", update_dates["update_run_dt"], nl,
    "last_data_dt:", update_dates["last_data_dt"], nl,
    "current_update_dt:", update_dates["current_update_dt"], nl,
    "current_update_dt_txt:", update_dates["current_update_dt_txt"]
)

##############################################################################
## SETUP CONNECTION TO MONGODB

client = MongoClient(
    connString(), 
    connectTimeoutMS=max_timeout,
    socketTimeoutMS = max_timeout,
    serverSelectionTimeoutMS=max_timeout,
    tlsCAFile=certifi.where()
    )

# set up connections
db = client.ebd_mgmt
ebd = db.ebd
ebd_err = db.ebd_upload_errlog
blocks = db.blocks

## FOR TESTING ################################################################
# ebd = db.ebd_test
# ebd_bc_history = db.ebd_bc_history_test
## FOR TESTING ################################################################


# database status
# retrieve last record date
dbs = db.db_status
db_status = dbs.find_one({u"_id":"summary"})
most_recent_ebd_date_str = db_status["MOST_RECENT_EBD_DATE"] # type: ignore
most_recent_ebd_date_dt = datetime.strptime(
    db_status["MOST_RECENT_EBD_DATE"], # type: ignore
    fmt_dt
)
update_dates["most_recent_ebd_date"] = most_recent_ebd_date_str
print(nl, "DB Last Record Date:", most_recent_ebd_date_str, nl)

def get_guid(obs_id):
    # convert obs_id to GUID
    if "URN:CornellLabOfOrnithology:EBIRD:" in obs_id:
        return(obs_id)
    else:
        return "URN:CornellLabOfOrnithology:EBIRD:" + obs_id

def format_number_with_commas(number):
  """Formats a number with commas as thousands separators."""
  return "{:,}".format(number)

# import entire file into a dictionary
file_data = {}
checklists = set()

#keep track of atlas cache actions
check_actions = {}

##############################################################################
## POPULATE BLOCK DATA

print(
    nl, "=======================================", nl, 
    "Retrieving Block Data"
    )

q = {}
p = {
    "ID_EBD_NAME" : 1,
    "ID_NCBA_BLOCK" : 1,
    "ID_BLOCK_CODE" : 1,
    "PRIORITY" : 1,
    "ECOREGION" : 1,
    "COUNTY" : 1
}
cursor = blocks.find(q, p)
cursor_list = list(cursor)
block_lookup = {}

for b in cursor_list:
    block_lookup[b["ID_BLOCK_CODE"]] = {
        "ID_NCBA_BLOCK" : b["ID_NCBA_BLOCK"],
        "ID_EBD_NAME" : b["ID_EBD_NAME"],
        "PRIORITY" : b["PRIORITY"],
        "ECOREGION" : b["ECOREGION"],
        "COUNTY" : b["COUNTY"]
    }


print(
    nl, "=======================================", nl, 
    "Importing file", nl,
    in_file
    )

##############################################################################
## POPULATE FILE DATA
i_fn = "/".join([in_drive,in_dir,in_file])
with open(i_fn, "r", encoding="utf-8") as f:
    count = 0
    for line in f:
            #remove final delimiter
            line = line.replace(
                ebird_delim + "\n" , ""
                ).replace(
                    "\n",""
                    ).replace(
                        "'",""
                        ) 
            #split by EBD delimiter (tab)
            r = line.split(ebird_delim)

            if count == 0:
                # header row
                # collect header row as array
                h = r
                count += 1 

            else: # all other lines
                # create dictionary from header and row data

                row_data = {}
                row_data_temp = dict(zip(h, r))

                if row_data_temp["taxon_category"] in ["species", "issf"]:
                    # rename row_data fields to match weekly
                    for heading, data in row_data_temp.items():
                        if heading in h_to_w_xwalk.keys():
                            row_data[h_to_w_xwalk[heading]] = data
                        
                    
                    curr_checklist_id = row_data["sub_id"]
                    curr_global_id = get_guid(row_data["obs_id"])
                    
                    if curr_checklist_id not in checklists:
                        # checklist has not been evaluated this code run
                        checklists.add(curr_checklist_id)

                        # add block data
                        try:
                            row_data.update(block_lookup[row_data["region_code"]])
                        except:
                            pass

                        curr_checklist = Checklist(
                            row_data,
                            update_dates["current_ebd_ver"],
                            update_dates["current_update_dt"]
                            )

                        # mark as a hidden record
                        curr_checklist.hide_record()

                        file_data[curr_checklist_id] = curr_checklist.get_checklist_record()

                    if curr_global_id not in file_data[curr_checklist_id]["OBSERVATIONS"]:
                        # observation is new
                        curr_obs = Observation(
                            row_data,
                            file_version
                        )
                        file_data[curr_checklist_id]["OBSERVATIONS"][curr_global_id] = curr_obs.get_obs_record()
                        
                    else:
                        # observation exists, check aux_code
                        if row_data["aux_code"] in bc_xwalk.keys():
                            # if aux_code in weekly file is valid (i.e.,
                            # not "adult|f"), gather obs data

                            curr_obs = Observation(
                                row_data,
                                file_version
                            )
                            file_data[curr_checklist_id]["OBSERVATIONS"][curr_global_id] = curr_obs.get_obs_record()

            count += 1
            if count % 100 == 0:
                print(
                    nl, "++++++++++++++++++++", nl,
                    "imported",
                    format_number_with_commas(count),
                    "lines", nl,
                    format_number_with_commas(len(file_data)), "checklists"
                )

checklists_to_import = len(file_data)
print(
    nl,
    format_number_with_commas(checklists_to_import),
    "total checklists found",
    nl
)

##############################################################################
## LOG ERRORS/STATUS TO DATABASE
def ebdUpdateErrors(
        msg, # err msg
        # ind, # indicator dict
        fd = {}, # row dict
        ac = {}, # atlas cache
        mdb_code = {}
        ):
    # pass results object, log error, return result
    # assemble record, remove empty components
    errOut = {}
    args= locals()
    del args["errOut"]

    for k,v in args.items():
        if v!= {}: errOut[k] = v
    
    errOut["update_dates"] = update_dates

    errKey = datetime.strftime(
        datetime.now(),
        "%Y-%m-%d %H:%M:%S.%f".rstrip("0")
        )
    errOut.update(
        {
            "scriptRun": update_dates["update_run_dt"],
            "errTime": errKey
        }
    )

    # upload to Atlas Cache
    ebd_err.insert_one(
        errOut
    )


def ebdUpdateStatus(
    msg = "Update Status",
    checks = {}
    ):

    runKey = datetime.strftime(
        datetime.now(),
        "%Y-%m-%d %H:%M:%S.%f".rstrip("0")
        )
    
    runOut = {
        "msg" : msg,
        "checks" : checks,
        "update_dates" : update_dates,
        "scriptRun" : update_dates["update_run_dt"],
        "endTime" : runKey
    }
    ebd_err.insert_one(runOut)


##############################################################################
## Check if LE date is after the last record date.
dt_formats = [
    "%Y-%m-%d %H:%M:%S",
    "%m-%d-%Y %H:%M:%S"
]
def checklist_updated(file_le):
    # evaluates if last edit date > the date of the last db update
    for f in dt_formats:
        # try:
        if "." in file_le:
            file_le = file_le.split(".")[0]
        
            file_le_dt = datetime.strptime(
                file_le,
                "%Y-%m-%d %H:%M:%S"
            )
        elif "-" in file_le:
            file_le_dt = datetime.strptime(
                file_le,
                "%Y-%m-%d %H:%M:%S"
            )

        else:
            file_le_dt = datetime.strptime(
                file_le,
                "%m/%d/%Y %H:%M:%S"
            )

            
        # except:
        #     continue

    
    if file_le_dt > most_recent_ebd_date_dt:
        # file is more recent
        return True
    else:
        return False


##############################################################################
## ASSEMBLE CODE TO UPDATE ATLAS CACHE/MONGODB
def get_mongodb_update_code(ac, checklist, mdb_code):
    # create code to update checklist
    # output will be two sets of code
    # one for an upsert operation,
    # one for adding new observations
    result = mdb_code
    
    checklist_id = checklist["SAMPLING_EVENT_IDENTIFIER"]
    check_actions[checklist_id]["action"] = "update"

    # loop through observations, check if new exist, update others
    for guid, obs in checklist["OBSERVATIONS"].items():
        if guid in ac["OBS_BC"].keys():
            
            check_actions[checklist_id]["observations"][guid] = "update"

            # update existing observation
            obs_set = {}
            # exists in Atlas Cache, create update code
            obs_elem = guid.split(":")[-1].lower()
            for k, v in obs.items():
                obs_set[f"OBSERVATIONS.$[{obs_elem}].{k}"] = v

            # add to set code
            result["update_code"]["set_code"]["$set"].update(
                obs_set
            )

            # add to array filters
            result["update_code"]["array_filter_code"].append(
                {f"{obs_elem}.GLOBAL_UNIQUE_IDENTIFIER" : guid}
            )
        else:
            # does not exist in Atlas Cache,
            # create query code to insert new observation
            check_actions[checklist_id]["observations"][guid] = "insert"
            mdb_code["insert_code"]["ind"] = True

            push_obs = {}
            for k, v in obs.items():
                push_obs[k] = v

            result["insert_code"]["set_code"]["$push"]["OBSERVATIONS"]["$each"].append(
                push_obs
            )

    # create query code to update checklist items
    for k, v in checklist.items():
        if k != "OBSERVATIONS":
            result["update_code"]["set_code"]["$set"][k] = v

    return result

def get_mongodb_insert_code(checklist):

    checklist_id = checklist["SAMPLING_EVENT_IDENTIFIER"]
    check_actions[checklist_id]["action"] = "insert"

    checklist["_id"] = checklist_id

    # change observations to array instead of dict
    obs_dict = checklist["OBSERVATIONS"]
    checklist["OBSERVATIONS"] = []
    for o in obs_dict.values():
        check_actions[checklist_id]["observations"][o["GLOBAL_UNIQUE_IDENTIFIER"]] = "insert"
        checklist["OBSERVATIONS"].append(o)

    mdb_code = { "$set" : checklist}

    return mdb_code


##############################################################################
## LOOP THROUGH FILE RECORDS, UPDATE ATLAS CACHE
def main():

    print(
        nl, "=======================================", nl, 
        "Updating Atlas Cache", nl
        )
    # upload to MongoDB
    notify_frequency = 1000
    start = time.perf_counter()
    start_dt = datetime.now()
    loop_time = start

    checklist_count = 0
    checklist_updated_count = 0
    checklist_inserted_count = 0

    # loop through checklists from input file
    for checklist_id in file_data:
        # get the current checklist record
        curr_checklist = file_data[checklist_id]
        check_actions[checklist_id] = {"action": "none", "observations":{}}

        curr_ac_record = {}

        # check database for checklist
        # returns JSON object with OBSERVATIONS as array of all observations
        cursor = list(ebd.find(
            {"_id": checklist_id},
            {
                "_id": 1,
                "NCBA_EBD_VER": 1,
                "NCBA_DATE_LAST_UPDATE": 1,
                "LAST_EDITED_DATE": 1,
                "OBSERVATIONS.GLOBAL_UNIQUE_IDENTIFIER": 1,
                "OBSERVATIONS.BREEDING_CODE": 1
            }
        ))

        if cursor:
            # record exists on atlas cache, get data
            curr_ac_record = cursor[0]

            # loop through ac observations list, create dict
            # with guids as keys, breeding codes as values
            curr_ac_record["OBS_BC"] = {}
            for o in curr_ac_record["OBSERVATIONS"]:
                curr_ac_record["OBS_BC"][o["GLOBAL_UNIQUE_IDENTIFIER"]] = o["BREEDING_CODE"]

            del curr_ac_record["OBSERVATIONS"]

            mdb_code = {
                "insert_code" : {
                    "ind" : False,
                    "set_code" : {
                        "$push" : {
                            "OBSERVATIONS" : {"$each" : []}
                        }
                    },
                    "array_filter_code" : [],
                    "upsert" : True
                },
                "update_code" : {
                    "ind" : False,
                    "set_code":{
                        "$set" : {}
                        },
                    "array_filter_code" : [],
                    "upsert" : True
                }
            }
            
            # check if checklist needs updating or inserting
            if checklist_updated(curr_ac_record["LAST_EDITED_DATE"]):
                # last edited date is later than db_update_date

                # print("- checklist updated - ", checklist_id)
                mdb_code["update_code"]["ind"] = True

                # get mdb code to update checklist
                mdb_code = get_mongodb_update_code(
                    curr_ac_record,
                    curr_checklist,
                    mdb_code
                )

                # Update the Atlas Cache!
                try:
                    ebd.update_one(
                        {u"_id" : checklist_id},
                        mdb_code["update_code"]["set_code"],
                        array_filters=mdb_code["update_code"]["array_filter_code"],
                        upsert = True
                    )
                    checklist_updated_count += 1
                except Exception as e:
                    # log error
                    ebdUpdateErrors(
                        msg = f"MongoDB update error: {e}",
                        fd = curr_checklist,
                        ac = curr_ac_record,
                        mdb_code = mdb_code
                    )
                    print("MongoDB update error", nl, e)
                    pass
                
                # add new observations to Atlas Cache, if needed
                if mdb_code["insert_code"]["ind"]:
                    # insert new observations
                    try:
                        ebd.update_one(
                            {u"_id" : checklist_id},
                            mdb_code["insert_code"]["set_code"],
                            array_filters=mdb_code["insert_code"]["array_filter_code"],
                            upsert = True
                        )
                        checklist_updated_count += 1
                    except Exception as e:
                        # log error
                        ebdUpdateErrors(
                            msg = f"MongoDB update new obs error: {e}",
                            fd = curr_checklist,
                            ac = curr_ac_record,
                            mdb_code = mdb_code
                        )
                        print("MongoDB update error", nl, e)
                        pass
            else:
                # update date prior to last database update, do nothing
                pass

        else:
            # checklist is new
            # inset new checklist
            # print("- insert new checklist -", curr_checklist["SAMPLING_EVENT_IDENTIFIER"])
            mdb_code_insert_set = get_mongodb_insert_code(curr_checklist)
            try:
                ebd.update_one(
                    {u"_id" : checklist_id},
                    mdb_code_insert_set,
                    upsert = True
                )
                checklist_inserted_count += 1
            except Exception as e:
                # print("error:", e)
                # log error
                ebdUpdateErrors(
                    msg = f"MongoDB insert new check error: {e}",
                    fd = curr_checklist,
                    ac = curr_ac_record,
                    mdb_code = mdb_code
                )
                print("MongoDB update error", nl, e)
                pass

        checklist_count += 1
        if checklist_count % notify_frequency == 0:
            nowt = time.perf_counter()
            elapsed_time = nowt - start
            secs_per_check = elapsed_time/checklist_count
            est_total_sec = secs_per_check * checklists_to_import
            est_hrs_remaining = round(
                (
                    (est_total_sec - elapsed_time)/60
                )/60, 1
            )
            est_end_time = start_dt + timedelta(
                seconds = est_total_sec
            )
            elapsed_time_str = str(
                format_number_with_commas(
                    round(elapsed_time, 1)
                )
            ) + "s"

            print(
                nl, "++++++++++++++++++++", nl,
                "elapsed time:", elapsed_time_str, nl,
                "loop time:", str(round(nowt - loop_time, 1))+"s",nl,
                "processed",
                format_number_with_commas(checklist_count),
                "checklists", nl,
                "checklists remaining:", 
                format_number_with_commas(checklists_to_import - checklist_count), nl,
                "est hrs remaining:", est_hrs_remaining, nl,
                "est end time:", str(est_end_time), nl,
                "updated:",
                format_number_with_commas(checklist_updated_count),nl,
                "inserted:",
                format_number_with_commas(checklist_inserted_count)
            )
            loop_time = nowt

    # log stats from completion
    ebdUpdateStatus(
        "Weekly Update Stats",
        check_actions
    )

    # update db_status collection with new document, update summary document
    dbs.insert_one(
        {
            u"_id" : update_dates["update_run_dt"],
            "MOST_RECENT_EBD_DATE" : update_dates["current_update_dt"],
            "MOST_RECENT_EBD_DATE_TEXT" : update_dates["current_update_dt_txt"],
            "RUN_DATE" : update_dates["update_run_dt"],
            "NCBA_EBD_VER" : file_version,
            "UPDATE_TYPE" : "HIDDEN"
        }
    )

    # dbs.update_one(
    #     {u"_id" : "summary"},
    #     {
    #         "$set" : {
    #             "MOST_RECENT_EBD_DATE" : update_dates["current_update_dt"],
    #             "MOST_RECENT_EBD_DATE_TEXT": update_dates["current_update_dt_txt"],
    #             "NCBA_EBD_VER" : file_version
    #         }
    #     }
    # )

    print("Upload complete!")

    # close the connection
    client.close()

if __name__ == "__main__":
    main()
