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
source_key = "WAP"

# version - will be key for entry in key
source_version = "2015"
source_date = "2015-09-01"
# map source fields to common fields
# For Species Lists:
# ID, RANK (order of species), COMMMON, SCIENTIFIC, ORDER, FAMILY, SUBFAMILY,
# SPEC4, SPEC6

source_info = {
    "FULL_NAME" : "NC Wildlife Resources Commission",
    "URL" : "https://ncwildlife.org/"
}

# For Conservation Designations (in addition to above):
# 


source_fields = {
    "SGCN" : "SGCN",
    "WAP_Eval": "EVALUATED",
    "WAP_Know" : "KNOWLEDGE_GAP",
    "WAP_Mgmt" : "MANAGEMENT",
    "WAP15_ID" : "ID"
}
source_field_data_type = {
    "SGCN" : True,
    "WAP_Eval": True,
    "WAP_Know" : True,
    "WAP_Mgmt" : True,
    "WAP15_ID" : "string"
}