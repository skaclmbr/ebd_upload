# create a geojson file from blocks file
# Scott Anderson
# 1/19/23

import os
import json

curr_dir = os.path.dirname(os.path.abspath(__file__))
outjson_fn  = "blocks.geojson"
outjson_fp = "/".join([curr_dir,outjson_fn])

blockjson_fn = "blocks.json"
blockjson_fp = "/".join([curr_dir,blockjson_fn])
blockjson_file = open(blockjson_fn)
blockjson = json.load(blockjson_file)

nl = "\n"

gj = {
    "type" : "FeatureCollection",
    "features" : [

    ]
}

def main():

    count = 0
    for b in blockjson:
        # loop through blocks
        g = {"type" : "Feature"}
        # g["type"] = "Feature"
        g["geometry"] = b["GEOM"]
        del b["GEOM"]
        del b["GAP_SPP"]
        g["properties"] = b
        # del g["properties"]["GEOM"]
        gj["features"].append( g )

        count += 1

        # if count == 10:
        #     break
            
 
    oj = open(
        outjson_fp,
        "w",
        encoding="utf-8"
        )
    oj.write(json.dumps(gj))

if __name__=="__main__":
	main();