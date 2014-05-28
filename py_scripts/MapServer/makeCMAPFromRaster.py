#! /usr/bin/python
import osgeo
import osgeo.gdal, osgeo.gdalconst
import os, sys, time
import struct
import numpy

numpy.set_printoptions(threshold='nan')
osgeo.gdal.AllRegister()

driver = osgeo.gdal.GetDriverByName('HFA')
driver.Register()

# os.chdir('C:/Data/NEMAC/Projects/FCAV/CarbonStock')

ds = osgeo.gdal.Open('carbon_8bit_ag_mg_ha.img', osgeo.gdal.GA_ReadOnly)
if ds is None:
    print 'Could not open file'
    sys.exit(1)

cols = ds.RasterXSize
rows = ds.RasterYSize
bands = ds.RasterCount
print "Columns: " + str(cols)
print "Rows: " + str(rows)	

#This is a way to go through a given raster band 
#one-by-one as an array by row, getting all of the columns for
#a given row
rowNum = 0
for r in range(rows):
    data = ds.GetRasterBand(1).ReadAsArray(0, r, cols, 1)
    print "row :" + str(rowNum)
    print str(data)
    print str(len(data[0]))
    colNum = 0
    for i in data[0]:
        print "col :" + str(colNum)
        print str(i)
        # fo.write(GetTypeFromID(str(i))+"\n")
        colNum=colNum+1
    rowNum=rowNum+1
#fo.close()
