# ---------------------------------------------------------------------------
# AutomateNCAPrep.py
# Created on: 2012-03-29
# Created by: Derek Morgan
# Description: for preprocessing NCA files
# Dependencies: this script is written for ArcGIS 10 python API, and thereore
# as dependencies to that environment.
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
import os
import glob

modelsCRCM = [{'fileName' : 'crcm_ccsm_cdd_mean'},
    {'fileName' : 'crcm_ccsm_gdd50_mean'},
    {'fileName' : 'crcm_ccsm_hdd_mean'},
    {'fileName' : 'crcm_ccsm_pp_1'},
    {'fileName' : 'crcm_ccsm_pp_2'},
    {'fileName' : 'crcm_ccsm_pp_3'},
    {'fileName' : 'crcm_ccsm_pp_4'},
    {'fileName' : 'crcm_ccsm_run_pp3'},
    {'fileName' : 'crcm_ccsm_run_tn32'},
    {'fileName' : 'crcm_ccsm_run_tx100'},
    {'fileName' : 'crcm_ccsm_run_tx95'},
    {'fileName' : 'crcm_ccsm_tn_0'},
    {'fileName' : 'crcm_ccsm_tn_10'},
    {'fileName' : 'crcm_ccsm_tn_32'},
    {'fileName' : 'crcm_ccsm_tx_100'},
    {'fileName' : 'crcm_ccsm_tx_90'},
    {'fileName' : 'crcm_ccsm_tx_95'},
    {'fileName' : 'crcm_cgcm3_cdd_mean'},
    {'fileName' : 'crcm_cgcm3_gdd50_mean'},
    {'fileName' : 'crcm_cgcm3_hdd_mean'},
    {'fileName' : 'crcm_cgcm3_pp_1'},
    {'fileName' : 'crcm_cgcm3_pp_2'},
    {'fileName' : 'crcm_cgcm3_pp_3'},
    {'fileName' : 'crcm_cgcm3_pp_4'},
    {'fileName' : 'crcm_cgcm3_run_pp3'},
    {'fileName' : 'crcm_cgcm3_run_tn32'},
    {'fileName' : 'crcm_cgcm3_run_tx100'},
    {'fileName' : 'crcm_cgcm3_run_tx95'},
    {'fileName' : 'crcm_cgcm3_tn_0'},
    {'fileName' : 'crcm_cgcm3_tn_10'},
    {'fileName' : 'crcm_cgcm3_tn_32'},
    {'fileName' : 'crcm_cgcm3_tx_100'},
    {'fileName' : 'crcm_cgcm3_tx_90'},
    {'fileName' : 'crcm_cgcm3_tx_95'}]

modelsMM5I = [{'fileName' : 'mm5i_ccsm_cdd_mean'}, 
    {'fileName' : 'mm5i_ccsm_gdd50_mean'}, 
    {'fileName' : 'mm5i_ccsm_hdd_mean'}, 
    {'fileName' : 'mm5i_ccsm_pp_1'}, 
    {'fileName' : 'mm5i_ccsm_pp_2'}, 
    {'fileName' : 'mm5i_ccsm_pp_3'}, 
    {'fileName' : 'mm5i_ccsm_pp_4'}, 
    {'fileName' : 'mm5i_ccsm_run_pp3'}, 
    {'fileName' : 'mm5i_ccsm_run_tn32'}, 
    {'fileName' : 'mm5i_ccsm_run_tx100'}, 
    {'fileName' : 'mm5i_ccsm_run_tx95'}, 
    {'fileName' : 'mm5i_ccsm_tn_0'}, 
    {'fileName' : 'mm5i_ccsm_tn_10'}, 
    {'fileName' : 'mm5i_ccsm_tn_32'}, 
    {'fileName' : 'mm5i_ccsm_tx_100'}, 
    {'fileName' : 'mm5i_ccsm_tx_90'}, 
    {'fileName' : 'mm5i_ccsm_tx_95'}]

