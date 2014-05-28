#! /usr/bin/python

from osgeo import gdal, gdalconst
import os, sys, math
import optparse 


class ColorInterp:
    def __init__(self, xMin, xMax, rMin, gMin, bMin, rMax, gMax, bMax):
        self.xMin = float(xMin)
        self.rMin = float(rMin)
        self.gMin = float(gMin)
        self.bMin = float(bMin)
        xLen = float(xMax) - float(xMin)
        self.rFactor = ( float(rMax) - float(rMin) ) / float(xLen)
        self.gFactor = ( float(gMax) - float(gMin) ) / float(xLen)
        self.bFactor = ( float(bMax) - float(bMin) ) / float(xLen)
    def interp(self,x):
        return [float(round(self.rMin + (x - self.xMin) * self.rFactor)),
                float(round(self.gMin + (x - self.xMin) * self.gFactor)),
                float(round(self.bMin + (x - self.xMin) * self.bFactor))]



# ./makestretchcmap.py -N 10 -n 0 -x 100 --rgbMin 0,0,0 --rgbMax 255,255,255
# OR
# ./makestretchcmap.py -N 40 -a carbon_8bit_ag_mg_ha.img --rgbMin 222,247,239 --rgbMax 41,109,57 
# OR
# ./makestretchcmap.py -N 20 -x 30 -n 0 --rgbMin 222,247,239 --rgbMax 41,109,57 
#-------------------------------------------------------

#Change to working directory where raster data file is
os.chdir('C:/Data/NEMAC/Projects/FCAV/CarbonStock')

#Verify input args    
parser = optparse.OptionParser()
parser.add_option('-N', help='mandatory N', dest='N', type="string")
parser.add_option('-n', help='optional n', dest='min', type="string")
parser.add_option('-x', help='optional x', dest='max', type="string")
parser.add_option('-a', help='optional RASTERFILE', dest='RASTERFILE', type="string")
parser.add_option('--rgbMin', help='mandatory rgbMin e.g 0,10,100', dest='rgbMin', type="string")
parser.add_option('--rgbMax', help='mandatory rgbMax e.g 0,10,100', dest='rgbMax', type="string")
(opts, args) = parser.parse_args()

if opts.N is None:
   print "A mandatory param N is missing\n"
   parser.print_help()
   exit(-1)
else:
   N = opts.N



if opts.RASTERFILE is None:
    if opts.min is None:
       print "A mandatory param n is missing\n"
       parser.print_help()
       exit(-1)
    else:
       MIN = opts.min

    if opts.max is None:
       print "A mandatory param x is missing\n"
       parser.print_help()
       exit(-1)
    else:
       MAX = opts.max     
else:
   ds = gdal.Open(opts.RASTERFILE, gdal.GA_ReadOnly)
   MIN = ds.GetRasterBand(1).GetMinimum()
   MAX = ds.GetRasterBand(1).GetMaximum()
   
if opts.rgbMin is None:
   print "A mandatory param rgbMin e.g 0,10,100 is missing\n"
   parser.print_help()
   exit(-1)
else:
   rgbMin = opts.rgbMin        
   
if opts.rgbMax is None:
   print "A mandatory param rgbMax e.g 0,10,100 is missing\n"
   parser.print_help()
   exit(-1)
else:
   rgbMax= opts.rgbMax        
#-------------------------------------------------------
increment = (float(MAX)-float(MIN))/float(N)
i = float(MIN)
#fout = open("cout.cmap", "w")
rgbMinDict = rgbMin.split(",")
rgbMaxDict = rgbMax.split(",")
c = ColorInterp(MIN, MAX, rgbMinDict[0], rgbMinDict[1], rgbMinDict[2], rgbMaxDict[0], rgbMaxDict[1], rgbMaxDict[2])
while (i<=float(MAX)):
    print('CLASS')
    #print("\tEXPRESSION \""+str(int(i))+"\" ")
    print("\tEXPRESSION ([pixel] > "+str(int(i))+" AND [pixel] <= "+str(int(i + increment))+") ")
    colors = c.interp(i)
    print("\tCOLOR " + "\t"+str(int(colors[0])) + "\t"+str(int(colors[1])) + "\t"+str(int(colors[2])))
    print('END')
    i = i + increment
    #print str(i)

