#############################################################
## SUITE OF VARIABLES TO LOAD CONSERVATION STATUS OR TAXONOMY

## AOU 60

# field to match to source file
match_id_field = "SCI_NAME"

# source id use to compare to match_id_field
source_id_field = "AC_ID"


# filename
source_fn = "CFR50-Part10.13-2023.csv"

# key to subdict with version data
source_key = "USFWS"

# version - will be key for entry in key
source_version = "2023"
source_date = "2023-01-01"

source_info = {
    "FULL_NAME" : "US Fish and Wildlife Service",
    "URL" : "https://www.fws.gov/"
}

# map source fields to common fields
# For Species Lists:
# ID, RANK (order of species), COMMMON, SCIENTIFIC, ORDER, FAMILY, SUBFAMILY,
# SPEC4, SPEC6

# For Conservation Designations (in addition to above):
# 


source_fields = {
    "TAXONOMIC_ORDER2" : "ID",
    "TAXONOMIC_ORDER" : "ORDER",
    "TAXONOMIC_FAMILY" : "FAMILY",
    "TAXONOMIC_GENUS" : "GENUS",
    "SCIENTIFIC_NAME" : "SCIENTIFIC",
    "ENGLISH_NAME" : "COMMON",
    "MBTA" : "MBTA",
    "BCC" : "BCC",
    "FedStatus": "STATUS"
}
source_field_data_type = {
    "TAXONOMIC_ORDER2" : "ID",
    "TAXONOMIC_ORDER" : "ORDER",
    "TAXONOMIC_FAMILY" : "FAMILY",
    "TAXONOMIC_GENUS" : "GENUS",
    "SCIENTIFIC_NAME" : "SCIENTIFIC",
    "ENGLISH_NAME" : "COMMON",
    "MBTA" : True,
    "BCC" : True,
    "FedStatus": "STATUS"
}