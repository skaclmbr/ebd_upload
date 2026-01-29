#############################################################
## SUITE OF VARIABLES TO LOAD CONSERVATION STATUS OR TAXONOMY

## AOU 60

# field to match to source file
match_id_field = "SCI_NAME"

# source id use to compare to match_id_field
source_id_field = "AC_ID"


# filename
source_fn = "TippingPointSpecies_List_Updated_2024.csv"

# key to subdict with version data
source_key = "R2R"

# version - will be key for entry in key
source_version = "2024"
source_date = "2024-01-01"

source_info = {
    "FULL_NAME" : "Road to Recovery",
    "URL" : "https://r2rbirds.org/"
}
# map source fields to common fields
# For Species Lists:
# ID, RANK (order of species), COMMMON, SCIENTIFIC, ORDER, FAMILY, SUBFAMILY,
# SPEC4, SPEC6

# For Conservation Designations (in addition to above):
# 


source_fields = {
    "Species_EnglishName" : "COMMON",
    "Species_ScientificName" : "SCIENTIFIC",
    "Alert_Level" : "STATUS",
    "Alert_Number" : "STATUS_NUM",
    "US_STATUS" : "US_STATUS",
    "CANADA_STATUS" : "CANADA_STATUS",
    "Alpha_Code_6" : "SPEC6",
    "Note" : "NOTES"
}
source_field_data_type = {
    "Species_EnglishName" : "COMMON",
    "Species_ScientificName" : "SCIENTIFIC",
    "Alert_Level" : "STATUS",
    "Alert_Number" : 10,
    "US_STATUS" : "US_STATUS",
    "CANADA_STATUS" : "CANADA_STATUS",
    "Alpha_Code_6" : "SPEC6",
    "Note" : "NOTES"
}