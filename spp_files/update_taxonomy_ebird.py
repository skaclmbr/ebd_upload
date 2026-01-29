#############################################################
## SUITE OF VARIABLES TO LOAD CONSERVATION STATUS OR TAXONOMY

## Natureserve

# field to match to source file
match_id_field = "SCI_NAME"

# source id use to compare to match_id_field
source_id_field = "AC_ID"


# filename
source_fn = "eBird-Clements-v2024-integrated-checklist-October-2024-rev.csv"

# key to subdict with version data
source_key = "EBIRD_CLEMENTS"

# version - will be key for entry in key
source_version = "2024"
source_date = "2024-10-01"

source_info = {
    "FULL_NAME" : "eBird-Clements Taxonomy",
    "URL" : "https://www.birds.cornell.edu/clementschecklist/introduction/updateindex/october-2024/2024-citation-checklist-downloads/?__hstc=60209138.7fe04f81ca45b0d8dd1dd1460041aa63.1728488753771.1734531592270.1735921069455.36&__hssc=60209138.1.1735921069455&__hsfp=3011104808&_ga=2.44386342.302678126.1735921069-895337938.1728488753&_gl=1*1kcgtrw*_gcl_au*MjA2NzE4Njk2MC4xNzI4NDg4NzUy*_ga*ODk1MzM3OTM4LjE3Mjg0ODg3NTM.*_ga_QR4NVXZ8BM*MTczNTkyMTA2OS40Mi4wLjE3MzU5MjEwNjkuNjAuMC4w"
}

# map source fields to common fields
# For Species Lists:
# ID, RANK (order of species), COMMMON, SCIENTIFIC, ORDER, FAMILY, SUBFAMILY,
# SPEC4, SPEC6

# For Conservation Designations (in addition to above):
# 


source_fields = {
    "sort v2024" : "ID",
    "category": "CATEGORY",
    "English name": "COMMON",
    "scientific name" : "SCIENTIFIC",
    "order": "ORDER",
    "family" : "FAMILY",
    "sort_v2023" : "EBIRD_CODE_2023",
    "species_code" : "EBIRD_CODE",
    "range" : "RANGE",
    "Clements v2024b change" : "CLEMENTS_CHANGE_TEXT",
    "text for website v2024b" : "EBIRD_CHANGE_TEXT"
}
source_field_data_type = {
    "sort v2024" : "ID",
    "category": "CATEGORY",
    "English name": "COMMON",
    "scientific name" : "SCIENTIFIC",
    "order": "ORDER",
    "family" : "FAMILY",
    "sort_v2023" : "EBIRD_CODE_2023",
    "species_code" : "EBIRD_CODE",
    "range" : "RANGE",
    "Clements v2024b change" : "CLEMENTS_CHANGE_TEXT",
    "text for website v2024b" : "EBIRD_CHANGE_TEXT"
}