modelsRCM3 = [{'fileName' : 'rcm3_cgcm3_cdd_mean'}, 
    {'fileName' : 'rcm3_cgcm3_gdd50_mean'}, 
    {'fileName' : 'rcm3_cgcm3_hdd_mean'}, 
    {'fileName' : 'rcm3_cgcm3_pp_1'}, 
    {'fileName' : 'rcm3_cgcm3_pp_2'}, 
    {'fileName' : 'rcm3_cgcm3_pp_3'}, 
    {'fileName' : 'rcm3_cgcm3_pp_4'}, 
    {'fileName' : 'rcm3_cgcm3_run_pp3'}, 
    {'fileName' : 'rcm3_cgcm3_run_tn32'}, 
    {'fileName' : 'rcm3_cgcm3_run_tx100'}, 
    {'fileName' : 'rcm3_cgcm3_run_tx95'}, 
    {'fileName' : 'rcm3_cgcm3_tn_0'}, 
    {'fileName' : 'rcm3_cgcm3_tn_10'}, 
    {'fileName' : 'rcm3_cgcm3_tn_32'}, 
    {'fileName' : 'rcm3_cgcm3_tx_100'}, 
    {'fileName' : 'rcm3_cgcm3_tx_90'}, 
    {'fileName' : 'rcm3_cgcm3_tx_95'}, 
    {'fileName' : 'rcm3_gfdl_cdd_mean'}, 
    {'fileName' : 'rcm3_gfdl_gdd50_mean'}, 
    {'fileName' : 'rcm3_gfdl_hdd_mean'}, 
    {'fileName' : 'rcm3_gfdl_pp_1'}, 
    {'fileName' : 'rcm3_gfdl_pp_2'}, 
    {'fileName' : 'rcm3_gfdl_pp_3'}, 
    {'fileName' : 'rcm3_gfdl_pp_4'}, 
    {'fileName' : 'rcm3_gfdl_run_pp3'}, 
    {'fileName' : 'rcm3_gfdl_run_tn32'}, 
    {'fileName' : 'rcm3_gfdl_run_tx100'}, 
    {'fileName' : 'rcm3_gfdl_run_tx95'}, 
    {'fileName' : 'rcm3_gfdl_tn_0'}, 
    {'fileName' : 'rcm3_gfdl_tn_10'}, 
    {'fileName' : 'rcm3_gfdl_tn_32'}, 
    {'fileName' : 'rcm3_gfdl_tx_100'}, 
    {'fileName' : 'rcm3_gfdl_tx_90'}, 
    {'fileName' : 'rcm3_gfdl_tx_95'}]

modelsWRFG = [{'fileName' : 'wrfg_ccsm_cdd_mean'}, 
    {'fileName' : 'wrfg_ccsm_gdd50_mean'}, 
    {'fileName' : 'wrfg_ccsm_hdd_mean'}, 
    {'fileName' : 'wrfg_ccsm_pp_1'}, 
    {'fileName' : 'wrfg_ccsm_pp_2'}, 
    {'fileName' : 'wrfg_ccsm_pp_3'}, 
    {'fileName' : 'wrfg_ccsm_pp_4'}, 
    {'fileName' : 'wrfg_ccsm_run_pp3'}, 
    {'fileName' : 'wrfg_ccsm_run_tn32'}, 
    {'fileName' : 'wrfg_ccsm_run_tx100'}, 
    {'fileName' : 'wrfg_ccsm_run_tx95'}, 
    {'fileName' : 'wrfg_ccsm_tn_0'}, 
    {'fileName' : 'wrfg_ccsm_tn_10'}, 
    {'fileName' : 'wrfg_ccsm_tn_32'}, 
    {'fileName' : 'wrfg_ccsm_tx_100'}, 
    {'fileName' : 'wrfg_ccsm_tx_90'}, 
    {'fileName' : 'wrfg_ccsm_tx_95'}, 
    {'fileName' : 'wrfg_cgcm3_cdd_mean'}, 
    {'fileName' : 'wrfg_cgcm3_gdd50_mean'}, 
    {'fileName' : 'wrfg_cgcm3_hdd_mean'}, 
    {'fileName' : 'wrfg_cgcm3_pp_1'}, 
    {'fileName' : 'wrfg_cgcm3_pp_2'}, 
    {'fileName' : 'wrfg_cgcm3_pp_3'}, 
    {'fileName' : 'wrfg_cgcm3_pp_4'}, 
    {'fileName' : 'wrfg_cgcm3_run_pp3'}, 
    {'fileName' : 'wrfg_cgcm3_run_tn32'}, 
    {'fileName' : 'wrfg_cgcm3_run_tx100'}, 
    {'fileName' : 'wrfg_cgcm3_run_tx95'}, 
    {'fileName' : 'wrfg_cgcm3_tn_0'}, 
    {'fileName' : 'wrfg_cgcm3_tn_10'}, 
    {'fileName' : 'wrfg_cgcm3_tn_32'}, 
    {'fileName' : 'wrfg_cgcm3_tx_100'}, 
    {'fileName' : 'wrfg_cgcm3_tx_90'}, 
    {'fileName' : 'wrfg_cgcm3_tx_95'}]
    

    

