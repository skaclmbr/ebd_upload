


import os
import json
import csv
from pymongo.mongo_client import MongoClient
import certifi
import copy
# import geopandas as gpd
# from shapely.geometry import Point, Polygon
import datetime
from mdbconn import connString

nl = "\n"
fmt_dt = "%Y-%m-%d"
out_delim = ","

out_headers = [
    "ID_NCBA_BLOCK",
    "COMMON_NAME",
    "COUNTY",
    "ECOREGION"
]
out_sppfields = [
    "SpeciesName",
    "SpeciesType",
    "Phenology",
    "BreedAbundance",
    "MigAbundance",
    "WinterAbundance",
    "YearAbundance",
    "WeeksDetected"
]
####################################################################
## Connect to Mongo

client = MongoClient(connString(), tlsCAFile=certifi.where())

## Get Block data
db = client.ebd_mgmt
ebd = db.ebd
blocks = db.BLOCK_SUMMARIES
dbs = db.db_status
err = db.ebd_upload_errlog

with open("spplist.json", "r", encoding = "utf-8") as file:
    sl_in = json.load(file)

# convert county names to upper
spplist = {}
for k, v in sl_in.items():
    spplist[k.upper()] = sl_in[k]

## Retrieve priority block data
query = {}
filter = {
    "ID_NCBA_BLOCK" : 1,
    "ID_BLOCK_CODE" : 1,
    "STATUS" : 1,
    "county" : 1,
    "region" : 1
}

# block_data = blocks.find(query, filter).limit(100) # TESTING
block_data = blocks.find(query, filter)
# returns list of json data for each block

with open(
    "20241112_unique_spp_block_lists.csv",
    "w",
    encoding = "utf-8",
    newline="") as file:

    writer = csv.writer(file)
    out_omit = [
        "_id",
        "ebird_county_data"
    ]
    bcount = 1
    county_not_found = 0
    out_row_headers = []
    for b in block_data:
        out_row_block = []
        print(b["ID_NCBA_BLOCK"] + nl)
        # loop through data, build out_row, headers
        for k, v in b.items():
            if k not in out_omit:
                out_row_block.append(v)

        if bcount == 1:
            for k, v in b.items():
                if k not in out_omit:
                    out_row_headers.append(k)
            writer.writerow(out_row_headers + out_sppfields)

        # get species data
        if b["county"] != "":
            for s in spplist[b["county"]]:
                # print(json.dumps(s))
                out_row_spp = []
                for f in s.keys():
                    if f in out_sppfields:
                        out_row_spp.append(s[f])
                
                writer.writerow(out_row_block + out_row_spp)
        else:
            county_not_found += 1
            print(
                str(county_not_found), "blocks with blank counties"
            )

        # except:
        #     county_not_found += 1
        #     print(
        #         "===",
        #         nl,
        #         b["county"].title(),
        #         "not found",
        #         nl,
        #         str(county_not_found), "total", nl,
        #         "===",
        #         nl)


        bcount += 1
        # if bcount > 1: break

print (
    str(county_not_found), "blocks with blank counties"
)