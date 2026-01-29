## Update block survey year for data

from pymongo import MongoClient
import certifi
import csv
from mdbconn import connString

nl = "\n"

#####################################################################
## Connect to Mongo


client = MongoClient(connString(), tlsCAFile=certifi.where())

db = client.ebd_mgmt
blocks = db.blocks


def main():
    query_list = []
    with open("block_priority.csv", "r", encoding = "utf-8-sig") as f:
        csvFile = csv.reader(f)
        count = 1
        for line in csvFile:
            if count == 1:
                pass
            else:
                year = line[3]
                if year == 0: year = "NONE"
                currId = line[1]
                q = {"ID_BLOCK_CODE" : currId}
                u = {"$set" : {"NCBA_SURVEY_YEAR" : year}}
                blocks.update_one(
                    q,
                    u,
                    upsert = False
                )
                print(
                    line[0],
                    "updated",
                    " - ",
                    count,
                    "blocks",
                    nl
                )
            count += 1


if __name__ == "__main__":
    main()