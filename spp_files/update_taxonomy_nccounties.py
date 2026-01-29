#############################################################
## SUITE OF VARIABLES TO LOAD CONSERVATION STATUS OR TAXONOMY

## Birds of North Carolina

# field in Atlas Cache to match to source file
match_id_field = "PRIMARY_COM_NAME"

# source id use to compare to match_id_field
source_id_field = "SpeciesName"

# filename
source_fn = "species_county_stats.csv"

# key to subdict with version data
source_key = "NC_COUNTY_DATA"

# version - will be key for entry in key
source_version = "25"
source_date = "2025-10-08"
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

# compile county data
nc_counties = ["Alamance", "Alexander", "Alleghany", "Anson", "Ashe", "Avery",
               "Beaufort", "Bertie", "Bladen", "Brunswick", "Buncombe", "Burke",
               "Cabarrus", "Caldwell", "Camden", "Carteret", "Caswell",
               "Catawba", "Chatham", "Cherokee", "Chowan", "Clay", "Cleveland",
               "Columbus", "Craven", "Cumberland", "Currituck", "Dare",
               "Davidson", "Davie", "Duplin", "Durham", "Edgecombe", "Forsyth",
               "Franklin", "Gaston", "Gates", "Graham", "Granville", "Greene",
               "Guilford", "Halifax", "Harnett", "Haywood", "Henderson",
               "Hertford", "Hoke", "Hyde", "Iredell", "Jackson", "Johnston",
               "Jones", "Lee", "Lenoir", "Lincoln", "Macon", "Madison",
               "Martin", "McDowell", "Mecklenburg", "Mitchell", "Montgomery",
               "Moore", "Nash", "New Hanover", "Northampton", "Onslow",
               "Orange", "Pamlico", "Pasquotank", "Pender", "Perquimans",
               "Person", "Pitt", "Polk", "Randolph", "Richmond", "Robeson",
               "Rockingham", "Rowan", "Rutherford", "Sampson", "Scotland",
               "Stanly", "Stokes", "Surry", "Swain", "Transylvania", "Tyrrell",
               "Union", "Vance", "Wake", "Warren", "Washington", "Watauga",
               "Wayne", "Wilkes", "Wilson", "Yadkin", "Yancey"]
county_breed = {}
for c in nc_counties:
    county_breed[c] = ""

# outlines which fields to store in xwalk dict
# and the corresponding atlas cache fields
# if "", field will be compiled from multiple fields
# and included in the "source_compiled_fields" dict

source_fields = {
    "SpeciesName" : "NC_SPECIES",
    "County" : "",
    "BreedAbundance" : "",
    "WinterAbundance" : "",
    "Phenology" : ""
}

source_field_data_type = {
    "SpeciesName" : "string"
}

# key/value pairs to compile into a dict
source_compiled_fields = {
    "COUNTY_BREED" : ["County", "BreedAbundance"],
    "COUNTY_WINTER" : ["County", "WinterAbundance"],
    "COUNTY_PHENOLOGY" : ["County", "Phenology"]
}