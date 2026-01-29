
# importing modules
from create_block_report_pdf import PDF
from pdf_to_google import upload_file_to_drive, delete_file_from_drive
import json

from pymongo.mongo_client import MongoClient
import certifi
import copy
import datetime
import time
from mdbconn import connString

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
# END PRODUCTION


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
blockcount = 1
for bs in block_data:
    block_id = bs["ID_NCBA_BLOCK"]
    print (
        nl, "=================================", nl,
        "retrieving", block_id, "data"
        )
    
    q = {
        "ID_NCBA_BLOCK" : block_id
    }
    # filter out the data not needed.
    f = {
        "ebird_web_data" : 0,
        "ebird_county_data" : 0,
    }

    bs = bsum.find_one(q,f)
    
    # delete old report
    try: 
        url = bs["REPORT_URL"]
        file_id = url.split("/")[-2]
        delete_file_from_drive(file_id)

    
        # create and upload report to google
        pdf = PDF(bs)
        file_name = f'{block_id}_Report.pdf'
        file_path = f'block_reports/{file_name}'
        pdf.output(file_path)

        file_url = upload_file_to_drive(file_path, file_name)

    except:
        print("report delete/update failed")

    # update atlas cache with the file_url
    try:
        bsum.update_one(
            {"ID_NCBA_BLOCK" : block_id},
            {
                "$set" : {
                    "REPORT_URL" : file_url
                }
            }
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
            "=================================" + 
            nl
            )

    except Exception as errmsg:
        print(
            block_id,
            "failed to update", nl,
            repr(errmsg)
        )
