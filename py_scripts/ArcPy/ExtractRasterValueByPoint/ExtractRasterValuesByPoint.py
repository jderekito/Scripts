import arcpy
from arcpy import env
from arcpy.sa import *
import re
import time
import glob #The glob module finds all the pathnames matching a specified pattern
import os



# Set environment settings
env.workspace = "c:/Users/KH036s/Desktop/ExtractRasterValueByPoint"
os.chdir("c:/Users/KH036s/Desktop/ExtractRasterValueByPoint")
inPointFeature = "NatRegHistoricPlaces.shp"

	
start = time.time()
arcpy.CheckOutExtension("Spatial")
for file in glob.glob("*.img"):
	arcpy.AddMessage("Currently processing: "+file)
	fieldName = file[:-4] #remove file extenstion
	fieldName = fieldName[:10] #get right 10 chars as shapefile formats have a field limitation of maximum 10 characters in length
	arcpy.AddMessage("with fieldName %s" % fieldName)
	inRasterList = [[file, fieldName]] #[[r['fileName'], fieldName]]
	ExtractMultiValuesToPoints(inPointFeature, inRasterList, "BILINEAR") #this tool adds a field onto the point attribute table with the value of intersect	
end = time.time()
arcpy.AddMessage("Took %s" % str(end - start))