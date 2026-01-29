##########################################################################
## Functions to calculate nocturnal hours
## Version 1.0
## Scott K. Anderson
## scott.anderson@ncwildlife.org
## 1/3/2023
##
## This function calculates the following from the provided date/time
## noc_ebird = indicator if time is within eBird nocturnal specs (EBD_NOCTURNAL)
## noc_ncba = indicator if time within NCBA nocturnal specs (NCBA_NOCTURNAL)
## noc_duration = total nocturnal duration (minutes)
## noc_partial = indicator if checklist crosses nocturnal times
## check_start_utc = checklist datetime in UTC (NCBA_OBSDT_UTC)
## check_start = checklist start datetime (local)
## check_end = checklist end datetime (local)
## 
##########################################################################

from datetime import datetime, timedelta
from pytz import timezone
from zoneinfo import ZoneInfo
from astral import LocationInfo
from astral.sun import sun


astraltz = ZoneInfo("America/New_York")
utctz = ZoneInfo("UTC")
sunrise_td = timedelta(minutes=-40) #nocturnal ends 40 min before sunrise
sunset_td = timedelta(minutes=20) #nocturnal starts 20 min after sunset
day_before = timedelta(days=-1)
day_after = timedelta(days=1)
eastern = timezone("US/Eastern")
dtformat = "%Y-%m-%dT%H:%M:%S%z"
utcformat = "%Y-%m-%dT%H:%M:%SZ"

#set location
li = LocationInfo(
    "New York",
    "United States",
    "US/NY",
    35.5,
    -79.5
    )

    
def getDateTime(d,t):
    # example d = 2020-10-21 12:20:00.0
    #returns dict of datetime components
    date = d.split(" ")
    date = date[0].split("-")
    time = t.split(":")

    r = datetime(
        int(date[0]), # year
        int(date[1]), # month
        int(date[2]), # day
        int(time[0]), # hour
        int(time[1]), # min
        int(time[2]) # sec
    )
    
    return eastern.localize(r)


def getNocStatus(id, d, t, li, dur):
     
    r = {"_id": id}
    # check to make sure time is present
    if len(str(t)) > 0:
        #create datetime object
        dt = getDateTime(d,t)
        r["check_start"] = {
            "$date" : dt.strftime(dtformat)
            }
        r["check_start_utc"] = {
            "$date": dt.astimezone(tz=utctz).strftime(utcformat)
            }

        dt_end = dt + timedelta(minutes=dur) #calculate end time
        s = sun(li.observer, dt, tzinfo=astraltz)
        noc_start = s["sunset"] + sunset_td
        noc_end = s["sunrise"] + sunrise_td
        
        r["check_end"] = {
            "$date" : dt_end.strftime(dtformat)
            }
        r["noc_start"] = {
            "$date" : noc_start.strftime(dtformat)
        }
        r["noc_end"] = {
            "$date" : noc_end.strftime(dtformat)
            }
        r["noc_partial"] = "0"

        #Is start date in:
        #   first half (sunset+20min to midnight)
        #   second half (midnight to sunrise-40min)

        if (dt >= noc_start):
            #first half of night
            r["noc_ncba"] = "1"
            r["noc_ebird"] = "1"

            # get sunrise day after
            night_end_s = sun(
                li.observer,
                (dt + day_after),
                tzinfo=astraltz
                )
            night_end = night_end_s["sunrise"] + sunrise_td # adjust -40 min
            r["noc_duration"] = (
                min(night_end, dt_end) -
                dt
                ).total_seconds()/60

            if (dt_end > night_end): r["noc_partial"] = "1"
        
        elif (dt <= noc_end):
            #second half of night
            r["noc_ncba"] = "1"
            r["noc_ebird"] = "1"

            r["noc_duration"] = (
                min(noc_end, dt_end) -
                dt
            ).total_seconds()/60

            if (dt_end > noc_end): r["noc_partial"] = "1"

        else:
            #does not start during nocturnal hours
            #all of these do not qualify for ebird nocturnal
            r["noc_ebird"] = "0"

            if (dt_end >= noc_start):
                #ends in first half of night
                #begins before sunset
                r["noc_ncba"] = "1"
                r["noc_partial"] = "1"

                r["noc_duration"] = (
                    dt_end - noc_start
                ).total_seconds()/60
            
            elif (dt_end <= noc_end):
                #ends in second half of night
                #begins before sunset previous day
                r["noc_ncba"] = "1"
                r["noc_partial"] = "1"

                # get sunrise day before
                night_start_s = sun(
                    li.observer,
                    (dt + day_before),
                    tzinfo=astraltz
                    )
                
                #adjust +20 min
                night_start = night_start_s["sunset"] + sunset_td
                r["noc_duration"] = (
                    dt_end - night_start
                    ).total_seconds()/60

            else:
                #does not start or end during nocturnal hours
                r["noc_ncba"] = "0"
                r["noc_duration"] = 0

		#time value not present, set to noon
    else:
        time_started = "12:00:00"
        #create datetime object
        dt = getDateTime(d,time_started)
        
        r["check_start"] = {
            "$date" : dt.strftime(dtformat)
            }
        r["check_start_utc"] = {
            "$date": dt.astimezone(tz=utctz).strftime(utcformat)
            }

    return r