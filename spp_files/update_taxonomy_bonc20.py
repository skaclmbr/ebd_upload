#############################################################
## SUITE OF VARIABLES TO LOAD CONSERVATION STATUS OR TAXONOMY

## Birds of North Carolina

# field to match to source file
match_id_field = "SCI_NAME"

# source id use to compare to match_id_field
source_id_field = "AC_ID"


# filename
source_fn = "20216015_bird_cons_status.csv"

# key to subdict with version data
source_key = "BirdsOfNC"

# version - will be key for entry in key
source_version = "20"
source_date = "2020-01-01"

source_info = {
    "FULL_NAME" : "Birds of North Carolina",
    "URL" : "https://ncbirds.carolinabirdclub.org/"
}
# map source fields to common fields
# For Species Lists:
# ID, RANK (order of species), COMMMON, SCIENTIFIC, ORDER, FAMILY, SUBFAMILY,
# SPEC4, SPEC6

# For Conservation Designations (in addition to above):
# 

source_fields = {
    "BoNC_ID" : "ID",
    "BoNC_Common": "COMMON",
    "BONC20_scientific" : "SCIENTIFIC",
    "NC_Species" : "NC_SPECIES",
    # "Breeding" : "NC_BREEDING",
    # "Wintering" : "NC_WINTERING"
}
source_fields_data_type = {
    "BoNC_ID" : "string",
    "BoNC_Common": "string",
    "BONC20_scientific" : "string",
    "NC_Species" : True,
    # "Breeding" : True,
    # "Wintering" : True
}