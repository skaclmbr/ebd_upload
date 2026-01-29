#############################################################
## SUITE OF VARIABLES TO LOAD CONSERVATION STATUS OR TAXONOMY

## AOU 61

# field to match to source file
match_id_field = "SCI_NAME"

# source id use to compare to match_id_field
source_id_field = "AC_ID"


# filename
source_fn = "20216015_bird_cons_status.csv"

# key to subdict with version data
source_key = "AOU"

# version - will be key for entry in key
source_version = "61"
source_date = "2021-01-04"
# map source fields to common fields
# For Species Lists:
# ID, RANK (order of species), COMMMON, SCIENTIFIC, ORDER, FAMILY, SUBFAMILY,
# SPEC4, SPEC6

# For Conservation Designations (in addition to above):
# 


source_fields = {
    "AOU61_id" : "ID",
    "AOU61_common" : "COMMON",
    "AOU61_species" : "SCIENTIFIC"
}
source_field_data_type = {
    "AOU61_id" : "string",
    "AOU61_common" : "string",
    "AOU61_species" : "string"
}