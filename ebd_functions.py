# Atlas-related functions
import csv
from pymongo.mongo_client import MongoClient
import certifi
from mdbconn import connString

nl = "\n"
fmt_dt = "%Y-%m-%d"
staff_fn = "ebird_staffids.csv"

work_year_seasons = [
    "breeding2021",
    "wintering2021",
    "breeding2022",
    "wintering2022",
    "breeding2023",
    "wintering2023",
    "breeding2024",
    "wintering2024",
    "breeding2025",
    "wintering2025"
]

bcode_bcat = {
    "F" : "C1",
    "H" : "C2",
    "S" : "C2",
    "A" : "C3",
    "B" : "C3",
    "C" : "C3",
    "M" : "C3",
    "N" : "C3",
    "P" : "C3",
    "S7" : "C3",
    "T" : "C3",
    "CF" : "C4",
    "CN" : "C4",
    "DD" : "C4",
    "FL" : "C4",
    "FS" : "C4",
    "FY" : "C4",
    "NB" : "C4",
    "NE" : "C4",
    "NY" : "C4",
    "ON" : "C4",
    "PE" : "C4",
    "UN" : "C4"
}


#############################################################################
## code to determine if a staff member worked in a given time period
# load staff_ids file into json for lookup
staff = {}
with (open(staff_fn, "r", encoding = "utf-8-sig") as file):
    reader = csv.reader(file)
    h = []
    for row in reader:
        if not h:
            # header row
            h = row
        else: # all other rows
            rowdata = dict(zip(h, row))
            if rowdata["ObserverID"].strip() != "":
                staff[rowdata["ObserverID"].strip()] = rowdata


def id_observer(obsid, season, year):
    #pass obsid and time period, return "volunteer" or name of staff
    result = "volunteer"
    if season != "interim":
        tp = "".join([season, str(year)])
        try:
            if obsid in staff.keys():
                if staff[obsid][tp] == "x":
                    result = staff[obsid]["full_name"]
        except:
            pass

    return result

#############################################################################
## code to determine species information

## Get subset of ebd_taxonomy for species data

client = MongoClient(connString(), tlsCAFile=certifi.where())

db = client.ebd_mgmt
tax = db.ebd_taxonomy

agg = [
    {
        "$project": {
            "_id": 0,
            "PRIMARY_COM_NAME": 1,
            "SCI_NAME": 1,
            "CATEGORY": 1,
            "SPEC4": 1,
            "SGCN" : "$WAP.latest.SGCN",
            "BCC" : "$USFWS.latest.BCC",
            "MBTA" : "$USFWS.latest.MBTA",
            # "PIF_HALF_LIFE" : "$PIF.latest.PIF_HALF_LIFE",
            "AUDUBON_PRIORITY" : "$AUDUBON.latest.PRIORITY",
            "BONC_NC" : "$BONC.latest.NC_SPECIES",

        }
    }
]

taxonomy = tax.aggregate(agg)
spp = {}

# loop through records, populate dictionary with species information
for row in taxonomy:
    # print(json.dumps(row))
    spp[row["PRIMARY_COM_NAME"]] = row

taxonomy.close()

# function to lookup results
def get_spp_info(spp_name):
    # pass common name, return dictionary of species information
    result = {}
    if spp_name in spp.keys():
        result = spp[spp_name]

    return result