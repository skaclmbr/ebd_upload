# Update ebd_taxonomy table
# 12/19/24
# Scott K. Anderson


import os
import json
from pymongo.mongo_client import MongoClient
import certifi
import copy
import csv
from datetime import datetime
from pathlib import Path
from mdbconn import connString

# import geopandas as gpd
# from shapely.geometry import Point, Polygon
import datetime

#####################################################################
## LOAD UPDATE INFORMATION
## external file sets variables that determine how to match and
## process species information


# import update_taxonomy_aou60 as xd
# import update_taxonomy_aou65 as xd
# import update_taxonomy_avibase as xd
# import update_taxonomy_pif as xd
# import update_taxonomy_aou61 as xd
# import update_taxonomy_nc as xd
# import update_taxonomy_bonc20 as xd
# import update_taxonomy_wap15 as xd
# import update_taxonomy_natureserve21 as xd
# import update_taxonomy_audubon as xd
# import update_taxonomy_r2r as xd
# import update_taxonomy_usfws20 as xd
# import update_taxonomy_usfws23 as xd
import update_taxonomy_nccounties as xd
# import update_taxonomy_itis as xd
# import update_taxonomy_ebird as xd



#####################################################################
## Connect to Mongo

client = MongoClient(connString(), tlsCAFile=certifi.where())

db = client.ebd_mgmt
err_log = db.ebd_taxonomy_missing

# PRODUCTION
tax = db.ebd_taxonomy
# END PRODUCTION

#########
# TESTING
# tax = db.ebd_taxonomy_test
# END TESTING
#############


#####################################################################
## local files
err = open("err.csv", "w", encoding = "utf-8")
# test = open("test.json", "w", encoding = "utf-8")
# xwalk_csv = open("xwalk.csv", "w", encoding = "utf-8")
nl = "\n"
fmt_dt = "%Y-%m-%d"
xwalk = {}
source_compiled_fields_keys = {}
source_spp_list = set()
miss_spp = {}
miss_ac_spp = {}

if xd.source_info:
    source_citation = xd.source_info
else:
    source_citation = {}

if xd.source_compiled_fields:
    compiled_fields_present = True
else:
    compiled_fields_present = False

#####################################################################
## FUNCTIONS

def log_err(id, e, v):
    err.write(",".join([id, e, v ])+ nl)

def load_source():
    # load source csv file into the xwalk dict
    # source file intended to have one row per species

    # check if compiled fields present
    # check to see if compiled fields present, get unique key values
    if compiled_fields_present:
        for k in xd.source_compiled_fields: source_compiled_fields_keys[k] = {}

    fp = Path(__file__).parent / "spp_files" / xd.source_fn
    with open(fp, "r", encoding = "utf-8-sig") as f:
        csvFile = csv.reader(f)
        count = 1
        headings = {}
        for line in csvFile:
            if count == 1:
                id_field_index = line.index(xd.source_id_field)
                headings[xd.source_id_field] = id_field_index
                ind = 0
                for i in line:
                    if i in xd.source_fields.keys():
                        headings[i] = ind
                    ind += 1
            else:
                # source file intended to have one row per species
                currId = line[id_field_index]
                source_spp_list.add(currId)
                if currId not in xwalk.keys():
                    xwalk[currId] = {}

                for v, i in headings.items():
                    if xd.source_fields[v] != "":
                        xwalk[currId][v] = line[i]

                # check if compiled fields present
                if compiled_fields_present:
                    for k, d in xd.source_compiled_fields.items():
                        if k not in xwalk[currId]:
                            xwalk[currId][k] = {}
                        
                        xwalk[currId][k][line[headings[d[0]]]] = \
                            line[headings[d[1]]]

            count += 1

    print(
        "Source File species loaded", nl,
        count, "rows found", nl,
        len(source_spp_list), "species found", nl
    )

def date_fmt(d):
    return datetime.datetime.strptime(d, "%Y-%m-%d").date()

def is_latest(ac_dict, source_date):
    result = False
    # # print(
    # #     "is_latest:", nl,
    # #     "ac_dict:", nl,
    # #     json.dumps(ac_dict),nl,
    # #     "source_date:", source_date
    # # )
    ac_dict.pop(xd.source_version)
    latest = ac_dict.pop("latest")
    result = (latest["VERSION"] == xd.source_version)
    if not result:
        for k, val in ac_dict.items():
            # print(
            #     "is_latest:", nl,
            #     k, nl,
            #     json.dumps(val), nl,
            #     date_fmt(source_date), nl,
            #     date_fmt(val["DATE"])
            # )

            if date_fmt(source_date) > date_fmt(val["DATE"]):
                # print("result true")
                result = True
                break

    return result

def convert_data_type (f, v):

    v = v.replace("0","").strip()

    try:
        dt = type(xd.source_field_data_type[f])
        if dt == str:
            result = str(v)
        elif dt == bool:
            if v.capitalize():
                result = 1
            else:
                result = 0
        elif dt == int:
            result = int(v)
        elif dt == float:
            result = float(v)

    except:
        result = v


    return result


