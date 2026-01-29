# Update the ebd_taxonomy collection

import csv
from pymongo.mongo_client import MongoClient
import certifi
from ebd_functions import spp, get_spp_info
import json
from mdbconn import connString

nl = "\n"
fmt_dt = "%Y-%m-%d"


#####################################################################
## Connect to Mongo


client = MongoClient(connString(), tlsCAFile=certifi.where())

db = client.ebd_mgmt
ebd = db.ebd

def main():

    count = 1
    for d in spp.values():
        if "SGCN" not in d.keys():
            sgcn = 0
        else:
            sgcn = d["SGCN"]
        
        if "AUDUBON_PRIORITY" not in d.keys():
            audubon = 0
        else:
            audubon = d["AUDUBON_PRIORITY"]

        if "MBTA" not in d.keys():
            mbta = 0
        else:
            mbta = d["MBTA"]

        if "KNOWLEDGE_GAP" not in d.keys():
            kg = 0
        else:
            kg = d["KNOWLEDGE_GAP"]

        q = {
            "OBSERVATIONS.SCIENTIFIC_NAME" : d["SCI_NAME"],
        }

        set_dict = {
                "$set" : {
                    "OBSERVATIONS.$[element].SGCN" : sgcn,
                    "OBSERVATIONS.$[element].AUDUBON_PRIORITY" : audubon,
                    "OBSERVATIONS.$[element].MBTA" : mbta,
                    "OBSERVATIONS.$[element].KNOWLEDGE_GAP" : kg
                }
            }
        array_dict = [
                    {"element.SCIENTIFIC_NAME" : d["SCI_NAME"]}
                ]

        # Execute the update and capture the result
        result = ebd.update_many(
            q,
            set_dict,
            upsert= False,
            array_filters = array_dict
            )

        # Print the update results
        print(f"Updated records for {d['PRIMARY_COM_NAME']}:")
        print(f"  Matched documents: {result.matched_count}")
        print(f"  Modified documents: {result.modified_count}")
        print(nl)

        count += 1

if __name__ == "__main__":
    main()