---

---

setwd(
    paste0(
        "C:\\Users\\skanderson\\State of North Carolina\\",
        "WRC_NC Bird Atlas - Documents\\Science Subcomitttee\\current_ebd"
    )
)
# setwd(
#     paste0(
#         "C:\\Users\\skanderson\\OneDrive - State of North Carolina\\",
#         "Documents - WRC_Wildlife Management Division\\Wildlife Diversity ",
#         "program\\projects\\species_listing\\NCSAT_Process_Guide\\Testing ",
#         "NCSAT\\birds"
#     )
# )
############################################################
## JOHN EMAIL - record to check
# https://ebird.org/atlasnc/checklist/S106325580 (this was one of the first edits/reviews I made, so although I don’t remember the exact date I made the change, it definitely wasn’t recent)

# Below is from same checklist in Atlas Cache ebd_mgmt.ebd (is it possible I’m not downloading the most current version? I’m assuming the same file is appended, maybe just overwritten, with new download each month?)
# OBSERVATIONS[17].COMMON_NAME	Ruby-crowned Kinglet
# OBSERVATIONS[17].BREEDING_CODE	S
# OBSERVATIONS[17].BREEDING_CATEGORY	C2
# OBSERVATIONS[17].BEHAVIOR_CODE	S
############################################################


if (!require(tidyverse)) install.packages("tidyverse")
if (!require(auk)) install.packages("auk")

# install.packages(c("cowplot", "googleway", "ggplot2", "ggrepel",
# "ggspatial", "libwgeom", "sf", "rnaturalearth", "rnaturalearthdata"))

library(tidyverse)
library(ggplot2)
theme_set(theme_bw())
library(sf)
library(auk)
library(lubridate)
library(gridExtra)

select <- dplyr::select

f.all.nc <- paste0(
    "C:/Users/skanderson/State of North Carolina/WRC_NC Bird Atlas",
    " - Documents/Science Subcommittee/current_ebd/",
    "ebd_US-NC_202101_202401_relDec-2023.txt")

# load text files into ebd object
ebd <- auk_ebd(
    f.all.nc
)
# define filters for the ebd
ebd_filters <- ebd %>%
    auk_date(date = "2022-04-05") %>%
    # auk_species("Seaside Sparrow") %>%
    # auk_county( counties ) %>% #only counties where SESP detected
    # auk_protocol(
    #     protocol = c(
    #         "Stationary",
    #         "Traveling"
    #     )
    # ) %>%
    auk_complete()
# list out the filters
ebd_filters


# output files
data_dir <- "data"
if (!dir.exists(data_dir)) {
  dir.create(data_dir)
}
f_ebd <- file.path(data_dir, "ebd_sesp_nc_coast.txt")
f_sampling <- file.path(data_dir, "ebd_checklists_nc_coast.txt")

# only run if the files don't already exist
if (!file.exists(f_ebd)) {
  auk_filter(ebd_filters, file = f_ebd, file_sampling = f_sampling)
}

# create a zero-filled version of the data
ebd_zf <- auk_zerofill(f_ebd, f_sampling, collapse = TRUE)

# add some fields that will help with analysis, incl converting time to dec
time_to_decimal <- function(x) {
    x <- hms(x, quiet = TRUE)
    hour(x) + minute (x) / 60 + second(x) / 3600
}

ebd_zf <- ebd_zf %>%
    mutate(
        observation_count = ifelse (
            observation_count == "X",
            NA_character_,
            observation_count
            ),
        observation_count = as.integer(observation_count),
        effort_distance_km = if_else(
            protocol_type != "Traveling",
            0,
            effort_distance_km),
        time_observations_started = time_to_decimal(time_observations_started),
        year = year(observation_date),
        day_of_year = yday(observation_date)
    )

ebd_zf_filtered <- ebd_zf %>%
    filter (
        duration_minutes <=5 * 60,
        effort_distance_km <=5,
        year >= 2000,
        number_observers <= 10
    )

ebird <- ebd_zf_filtered %>%
      select(
        checklist_id,
        observer_id,
        sampling_event_identifier,
        scientific_name,
        observation_count,
        species_observed,
        state_code,
        locality_id,
        latitude,
        longitude,
        protocol_type,
        all_species_reported,
        observation_date,
        year,
        day_of_year,
        time_observations_started,
        duration_minutes,
        effort_distance_km,
        number_observers
        )
write_csv(ebird, "data/ebd_sesp_nc_coast_zf.csv", na = "")


