#############################################################
## SUITE OF VARIABLES TO LOAD CONSERVATION STATUS OR TAXONOMY

## Natureserve

# field to match to source file
match_id_field = "SCI_NAME"

# source id use to compare to match_id_field
source_id_field = "AC_ID"


# filename
source_fn = "itis.csv"

# key to subdict with version data
source_key = "ITIS"

# version - will be key for entry in key
source_version = "2024"
source_date = "2024-12-16"

source_info = {
    "FULL_NAME" : "Integrated Taxonomic Information System",
    "URL" : "https://itis.gov/downloads/index.html"
}

# map source fields to common fields
# For Species Lists:
# ID, RANK (order of species), COMMMON, SCIENTIFIC, ORDER, FAMILY, SUBFAMILY,
# SPEC4, SPEC6

# For Conservation Designations (in addition to above):
# 


source_fields = {
    "tsn" : "ID",
    "parent_tsn": "PARENT_ID",
    "common": "COMMON",
    "name1" : "GENUS",
    "name2" : "SPECIES",
    "complete_name" : "SCIENTIFIC",
    "rank" : "RANK"
}
source_field_data_type = {
    "tsn" : "ID",
    "parent_tsn": "PARENT_ID",
    "common": "COMMON",
    "name1" : "GENUS",
    "name2" : "SPECIES",
    "complete_name" : "SCIENTIFIC",
    "rank" : "RANK"
}