#1. Generate raster files from NetCDF files----------------------------------------------------    
def NetCDFToRaster():
    for mid in modelsCRCM:
        arcpy.AddMessage("fileName: " + mid['fileName'])
        modelFile = "C:\\Data\\NEMAC\\Projects\\NCA\\NCANetcdfProcessing\\output_files\\"+mid['fileName']+".nc"
        arcpy.AddMessage("modelFile: " + modelFile)
        #result1 -------------------
        outLayer=""+mid['fileName']+"ModelResult1"
        result1 = arcpy.MakeNetCDFRasterLayer_md(modelFile, "result1", "xc", "yc", outLayer, "", "", "BY_VALUE")
        outRaster = ""+mid['fileName']+"_result1.tif"
        arcpy.AddMessage("outRaster: " + outRaster) 
        arcpy.AddMessage("outLayer: " + outLayer) 
        result1 = arcpy.CopyRaster_management(outLayer,outRaster)    
        #result2 --------------------
        outLayer=""+mid['fileName']+"ModelResult2"
        result2 = arcpy.MakeNetCDFRasterLayer_md(modelFile, "result2", "xc", "yc", outLayer, "", "", "BY_VALUE")
        outRaster = ""+mid['fileName']+"_result2.tif"
        arcpy.AddMessage("outRaster: " + outRaster) 
        arcpy.AddMessage("outLayer: " + outLayer)     
        result2 = arcpy.CopyRaster_management(outLayer,outRaster)    
        #resultNCEP --------------------------------
        outLayer=""+mid['fileName']+"ModelsResultNCEP"
        resultNCEP = arcpy.MakeNetCDFRasterLayer_md(modelFile, "ncep", "xc", "yc", outLayer, "", "", "BY_VALUE")
        outRaster = ""+mid['fileName']+"_resultNCEP.tif"
        arcpy.AddMessage("outRaster: " + outRaster) 
        arcpy.AddMessage("outLayer: " + outLayer)     
        resultNCEP = arcpy.CopyRaster_management(outLayer,outRaster)    
    for mid in modelsMM5I:
        arcpy.AddMessage("fileName: " + mid['fileName'])
        modelFile = "C:\\Data\\NEMAC\\Projects\\NCA\\NCANetcdfProcessing\\output_files\\"+mid['fileName']+".nc"
        arcpy.AddMessage("modelFile: " + modelFile)
        #result1 -------------------
        outLayer=""+mid['fileName']+"ModelResult1"
        result1 = arcpy.MakeNetCDFRasterLayer_md(modelFile, "result1", "xc", "yc", outLayer, "", "", "BY_VALUE")
        outRaster = ""+mid['fileName']+"_result1.tif"
        arcpy.AddMessage("outRaster: " + outRaster) 
        arcpy.AddMessage("outLayer: " + outLayer) 
        result1 = arcpy.CopyRaster_management(outLayer,outRaster)    
        #result2 --------------------
        outLayer=""+mid['fileName']+"ModelResult2"
        result2 = arcpy.MakeNetCDFRasterLayer_md(modelFile, "result2", "xc", "yc", outLayer, "", "", "BY_VALUE")
        outRaster = ""+mid['fileName']+"_result2.tif"
        arcpy.AddMessage("outRaster: " + outRaster) 
        arcpy.AddMessage("outLayer: " + outLayer)     
        result2 = arcpy.CopyRaster_management(outLayer,outRaster)    
        #resultNCEP --------------------------------
        outLayer=""+mid['fileName']+"ModelsResultNCEP"
        resultNCEP = arcpy.MakeNetCDFRasterLayer_md(modelFile, "ncep", "xc", "yc", outLayer, "", "", "BY_VALUE")
        outRaster = ""+mid['fileName']+"_resultNCEP.tif"
        arcpy.AddMessage("outRaster: " + outRaster) 
        arcpy.AddMessage("outLayer: " + outLayer)     
        resultNCEP = arcpy.CopyRaster_management(outLayer,outRaster)    
    for mid in modelsRCM3:
        arcpy.AddMessage("fileName: " + mid['fileName'])
        modelFile = "C:\\Data\\NEMAC\\Projects\\NCA\\NCANetcdfProcessing\\output_files\\"+mid['fileName']+".nc"
        arcpy.AddMessage("modelFile: " + modelFile)
        #result1 -------------------
        outLayer=""+mid['fileName']+"ModelResult1"
        result1 = arcpy.MakeNetCDFRasterLayer_md(modelFile, "result1", "xc", "yc", outLayer, "", "", "BY_VALUE")
        outRaster = ""+mid['fileName']+"_result1.tif"
        arcpy.AddMessage("outRaster: " + outRaster) 
        arcpy.AddMessage("outLayer: " + outLayer) 
        result1 = arcpy.CopyRaster_management(outLayer,outRaster)    
        #result2 --------------------
        outLayer=""+mid['fileName']+"ModelResult2"
        result2 = arcpy.MakeNetCDFRasterLayer_md(modelFile, "result2", "xc", "yc", outLayer, "", "", "BY_VALUE")
        outRaster = ""+mid['fileName']+"_result2.tif"
        arcpy.AddMessage("outRaster: " + outRaster) 
        arcpy.AddMessage("outLayer: " + outLayer)     
        result2 = arcpy.CopyRaster_management(outLayer,outRaster)    
        #resultNCEP --------------------------------
        outLayer=""+mid['fileName']+"ModelsResultNCEP"
        resultNCEP = arcpy.MakeNetCDFRasterLayer_md(modelFile, "ncep", "xc", "yc", outLayer, "", "", "BY_VALUE")
        outRaster = ""+mid['fileName']+"_resultNCEP.tif"
        arcpy.AddMessage("outRaster: " + outRaster) 
        arcpy.AddMessage("outLayer: " + outLayer)     
        resultNCEP = arcpy.CopyRaster_management(outLayer,outRaster)    
    for mid in modelsWRFG:
        arcpy.AddMessage("fileName: " + mid['fileName'])
        modelFile = "C:\\Data\\NEMAC\\Projects\\NCA\\NCANetcdfProcessing\\output_files\\"+mid['fileName']+".nc"
        arcpy.AddMessage("modelFile: " + modelFile)
        #result1 -------------------
        outLayer=""+mid['fileName']+"ModelResult1"
        result1 = arcpy.MakeNetCDFRasterLayer_md(modelFile, "result1", "xc", "yc", outLayer, "", "", "BY_VALUE")
        outRaster = ""+mid['fileName']+"_result1.tif"
        arcpy.AddMessage("outRaster: " + outRaster) 
        arcpy.AddMessage("outLayer: " + outLayer) 
        result1 = arcpy.CopyRaster_management(outLayer,outRaster)    
        #result2 --------------------
        outLayer=""+mid['fileName']+"ModelResult2"
        result2 = arcpy.MakeNetCDFRasterLayer_md(modelFile, "result2", "xc", "yc", outLayer, "", "", "BY_VALUE")
        outRaster = ""+mid['fileName']+"_result2.tif"
        arcpy.AddMessage("outRaster: " + outRaster) 
        arcpy.AddMessage("outLayer: " + outLayer)     
        result2 = arcpy.CopyRaster_management(outLayer,outRaster)    
        #resultNCEP --------------------------------
        outLayer=""+mid['fileName']+"ModelsResultNCEP"
        resultNCEP = arcpy.MakeNetCDFRasterLayer_md(modelFile, "ncep", "xc", "yc", outLayer, "", "", "BY_VALUE")
        outRaster = ""+mid['fileName']+"_resultNCEP.tif"
        arcpy.AddMessage("outRaster: " + outRaster) 
        arcpy.AddMessage("outLayer: " + outLayer)     
        resultNCEP = arcpy.CopyRaster_management(outLayer,outRaster)    