#####################################################################
## MAIN FUNCTION
def main():
    # download current list of ids from atlas cache
    q = {}
    p = {
        "PRIMARY_COM_NAME" : 1,
        "SCI_NAME" : 1,
        "CATEGORY" : 1
    }

    # add match field from source file if not present
    if xd.match_id_field not in p.keys():
        p[xd.match_id_field] = 1
    
    if xd.source_key not in p.keys():
        p[xd.source_key] = 1

    cursor = tax.find(q,p)
    # cursor = tax.find(q,p).limit(5) ## TESTING
    mdb_spp = list(cursor)

    print(
        "Atlas Cache species downloaded", nl,
        len(mdb_spp), "found", nl
    )
    
    # load the source file into the xwalk dict
    load_source()
    source_spp_list = list(xwalk.keys())

    nonblank_source_fields = {}
    for k, v in xd.source_fields.items():
        if v != "": nonblank_source_fields[k] = v
    
    count_matched = 0
    for spp in mdb_spp:

        if spp[xd.match_id_field] in xwalk.keys():
            # ac records have a match wth crosswalk document
            matched_id = spp[xd.match_id_field]
            # print(
            #     spp["PRIMARY_COM_NAME"], "(",matched_id,")",
            #     "matched!",
            #     # # "spp data:", nl,
            #     # # json.dumps(spp)
            # )

            # check to see if source key is in Atlas Cache data
            if xd.source_key in spp.keys(): 
                source_key_present = True
            else:
                source_key_present = False

            # match found! load data
            # this will be the update code for mongodb
            set_dict = {
                xd.source_key : {
                    xd.source_version : {}
                }
            }

            # load source_key versions that do not match current version
            # there is likely a better way to do this!
            # running the $set command clears out all other versions otherwise!
            if source_key_present:
                for ver in spp[xd.source_key].keys():
                    if ver != xd.source_version:
                        set_dict[xd.source_key][ver] = spp[xd.source_key][ver]

            # set variables for current version
            set_dict[xd.source_key][xd.source_version] = {
                "DATE" : xd.source_date,
                "VERSION" : xd.source_version
            }
            
            # add source fields to the update query
            # for f in xd.source_fields:
            for f in nonblank_source_fields:
                set_dict[xd.source_key][xd.source_version][xd.source_fields[f]]\
                    = convert_data_type(f, xwalk[matched_id][f] )

            if compiled_fields_present:

                # add compiled fields
                for f in xd.source_compiled_fields:
                    set_dict[xd.source_key][xd.source_version][f] = \
                        xwalk[matched_id][f]


            # evaluate if newest
            # add latest designation
            new_latest = copy.deepcopy(set_dict[xd.source_key][xd.source_version])
            if source_key_present and xd.source_version in spp[xd.source_key].keys():
                    # # print(
                    # #     xd.source_key,
                    # #     "is in atlascache", nl,
                    # #     json.dumps(spp[xd.source_key]), nl,
                    # #     "source_version:", xd.source_version
                    # # )
                    if is_latest(spp[xd.source_key], xd.source_date):
                        # this record is not the latest, remove latest entry
                        set_dict[xd.source_key]["latest"] = new_latest
                        # del set_dict[xd.source_key]["latest"]
            else:
                #source key is new, by default current rec is th latest
                set_dict[xd.source_key]["latest"] = new_latest

            # remove from source species list
            source_spp_list.remove(spp[xd.match_id_field])
            # write to Atlas Cache
            # # print(
            # #     "set_dict:", nl,
            # #     json.dumps(set_dict)
            # # )

            try:
                tax.update_one(
                    {
                        xd.match_id_field : matched_id
                    },
                    {"$set": set_dict },
                    upsert = False
                )
            except:
                log_err(matched_id, Exception, json.dumps(set_dict))
                print(
                    "atlas cache record update failed.", nl,
                    repr(Exception)
                )
            count_matched += 1

        else:
            # ac species did not match source records
            miss_spp[spp["PRIMARY_COM_NAME"]] = {
                    "SPP_ID" : spp["_id"],
                    "SPP_SCI" : spp["SCI_NAME"]
                }
    if count_matched:
        #add citation info to source key entry
        tax.update_many(
            {
                xd.source_key : {"$exists": 1}
            },
            {
                "$set" : {
                    ".".join([xd.source_key, "citation"]) : source_citation
                }
            }
        )


    print(
        nl, "=================", nl,
        count_matched,
        "Species Matched!", nl,
        xd.source_key, nl,
        xd.source_version,
    )


    # update species missed to atlas cache
    if len(miss_spp):
        record = {
            "DATE" : datetime.datetime.now(),
            "SOURCE_KEY" : xd.source_key,
            "SOURCE_VERSION" : xd.source_version,
            "SOURCE_ID_FIELD" : xd.source_id_field,
            "MATCH_ID_FIELD" : xd.match_id_field,
            "TOTAL_MATCHED" : count_matched,
            "AC_SPP_LIST": miss_spp,
            "SOURCE_SPP_LIST" : source_spp_list
        }
        err_log.insert_one(record)

if __name__=="__main__":
    main()
