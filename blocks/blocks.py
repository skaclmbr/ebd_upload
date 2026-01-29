"""
blocks.py

author: Scott Anderson

update: 1/18/23
"""

# ArcGIS Online connections
from arcgis.gis import GIS
print(GIS)
from arcgis.features import FeatureLayerCollection
from arcgis.geometry import *

agol_username = "scott.anderson@ncwildlife.org"
agol_pw = "2yR5GnTlpYX6"


def getBlockData():

    