#----------------------------------------------------------------------------------------------------
        

        
#2. Define projections and assign to raster files----------------------------------------------------    
def ProjectRaster():
    for mid in modelsCRCM:
        #result1
        inRaster = ""+mid['fileName']+"_result1.tif"
        arcpy.AddMessage("inRaster: " + inRaster) 
        outRaster = ""+mid['fileName']+"_result1WGS84.tif"
        inPrjFile = inRaster
        prjFile = r"C:\\Data\\NEMAC\\Projects\\NCA\\Scripting\\ArcPyGDAL\\proj_files\\CRCM.prj"
        arcpy.DefineProjection_management(inPrjFile, prjFile)
        #arcpy.ProjectRaster_management(inRaster, "projected\\"+outRaster, "PROJCS['WGS_1984_Web_Mercator',GEOGCS['GCS_WGS_1984_Major_Auxiliary_Sphere',DATUM['D_WGS_1984_Major_Auxiliary_Sphere',SPHEROID['WGS_1984_Major_Auxiliary_Sphere',6378137.0,0.0]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],UNIT['Meter',1.0]]", "NEAREST", "50000", "WGS_1984_Major_Auxiliary_Sphere_To_WGS_1984", "", "PROJCS['CRCM',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Stereographic_North_Pole'],PARAMETER['False_Easting',3475000.0],PARAMETER['False_Northing',7475000.0],PARAMETER['Central_Meridian',263.0],PARAMETER['Standard_Parallel_1',60.0],UNIT['Meter',1.0]]")
        arcpy.ProjectRaster_management(inRaster, "projected\\"+outRaster, "PROJCS['WGS_1984_Web_Mercator_Auxiliary_Sphere',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator_Auxiliary_Sphere'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],PARAMETER['Auxiliary_Sphere_Type',0.0],UNIT['Meter',1.0]]", "NEAREST", "50000", "", "", "PROJCS['CRCM',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Stereographic_North_Pole'],PARAMETER['false_easting',3475000.0],PARAMETER['false_northing',7475000.0],PARAMETER['central_meridian',263.0],PARAMETER['standard_parallel_1',60.0],UNIT['Meter',1.0]]")
        #result2
        inRaster = ""+mid['fileName']+"_result2.tif"
        arcpy.AddMessage("inRaster: " + inRaster) 
        outRaster = ""+mid['fileName']+"_result2WGS84.tif"
        inPrjFile = inRaster
        prjFile = r"C:\\Data\\NEMAC\\Projects\\NCA\\Scripting\\ArcPyGDAL\\proj_files\\CRCM.prj"
        arcpy.DefineProjection_management(inPrjFile, prjFile)
        #arcpy.ProjectRaster_management(inRaster, "projected\\"+outRaster, "PROJCS['WGS_1984_Web_Mercator',GEOGCS['GCS_WGS_1984_Major_Auxiliary_Sphere',DATUM['D_WGS_1984_Major_Auxiliary_Sphere',SPHEROID['WGS_1984_Major_Auxiliary_Sphere',6378137.0,0.0]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],UNIT['Meter',1.0]]", "NEAREST", "50000", "WGS_1984_Major_Auxiliary_Sphere_To_WGS_1984", "", "PROJCS['CRCM',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Stereographic_North_Pole'],PARAMETER['False_Easting',3475000.0],PARAMETER['False_Northing',7475000.0],PARAMETER['Central_Meridian',263.0],PARAMETER['Standard_Parallel_1',60.0],UNIT['Meter',1.0]]")
        arcpy.ProjectRaster_management(inRaster, "projected\\"+outRaster, "PROJCS['WGS_1984_Web_Mercator_Auxiliary_Sphere',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator_Auxiliary_Sphere'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],PARAMETER['Auxiliary_Sphere_Type',0.0],UNIT['Meter',1.0]]", "NEAREST", "50000", "", "", "PROJCS['CRCM',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Stereographic_North_Pole'],PARAMETER['false_easting',3475000.0],PARAMETER['false_northing',7475000.0],PARAMETER['central_meridian',263.0],PARAMETER['standard_parallel_1',60.0],UNIT['Meter',1.0]]")
        #resultNCEP
        inRaster = ""+mid['fileName']+"_resultNCEP.tif"
        arcpy.AddMessage("inRaster: " + inRaster) 
        outRaster = ""+mid['fileName']+"_resultNCEPWGS84.tif"
        inPrjFile = inRaster
        prjFile = r"C:\\Data\\NEMAC\\Projects\\NCA\\Scripting\\ArcPyGDAL\\proj_files\\CRCM.prj"
        arcpy.DefineProjection_management(inPrjFile, prjFile)
        #arcpy.ProjectRaster_management(inRaster, "projected\\"+outRaster, "PROJCS['WGS_1984_Web_Mercator',GEOGCS['GCS_WGS_1984_Major_Auxiliary_Sphere',DATUM['D_WGS_1984_Major_Auxiliary_Sphere',SPHEROID['WGS_1984_Major_Auxiliary_Sphere',6378137.0,0.0]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],UNIT['Meter',1.0]]", "NEAREST", "50000", "WGS_1984_Major_Auxiliary_Sphere_To_WGS_1984", "", "PROJCS['CRCM',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Stereographic_North_Pole'],PARAMETER['False_Easting',3475000.0],PARAMETER['False_Northing',7475000.0],PARAMETER['Central_Meridian',263.0],PARAMETER['Standard_Parallel_1',60.0],UNIT['Meter',1.0]]")        
        arcpy.ProjectRaster_management(inRaster, "projected\\"+outRaster, "PROJCS['WGS_1984_Web_Mercator_Auxiliary_Sphere',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator_Auxiliary_Sphere'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],PARAMETER['Auxiliary_Sphere_Type',0.0],UNIT['Meter',1.0]]", "NEAREST", "50000", "", "", "PROJCS['CRCM',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Stereographic_North_Pole'],PARAMETER['false_easting',3475000.0],PARAMETER['false_northing',7475000.0],PARAMETER['central_meridian',263.0],PARAMETER['standard_parallel_1',60.0],UNIT['Meter',1.0]]")
    for mid in modelsMM5I:        
        #result1
        inRaster = ""+mid['fileName']+"_result1.tif"
        arcpy.AddMessage("inRaster: " + inRaster) 
        outRaster = ""+mid['fileName']+"_result1WGS84.tif"
        inPrjFile = inRaster
        prjFile = r"C:\\Data\\NEMAC\\Projects\\NCA\\Scripting\\ArcPyGDAL\\proj_files\\MM5i.prj"
        arcpy.DefineProjection_management(inPrjFile, prjFile)
        arcpy.ProjectRaster_management(inRaster, "projected\\"+outRaster, "PROJCS['WGS_1984_Web_Mercator_Auxiliary_Sphere',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator_Auxiliary_Sphere'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],PARAMETER['Auxiliary_Sphere_Type',0.0],UNIT['Meter',1.0]]", "NEAREST", "50000", "NAD_1983_To_WGS_1984_1", "", "PROJCS['MM5i',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',3825000.0],PARAMETER['False_Northing',3200000.0],PARAMETER['Central_Meridian',-97.0],PARAMETER['Standard_Parallel_1',30.0],PARAMETER['Standard_Parallel_2',60.0],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',47.5],UNIT['Meter',1.0]]")
        #result2
        inRaster = ""+mid['fileName']+"_result2.tif"
        arcpy.AddMessage("inRaster: " + inRaster) 
        outRaster = ""+mid['fileName']+"_result2WGS84.tif"
        inPrjFile = inRaster
        prjFile = r"C:\\Data\\NEMAC\\Projects\\NCA\\Scripting\\ArcPyGDAL\\proj_files\\MM5i.prj"
        arcpy.DefineProjection_management(inPrjFile, prjFile)
        arcpy.ProjectRaster_management(inRaster, "projected\\"+outRaster, "PROJCS['WGS_1984_Web_Mercator_Auxiliary_Sphere',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator_Auxiliary_Sphere'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],PARAMETER['Auxiliary_Sphere_Type',0.0],UNIT['Meter',1.0]]", "NEAREST", "50000", "NAD_1983_To_WGS_1984_1", "", "PROJCS['MM5i',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',3825000.0],PARAMETER['False_Northing',3200000.0],PARAMETER['Central_Meridian',-97.0],PARAMETER['Standard_Parallel_1',30.0],PARAMETER['Standard_Parallel_2',60.0],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',47.5],UNIT['Meter',1.0]]")
        #resultNCEP
        inRaster = ""+mid['fileName']+"_resultNCEP.tif"
        arcpy.AddMessage("inRaster: " + inRaster) 
        outRaster = ""+mid['fileName']+"_resultNCEPWGS84.tif"
        inPrjFile = inRaster
        prjFile = r"C:\\Data\\NEMAC\\Projects\\NCA\\Scripting\\ArcPyGDAL\\proj_files\\MM5i.prj"
        arcpy.DefineProjection_management(inPrjFile, prjFile)
        arcpy.ProjectRaster_management(inRaster, "projected\\"+outRaster, "PROJCS['WGS_1984_Web_Mercator_Auxiliary_Sphere',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator_Auxiliary_Sphere'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],PARAMETER['Auxiliary_Sphere_Type',0.0],UNIT['Meter',1.0]]", "NEAREST", "50000", "NAD_1983_To_WGS_1984_1", "", "PROJCS['MM5i',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',3825000.0],PARAMETER['False_Northing',3200000.0],PARAMETER['Central_Meridian',-97.0],PARAMETER['Standard_Parallel_1',30.0],PARAMETER['Standard_Parallel_2',60.0],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',47.5],UNIT['Meter',1.0]]")        
    for mid in modelsRCM3:
        #result1
        inRaster = ""+mid['fileName']+"_result1.tif"
        arcpy.AddMessage("inRaster: " + inRaster) 
        outRaster = ""+mid['fileName']+"_result1WGS84.tif"
        inPrjFile = inRaster
        prjFile = r"C:\\Data\\NEMAC\\Projects\\NCA\\Scripting\\ArcPyGDAL\\proj_files\\RCM3.prj"
        arcpy.DefineProjection_management(inPrjFile, prjFile)
        #arcpy.ProjectRaster_management(inRaster, "projected\\"+outRaster, "PROJCS['WGS_1984_Web_Mercator',GEOGCS['GCS_WGS_1984_Major_Auxiliary_Sphere',DATUM['D_WGS_1984_Major_Auxiliary_Sphere',SPHEROID['WGS_1984_Major_Auxiliary_Sphere',6378137.0,0.0]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator'],PARAMETER['false_easting',0.0],PARAMETER['false_northing',0.0],PARAMETER['central_meridian',0.0],PARAMETER['standard_parallel_1',0.0],UNIT['Meter',1.0]]", "NEAREST", "50000", "WGS_1984_Major_Auxiliary_Sphere_To_WGS_1984", "", "PROJCS['RCM3',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',3925000.0],PARAMETER['False_Northing',3175000.0],PARAMETER['Central_Meridian',-97.0],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',47.5],UNIT['Meter',1.0]]")
        arcpy.ProjectRaster_management(inRaster, "projected\\"+outRaster, "PROJCS['WGS_1984_Web_Mercator_Auxiliary_Sphere',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator_Auxiliary_Sphere'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],PARAMETER['Auxiliary_Sphere_Type',0.0],UNIT['Meter',1.0]]", "NEAREST", "50000", "", "", "PROJCS['RCM3',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Stereographic_North_Pole'],PARAMETER['false_easting',3475000.0],PARAMETER['false_northing',7475000.0],PARAMETER['central_meridian',263.0],PARAMETER['standard_parallel_1',60.0],UNIT['Meter',1.0]]")
        #result2
        inRaster = ""+mid['fileName']+"_result2.tif"
        arcpy.AddMessage("inRaster: " + inRaster) 
        outRaster = ""+mid['fileName']+"_result2WGS84.tif"
        inPrjFile = inRaster
        prjFile = r"C:\\Data\\NEMAC\\Projects\\NCA\\Scripting\\ArcPyGDAL\\proj_files\\RCM3.prj"
        arcpy.DefineProjection_management(inPrjFile, prjFile)
        #arcpy.ProjectRaster_management(inRaster, "projected\\"+outRaster, "PROJCS['WGS_1984_Web_Mercator',GEOGCS['GCS_WGS_1984_Major_Auxiliary_Sphere',DATUM['D_WGS_1984_Major_Auxiliary_Sphere',SPHEROID['WGS_1984_Major_Auxiliary_Sphere',6378137.0,0.0]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator'],PARAMETER['false_easting',0.0],PARAMETER['false_northing',0.0],PARAMETER['central_meridian',0.0],PARAMETER['standard_parallel_1',0.0],UNIT['Meter',1.0]]", "NEAREST", "50000", "WGS_1984_Major_Auxiliary_Sphere_To_WGS_1984", "", "PROJCS['RCM3',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',3925000.0],PARAMETER['False_Northing',3175000.0],PARAMETER['Central_Meridian',-97.0],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',47.5],UNIT['Meter',1.0]]")
        arcpy.ProjectRaster_management(inRaster, "projected\\"+outRaster, "PROJCS['WGS_1984_Web_Mercator_Auxiliary_Sphere',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator_Auxiliary_Sphere'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],PARAMETER['Auxiliary_Sphere_Type',0.0],UNIT['Meter',1.0]]", "NEAREST", "50000", "", "", "PROJCS['RCM3',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Stereographic_North_Pole'],PARAMETER['false_easting',3475000.0],PARAMETER['false_northing',7475000.0],PARAMETER['central_meridian',263.0],PARAMETER['standard_parallel_1',60.0],UNIT['Meter',1.0]]")
        #resultNCEP
        inRaster = ""+mid['fileName']+"_resultNCEP.tif"
        arcpy.AddMessage("inRaster: " + inRaster) 
        outRaster = ""+mid['fileName']+"_resultNCEPWGS84.tif"
        inPrjFile = inRaster
        prjFile = r"C:\\Data\\NEMAC\\Projects\\NCA\\Scripting\\ArcPyGDAL\\proj_files\\RCM3.prj"
        arcpy.DefineProjection_management(inPrjFile, prjFile)
        #arcpy.ProjectRaster_management(inRaster, "projected\\"+outRaster, "PROJCS['WGS_1984_Web_Mercator',GEOGCS['GCS_WGS_1984_Major_Auxiliary_Sphere',DATUM['D_WGS_1984_Major_Auxiliary_Sphere',SPHEROID['WGS_1984_Major_Auxiliary_Sphere',6378137.0,0.0]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator'],PARAMETER['false_easting',0.0],PARAMETER['false_northing',0.0],PARAMETER['central_meridian',0.0],PARAMETER['standard_parallel_1',0.0],UNIT['Meter',1.0]]", "NEAREST", "50000", "WGS_1984_Major_Auxiliary_Sphere_To_WGS_1984", "", "PROJCS['RCM3',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',3925000.0],PARAMETER['False_Northing',3175000.0],PARAMETER['Central_Meridian',-97.0],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',47.5],UNIT['Meter',1.0]]")
        arcpy.ProjectRaster_management(inRaster, "projected\\"+outRaster, "PROJCS['WGS_1984_Web_Mercator_Auxiliary_Sphere',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator_Auxiliary_Sphere'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],PARAMETER['Auxiliary_Sphere_Type',0.0],UNIT['Meter',1.0]]", "NEAREST", "50000", "", "", "PROJCS['RCM3',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Stereographic_North_Pole'],PARAMETER['false_easting',3475000.0],PARAMETER['false_northing',7475000.0],PARAMETER['central_meridian',263.0],PARAMETER['standard_parallel_1',60.0],UNIT['Meter',1.0]]")
    for mid in modelsWRFG:   
        #result1
        inRaster = ""+mid['fileName']+"_result1.tif"
        arcpy.AddMessage("inRaster: " + inRaster) 
        outRaster = ""+mid['fileName']+"_result1WGS84.tif"
        inPrjFile = inRaster
        prjFile = r"C:\\Data\\NEMAC\\Projects\\NCA\\Scripting\\ArcPyGDAL\\proj_files\\WRFG.prj"
        arcpy.DefineProjection_management(inPrjFile, prjFile)
        arcpy.ProjectRaster_management(inRaster, "projected\\"+outRaster, "PROJCS['WGS_1984_Web_Mercator_Auxiliary_Sphere',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator_Auxiliary_Sphere'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],PARAMETER['Auxiliary_Sphere_Type',0.0],UNIT['Meter',1.0]]", "NEAREST", "50000", "NAD_1983_To_WGS_1984_1", "", "PROJCS['NWRFG',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',3325000.0],PARAMETER['False_Northing',2700000.0],PARAMETER['Central_Meridian',-97.0],PARAMETER['Standard_Parallel_1',30.0],PARAMETER['Standard_Parallel_2',60.0],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',47.5],UNIT['Meter',1.0]]")
        #result2
        inRaster = ""+mid['fileName']+"_result2.tif"
        arcpy.AddMessage("inRaster: " + inRaster) 
        outRaster = ""+mid['fileName']+"_result2WGS84.tif"
        inPrjFile = inRaster
        prjFile = r"C:\\Data\\NEMAC\\Projects\\NCA\\Scripting\\ArcPyGDAL\\proj_files\\WRFG.prj"
        arcpy.DefineProjection_management(inPrjFile, prjFile)
        arcpy.ProjectRaster_management(inRaster, "projected\\"+outRaster, "PROJCS['WGS_1984_Web_Mercator_Auxiliary_Sphere',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator_Auxiliary_Sphere'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],PARAMETER['Auxiliary_Sphere_Type',0.0],UNIT['Meter',1.0]]", "NEAREST", "50000", "NAD_1983_To_WGS_1984_1", "", "PROJCS['NWRFG',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',3325000.0],PARAMETER['False_Northing',2700000.0],PARAMETER['Central_Meridian',-97.0],PARAMETER['Standard_Parallel_1',30.0],PARAMETER['Standard_Parallel_2',60.0],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',47.5],UNIT['Meter',1.0]]")
        #resultNCEP
        inRaster = ""+mid['fileName']+"_resultNCEP.tif"
        arcpy.AddMessage("inRaster: " + inRaster) 
        outRaster = ""+mid['fileName']+"_resultNCEPWGS84.tif"
        inPrjFile = inRaster
        prjFile = r"C:\\Data\\NEMAC\\Projects\\NCA\\Scripting\\ArcPyGDAL\\proj_files\\WRFG.prj"
        arcpy.DefineProjection_management(inPrjFile, prjFile)
        arcpy.ProjectRaster_management(inRaster, "projected\\"+outRaster, "PROJCS['WGS_1984_Web_Mercator_Auxiliary_Sphere',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator_Auxiliary_Sphere'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],PARAMETER['Auxiliary_Sphere_Type',0.0],UNIT['Meter',1.0]]", "NEAREST", "50000", "NAD_1983_To_WGS_1984_1", "", "PROJCS['NWRFG',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',3325000.0],PARAMETER['False_Northing',2700000.0],PARAMETER['Central_Meridian',-97.0],PARAMETER['Standard_Parallel_1',30.0],PARAMETER['Standard_Parallel_2',60.0],PARAMETER['Scale_Factor',1.0],PARAMETER['Latitude_Of_Origin',47.5],UNIT['Meter',1.0]]")        

