import arcpy
from arcpy import env
import os
import glob #The glob module finds all the pathnames matching a specified pattern

directory = "C:/Data/PhD/Teaching/GISProgramming/ArcGIS/ReadShpFileAttributes/shps"

env.workspace = directory
os.chdir(directory)

for files in glob.glob("*.shp"):
	print "Currently Inspecting: "+files
	# For each field shapeFile list the field name, type, and length
	fieldList = arcpy.ListFields(files)
	for field in fieldList:
		print("{0} is a type of {1} with a length of {2}".format(field.name, field.type, field.length)) 	