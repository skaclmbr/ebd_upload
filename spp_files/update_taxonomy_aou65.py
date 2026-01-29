#############################################################
## SUITE OF VARIABLES TO LOAD CONSERVATION STATUS OR TAXONOMY

## AOU 60

# field to match to source file
match_id_field = "SCI_NAME"

# source id use to compare to match_id_field
source_id_field = "AC_ID"


# filename
source_fn = "aou65.csv"

# key to subdict with version data
source_key = "AOU"

# version - will be key for entry in key
source_version = "65"
source_date = "2024-01-01"
# map source fields to common fields
# For Species Lists:
# ID, RANK (order of species), COMMMON, SCIENTIFIC, ORDER, FAMILY, SUBFAMILY,
# SPEC4, SPEC6
source_info = {
    "FULL_NAME" : "American Ornithological Society",
    "URL" : "https://checklist.americanornithology.org/"
}
# For Conservation Designations (in addition to above):
# 


source_fields = {
    "id" : "ID",
    "rank": "RANK",
    "common_name": "COMMON",
    "species" : "SCIENTIFIC",
    "order": "ORDER",
    "family" : "FAMILY",
    "subfamily" : "SUBFAMILY",
    "genus" : "GENUS",
}
source_field_data_type = {
    "id" : "string",
    "rank": "string",
    "common_name": "string",
    "species" : "string",
    "order": "string",
    "family" : "string",
    "subfamily" : "string",
    "genus" : "string",
}