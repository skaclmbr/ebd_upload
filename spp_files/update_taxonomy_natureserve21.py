#############################################################
## SUITE OF VARIABLES TO LOAD CONSERVATION STATUS OR TAXONOMY

## Natureserve

# field to match to source file
match_id_field = "SCI_NAME"

# source id use to compare to match_id_field
source_id_field = "AC_ID"


# filename
source_fn = "20216015_bird_cons_status.csv"

# key to subdict with version data
source_key = "NatureServe"

# version - will be key for entry in key
source_version = "2021"
source_date = "2021-01-01"

source_info = {
    "FULL_NAME" : "NatureServe",
    "URL" : "https://explorer.natureserve.org/"
}

# map source fields to common fields
# For Species Lists:
# ID, RANK (order of species), COMMMON, SCIENTIFIC, ORDER, FAMILY, SUBFAMILY,
# SPEC4, SPEC6

# For Conservation Designations (in addition to above):
# 


source_fields = {
    "NatureServe_Unique_ID" : "ID",
    "NS_GLOBAL": "GLOBAL_STATUS",
    "NS_STATE": "NC_STATUS",
}
source_field_data_type = {
    "NatureServe_Unique_ID" : "string",
    "NS_GLOBAL": "string",
    "NS_STATE": "string",
}