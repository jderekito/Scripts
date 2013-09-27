import arcpy
 
fc = "C:\\Data\\NEMAC\\Projects\\FCAV\\AerialDisturbanceSurveys\\FHM_ADS_2012_4326.shp"
# Create a search cursor 
#
rows = arcpy.SearchCursor(fc) 
# Create a list of string fields
fields = arcpy.ListFields(fc, "", "All")

keepFields = ["FID", "Shape", "OBJECTID", "FS_REGION", "SIRVEU_YEA", "DMG_TYPE", "AGENT_NM", "HOST", "FORTYPE", "NOTES", "ACRES", "HAZARD"]
removeFields = []

for field in fields:
    arcpy.AddMessage("field name = %s" % (field.name))
    if keepFields.count(field.name) == 0:
        arcpy.AddMessage("in list")
        removeFields.append(field.name)

arcpy.AddMessage(removeFields)      
arcpy.DeleteField_management(fc, removeFields)    