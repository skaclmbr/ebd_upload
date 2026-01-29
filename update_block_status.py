
# Uploads Winter and Breeding Completion status for each block
# requires csv file from BLOCK_SUMMARIES Excel file
# Created 9/18/25
# Scott K. Anderson

from pymongo.mongo_client import MongoClient
import certifi
import csv
from mdbconn import connString

nl = "\n"
fmt_dt = "%Y-%m-%d"
max_timeout = 100000000
start_block = "" # change this if restarting after partial run

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

# PRODUCTION
bsum = db.BLOCK_SUMMARIES
# bsum = db.bs_test
# END PRODUCTION


# LOAD CSV file
with open("breed_winter_status.csv", "r", encoding = "utf-8-sig") as f:
    reader = csv.reader(f)
    row_count = 1
    for row in reader:
        if row_count == 1:
            # header row
            h = row
        else: # all other rows
            row_data = dict(zip(h,row))
            update_json = {
                "BREEDING_COMPLETE" : int(row_data["BREEDING_COMPLETE"]),
                "WINTERING_COMPLETE" : int(row_data["WINTERING_COMPLETE"]),
            }
            print(
                "Updating", row_data["ID_NCBA_BLOCK"],nl
            )

            response = bsum.update_one(
                {"ID_BLOCK_CODE" : row_data["ID_BLOCK_CODE"]},
                {"$set" : update_json}
            )

        row_count += 1

    print(
        " ===", nl,
        "Updated", str(row_count - 2), "block records", nl,
        "==="
    )