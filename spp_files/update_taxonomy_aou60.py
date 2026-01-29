#############################################################
## SUITE OF VARIABLES TO LOAD CONSERVATION STATUS OR TAXONOMY

## AOU 60

# field to match to source file
match_id_field = "SCI_NAME"

# source id use to compare to match_id_field
source_id_field = "AC_ID"


# filename
source_fn = "20216015_bird_cons_status.csv"

# key to subdict with version data
source_key = "AOU"

# version - will be key for entry in key
source_version = "60"
source_date = "2020-01-01"
# map source fields to common fields
# For Species Lists:
# ID, RANK (order of species), COMMMON, SCIENTIFIC, ORDER, FAMILY, SUBFAMILY,
# SPEC4, SPEC6
source_info = {
    "FULL_NAME" : "American Ornithological Society",
    "URL" : "https://americanornithology.org/publications/north-and-middle-american-checklist/"
}
# For Conservation Designations (in addition to above):
# 


source_fields = {
    "AOU60_id" : "ID",
    "AOU60_rank": "RANK",
    "aou60_common_name": "COMMON",
    "AOU60_species" : "SCIENTIFIC",
    "AOU60_order": "ORDER",
    "AOU60_family" : "FAMILY",
    "AOU60_subfamily" : "SUBFAMILY",
    "AOU60_genus" : "GENUS",
    "AOU60_SPEC4" : "SPEC4",
    "AOU60_SPEC6" : "SPEC6"
}
source_field_data_type = {
    "AOU60_id" : "string",
    "AOU60_rank": "string",
    "aou60_common_name": "string",
    "AOU60_species" : "string",
    "AOU60_order": "string",
    "AOU60_family" : "string",
    "AOU60_subfamily" : "string",
    "AOU60_genus" : "string",
    "AOU60_SPEC4" : "string",
    "AOU60_SPEC6" : "SPEC6"
}