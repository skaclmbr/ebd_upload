# populate the NCBA_OBSERVER field
# should be either "volunteer" or the name of NCBA staff/temp

import csv
from pymongo.mongo_client import MongoClient
import certifi
from ebd_functions import staff, work_year_seasons
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
    for d in staff.values():
    
        # gather working season data
        emp_work_ys = []
        emp_y = set()
        emp_s = set()

        # which season(s) did they work?
        for w in work_year_seasons:
            if d[w] == "x":
                emp_work_ys.append(w)
                emp_y.add(w[-4:])
                emp_s.add(w[:-4])


        # build query
        for y in emp_y:

            q = {
                "OBSERVER_ID" : d["ObserverID"],
                "YEAR" : int(y),
                "PROJECT_CODE" : "EBIRD_ATL_NC",
                "NCBA_OBSERVER" : "volunteer",
                "NCBA_SEASON" : {
                    "$in" : list(emp_s)
                }
            }

            set_dict = {
                "$set" : {
                    "NCBA_OBSERVER" : d["full_name"]
                }
            }

            # Execute the update and capture the result
            result = ebd.update_many(q, set_dict)

            # Print the update results
            print(f"Updated records for {d['full_name']} in year {y}:")
            print(f"  Matched documents: {result.matched_count}")
            print(f"  Modified documents: {result.modified_count}")
            print(nl)
            # if count < 5:
            #     print("ebd.update_many(q, set_dict)")
            #     print("q", q)
            #     print("set_dict", set_dict)
            #     print(nl)

        count += 1

if __name__ == "__main__":
    main()