#2. Define projections and assign to raster files----------------------------------------------------    
def Shift():
    # # Local variables:
    # mm5i_ccsm_cdd_mean_result1WGS84_tif = "C:\\Data\\NEMAC\\Projects\\NCA\\Scripting\\ArcPyGDAL\\output_files\\projected\\mm5i_ccsm_cdd_mean_result1WGS84.tif"
    ReferenceRaster = "C:\\Data\\NEMAC\\Projects\\NCA\\Scripting\\ArcPyGDAL\\output_files\\projected\\crcm_ccsm_cdd_mean_result1WGS84.tif"
    # mm5i_ccsm_cdd_mean_result1WG = "C:\\Data\\NEMAC\\Projects\\NCA\\Scripting\\ArcPyGDAL\\output_files\\projected\\shifted\\test.tif"
    # # Process: Shift
    # # Shift_management (in_raster, out_raster, x_value, y_value, {in_snap_raster})
    # arcpy.Shift_management(mm5i_ccsm_cdd_mean_result1WGS84_tif, mm5i_ccsm_cdd_mean_result1WG, "1", "1", crcm_ccsm_cdd_mean_result1WGS84_tif)
    for mid in modelsMM5I:     
        inRaster = ""+mid['fileName']+"_result1WGS84.tif"
        arcpy.AddMessage("inRaster: " + inRaster) 
        outRaster = ""+mid['fileName']+"_result1WGS84Shifted.tif"
        arcpy.Shift_management("projected\\"+inRaster, "projected\\shifted\\"+outRaster, "1", "1", ReferenceRaster)
    
        
        
#----------------------------------------------------------------------------------------------------


#program control here ---------------------------------------------------------------
#Clear out old files
#files = glob.glob('C:/data/NEMAC/Projects/NCA/Scripting/ArcPyGDAL/output_files/*')
#for f in files:
#    os.remove(f)

arcpy.env.workspace = "C:/data/NEMAC/Projects/NCA/Scripting/ArcPyGDAL/output_files"
mxd = arcpy.mapping.MapDocument("CURRENT")

#arcpy.AddMessage("RUNNING NetCDFToRaster:") 
#NetCDFToRaster()
#arcpy.AddMessage("RUNNING ProjectRaster:") 
#ProjectRaster()
arcpy.AddMessage("RUNNING Shift:") 
Shift()

#---------------------------------------------------------------------------------------
    
    
del mxd
arcpy.AddMessage("Done!")





