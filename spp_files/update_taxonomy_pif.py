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
source_key = "PIF"

# version - will be key for entry in key
source_version = "2020"
source_date = "2020-01-01"

source_info = {
    "FULL_NAME" : "Partners In Flight Avian Conservation and Assessment Database",
    "URL" : "https://pif.birdconservancy.org/avian-conservation-assessment-database/"
}
# map source fields to common fields
# For Species Lists:
# ID, RANK (order of species), COMMMON, SCIENTIFIC, ORDER, FAMILY, SUBFAMILY,
# SPEC4, SPEC6

# For Conservation Designations (in addition to above):
# 


source_fields = {
    "PIF_half_life" : "PIF_HALF_LIFE",
    "PIF_pop_est" : "PIF_POP_EST"
}
source_field_data_type = {
    "PIF_half_life" : 100,
    "PIF_pop_est" : 1000000
}