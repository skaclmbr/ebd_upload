# Created 6/1/2023
# Scott K. Anderson

import csv
import copy
import datetime
import time
import json


nl = "\n"
ebird_delim = ","
in_drive = (
    "C:/Users/skanderson/State of North Carolina/" + 
    "WRC_NC Bird Atlas - Documents/Science Subcommittee"
    )
in_dir = "current_ebd"

# PROJECT DOWNLOAD
in_file = "NCBA EBD-style data pull 20250422.csv"
in_sample_file = "NCBA EBD-style data pull 20250422_sample.csv"

test_file = open("project_sample.csv", "w", encoding = "utf-8-sig")

bc_xwalk = {
    "AB":{"BREEDING_CODE":"A","BREEDING_CATEGORY":"C3"},
    "DN":{"BREEDING_CODE":"B","BREEDING_CATEGORY":"C3"},
    "CC":{"BREEDING_CODE":"C","BREEDING_CATEGORY":"C3"},
    "FY":{"BREEDING_CODE":"CF","BREEDING_CATEGORY":"C4"},
    "CM":{"BREEDING_CODE":"CN","BREEDING_CATEGORY":"C4"},
    "DD":{"BREEDING_CODE":"DD","BREEDING_CATEGORY":"C4"},
    "FO":{"BREEDING_CODE":"F","BREEDING_CATEGORY":"C1"},
    "FL":{"BREEDING_CODE":"FL","BREEDING_CATEGORY":"C4"},
    "FS":{"BREEDING_CODE":"FS","BREEDING_CATEGORY":"C4"},
    "FR":{"BREEDING_CODE":"FY","BREEDING_CATEGORY":"C4"},
    "OS":{"BREEDING_CODE":"H","BREEDING_CATEGORY":"C2"},
    "SM":{"BREEDING_CODE":"M","BREEDING_CATEGORY":"C3"},
    "VS":{"BREEDING_CODE":"N","BREEDING_CATEGORY":"C3"},
    "NB":{"BREEDING_CODE":"NB","BREEDING_CATEGORY":"C4"},
    "NC":{"BREEDING_CODE":"NC","BREEDING_CATEGORY":"C0"},
    "NE":{"BREEDING_CODE":"NE","BREEDING_CATEGORY":"C4"},
    "NY":{"BREEDING_CODE":"NY","BREEDING_CATEGORY":"C4"},
    "ON":{"BREEDING_CODE":"ON","BREEDING_CATEGORY":"C4"},
    "PO":{"BREEDING_CODE":"P","BREEDING_CATEGORY":"C3"},
    "BP":{"BREEDING_CODE":"PE","BREEDING_CATEGORY":"C4"},
    "S1":{"BREEDING_CODE":"S","BREEDING_CATEGORY":"C2"},
    "S7":{"BREEDING_CODE":"S7","BREEDING_CATEGORY":"C3"},
    "T7":{"BREEDING_CODE":"T","BREEDING_CATEGORY":"C3"},
    "UN":{"BREEDING_CODE":"UN","BREEDING_CATEGORY":"C4"}
    }


# def check_aux_code_value(aux_code):
#     if aux_code in bc_xwalk:
#         # get behavior code
#         result = bc_xwalk[aux_code]
#     elif "|" in aux_code:
#         #adult/juv sex info
#         sex_age = aux_code.split("|")
#         result = {
#             "sex" : sex_age[0],
#             "age" : sex_age[1]
#         }
#     else:
#         result = False

#     return result

def is_coded(aux_code):
    if aux_code in bc_xwalk:
        return True
    else:
        return False

def get_aux_type(aux_code):
    if aux_code in bc_xwalk:
        return "BREEDING_CODE"
    elif "|" in aux_code:
        return "SEX_AGE"
    else:
        return "BREEDING_CODE"

def populate_json(filename):
##############################################################################
    ## POPULATE FILE DATA
    i_fn = "/".join([in_drive,in_dir,filename])
    start = time.perf_counter()
    loop_time = start
    records = {}
    with open(i_fn, "r", encoding="utf-8") as f:
        count = 0
        checklists = set()
        coded_obs = set()
        uncoded_obs = set()
        csv_reader = csv.reader(f)
        for line in csv_reader:

            if count == 0:
                # collect header row as array,
                # set index variables for important fields
                h = line

                print("\n==============\nHEADERS:\n", h)
                checklist_ind = h.index("sub_id")
                obs_ind = h.index("obs_id")
                aux_code_ind = h.index("aux_code")
                value_ind = h.index("value")
            else:
                # add checklist to set

                obs_id = line[obs_ind]
                aux_type = get_aux_type(line[aux_code_ind])
                if obs_id in records:
                    # add aux info
                    records[obs_id][aux_type] = line[value_ind]
                else:
                    # build record
                    curr_record = {}
                    for i, v in enumerate(line):
                        if h[i] == "aux_code":

                            curr_record[aux_type] = line[value_ind]

                        elif h[i] == "value":
                            pass
                        else:
                            curr_record[h[i]] = v

                    records[obs_id] = curr_record


                checklists.add(line[checklist_ind])

                if is_coded(line[aux_code_ind]):
                    coded_obs.add(obs_id)
                    if obs_id in uncoded_obs:
                        uncoded_obs.remove(obs_id)
                else:
                    uncoded_obs.add(obs_id)
                
                # previous_line = line

            if count < 5000:
                test_file.write(",".join(line))

            count += 1
            if count % 100000 == 0:
                # every 100,000 lines print status

                ## Calculate time
                nowt = time.perf_counter()
                elapsed_time = nowt - start
                elapsed_time_str = str(round(elapsed_time,1))
                # secs_per_rec = elapsed_time/count

                print(
                    nl,
                    "== ", filename, " ==", nl,
                    "== ", "elapsed time: ", elapsed_time_str,
                    "s loop time: ", str(round(nowt - loop_time,1)), "s ==", nl,
                    str(f"{count:,}"), "lines read", nl,
                    str(f"{len(checklists):,}"), "checklists", nl,
                    str(f"{len(coded_obs):,}"), "coded obs", nl,
                    str(f"{len(uncoded_obs):,}"), "uncoded obs", nl
                )
                # break
    return records

def make_list(json):
    results = []
    for v in json.values(): results.append(v)
    return results

def main():
    
    # get sample data
    sample_records = populate_json(in_sample_file)
    sample_records_list = make_list(sample_records)
    
    sample_records_out = open(
        "project_sample_records.json",
        "w",
        encoding = "utf-8-sig"
        )
    
    print(str(f"{len(sample_records_list):,}"), "project records found")
    sample_records_out.write(json.dumps(sample_records_list, indent = 2))
    sample_records_out.close()

    atlas_records = populate_json(in_file)
    atlas_records_list = make_list(atlas_records)
    print(str(f"{len(atlas_records_list):,}"), "atlas records found")
    atlas_records_out = open(
        "project_atlas_records.json",
        "w",
        encoding = "utf-8-sig"
        )
    
    atlas_records_out.write(json.dumps(atlas_records_list, indent = 2))
    atlas_records_out.close()

    print("completed!")

if __name__=="__main__":
    main();