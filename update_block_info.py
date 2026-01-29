# # Loops through mongodb records with
# # NCBA_UPDATE_BLOCK = "1"
# # and updates the Block information based on coords


# from datetime import datetime, timedelta
# from dateutil import parser
# import time
import os
from pymongo.mongo_client import MongoClient
import mdbconn #stores database connection information
import certifi
import json
import geopandas as gpd
from shapely.geometry import Point, Polygon
from mdbconn import connString

nl = "\n"
sjdict = {"OBSERVATION_ID": [], "geometry": []}

## SETUP CONNECTION TO MONGODB

client = MongoClient(connString(), tlsCAFile=certifi.where())

db = client.ebd_mgmt
# FOR PRODUCTION
ebd = db.ebd
blocks = db.blocks

# FOR TESTING
# ebd = db.ebd_test
# ebd = db.ebd_f_test


def main():

    #####################################################################
    ## LOOP THROUGH EBD AND ASSEMBLE DATA
    # Get EBD data
    q = {
        # "NCBA_UPDATE_BLOCK" : "1"
        "$or":[
            {"ID_NCBA_BLOCK" : {"$exists": 0}},
            {"ID_NCBA_BLOCK" : ""}
        ]
    }

    p = {
        "LATITUDE" : 1,
        "LONGITUDE" : 1
    }
    cursor = ebd.find( q, p) # PRODUCTION
    # cursor = ebd.find( q, p).limit(100) # TESTING

    #loop through cursor, build sjdict
    ac_record_list = list(cursor)


    print(str(len(ac_record_list)), "records")
    for i in ac_record_list: 
        sjdict["OBSERVATION_ID"].append(i["_id"])
        sjdict["geometry"].append(
            Point(
                float(i["LONGITUDE"]),
                float(i["LATITUDE"])
                )
        )
    # loop through blocks, build sjblocks
    qblocks = {}
    coord_fields = {
        "NW_X" : 1,
        "NW_Y" : 1,
        "SE_X" : 1,
        "SE_Y" : 1
    }
    pblocks = {
        "ID_NCBA_BLOCK" : 1,
        "ID_BLOCK_CODE" : 1,
        "ID_EBD_NAME" : 1,
        "PRIORITY" : 1,
    }
    pblocks.update(coord_fields)
    cursor = blocks.find(qblocks, pblocks)
    ac_blocks_list = list(cursor)
    
    #####################################################################
    ## LOOP THROUGH BLOCKS AND ASSEMBLE DATA
    blocks_dict = {
            "ID_NCBA_BLOCK" : [],
            "geometry" : []
        }
    blocks_data = {}
    for b in ac_blocks_list:
        #create sj dict AND reference dict for properties
        block_key = b["ID_NCBA_BLOCK"]
        
        blocks_dict["ID_NCBA_BLOCK"].append(block_key)
        # add coord fields
        blocks_dict["geometry"].append(
            Polygon(
            (
                (
                    float(b["NW_X"]),
                    float(b["NW_Y"])
                ),
                (
                    float(b["NW_X"]),
                    float(b["SE_Y"])
                ),
                (
                    float(b["SE_X"]),
                    float(b["SE_Y"])
                ),
                (
                    float(b["SE_X"]),
                    float(b["NW_Y"])
                ),
                (
                    float(b["NW_X"]),
                    float(b["NW_Y"])
                )
            )
            )
        )
        #populate properties
        blocks_data[block_key] = {}
        for f in b.keys():
            if f not in coord_fields:
                blocks_data[block_key][f] = b[f]

    #####################################################################
    ## PERFORM SPATIAL JOIN
    # do spatial join to find blocks for each checklist
    sjpnts = gpd.GeoDataFrame( sjdict, crs = 'EPSG:4326')
    sjblocks = gpd.GeoDataFrame(blocks_dict, crs = 'EPSG:4326')
    sjresult = gpd.sjoin(
        sjpnts,
        sjblocks,
        how = 'left',
        predicate = 'within')

    #####################################################################
    ## LOOP THROUGH SPATIAL JOIN RESULTS, COMPILE FOR MONGO UPDATE
    block_list_out = {}
    sj_count = 0
    for k , row in sjresult.iterrows():
        try:
            block_key = row["ID_NCBA_BLOCK"]

            SID = row["OBSERVATION_ID"]
            block_data = blocks_data[block_key]
            if block_key not in block_list_out.keys():
                block_list_out[block_key] = {
                    "SEI" : [],
                    "UPDATE_CODE" : {
                        "ID_NCBA_BLOCK" : block_data["ID_NCBA_BLOCK"],
                        "ID_BLOCK_CODE" : block_data["ID_BLOCK_CODE"],
                        "NCBA_BLOCK" : block_data["ID_EBD_NAME"],
                        "PRIORITY_BLOCK" : block_data["PRIORITY"],
                        "NCBA_UPDATE_BLOCK" : "0" #mark record as updated
                    }
                }

            block_list_out[block_key]["SEI"].append(SID)
        except:
            # block not found (mostly pelagic trips)
            # skip update to mongo
            pass

        sj_count += 1

        sj_break = sj_count % 1000
        if sj_break == 0:
            print(
                nl,
                "== LOOPING SPATIAL JOIN RESULTS ==",
                nl,
                str(sj_count), "records processed."
            )

    #####################################################################
    ## UPDATE ATLAS CACHE, ONE QUERY PER BLOCK
    # loop through blocks and update each block
    for b in block_list_out.keys():
        ebd.update_many(
            {u"_id" : {"$in" : block_list_out[b]["SEI"]}},
            {"$set": block_list_out[b]["UPDATE_CODE"]}
        )

if __name__ == "__main__":
    main();