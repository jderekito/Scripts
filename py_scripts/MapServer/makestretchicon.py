#!/usr/bin/env python

import gd, os, cStringIO, urllib2, sys, getopt

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

def usage():
    print """NAME
    makestretchicon - generate a legend icon for a stretched colormap

SYNOPSIS
    makeicon [ OPTIONS ] OUTPUT_FILE

DESCRIPTION
    OUTPUT_FILE should be the name of a PNG image to be written, complete
    with ".png" suffix.

OPTIONS
    -L R,G,B, --cMin=R,G,B
        Color to use for low end of range

    -H R,G,B, --cMax=R,G,B
        Color to use for high end of range

    -W N, --iconwidth=N 
        Set the overall width of the generated icon to N pixels.  The default
        is 275.  (The height of the icon is computed automatically based on
        other parameters.)

    -p N, --padding=N
        Include a padding amount of N pixels of white space on all 4 sides of
        the icon.  The default padding is 0.

    -h N, --colorbarheight=N
        Use a height of N pixels for the color bar drawn inside the icon; the
        default is 20.

    -f N, --fontsize=N 
        Use a font size of N points for the text in the icon; the default is 12.

    -t STRING, --title=STRING
        Use the given STRING as the title text in the icon.  The default is no title.

    -c STRING, --caption=STRING
        Use the given STRING as the caption text in the icon (under the color bar).
        The default is no caption.

    -l STRING, --leftlabel=STRING 
        Use the given STRING as the label for the left end of the color bar.  The default
        is to use the first (lowest) pixel value in the COLORMAP_FILE.

    -r STRING, --rightlabel=STRING
        Use the given STRING as the label for the right end of the color bar.  The default
        is to use the last (highest) pixel value in the COLORMAP_FILE.

    -T N, --tickheight=N
        Use a height of N pixels for the tick marks drawn at the left and right ends
        of the color bar.  The default is 5.

    -q, --quiet
        Quiet mode; suppresses the output message indicating that the PNG file has been written.

EXAMPLE
	./makestretchicon.py -c "Carbon Stock 2009" -T 0 -W 128 -h 15 -f 8 -L 0,0,0 -H 222,247,239 -l low -r high Carbon09.png

AUTHOR
    Mark Phillips
    mphillip@unca.edu
    Fri Sep 17 15:12:21 2010
"""
    sys.exit(-1)


def ir(x):
    return int(round(x))

###
### The following line should set the FONT variable to the name of a .ttf file
### containing the font to be used for text in the icon.  The file should
### be located in the current directory when this program is run.
###
FONT = "FreeSans.ttf"

###
### This line tells the GD library (imported above) to look for font files
### in the current directory:
###
os.environ["GDFONTPATH"] = "."

###
### A utility function to compute the width and height of a string
### using a given font and pointsize.
###
def stringsize(font, pointsize, string):
    im = gd.image((100,100))
    rect = im.get_bounding_rect(font, pointsize, 0, (50,50), string)
    width = rect[2] - rect[0]
    height = rect[1] - rect[7]
    return [width,height]

###
### Default values:
###
iconWidth      = 275
colorBarHeight =  30
padding        =  10
fontSize       =  12
tickHeight     =   5
tickLabelPad   =   5
title          = None
leftLabel      = None
rightLabel     = None
caption        = None
quietMode      = False

###                                                                                                                                
### Process command line arguments and filenames                                                                                   
###                                                                                                                                
opts, args = getopt.getopt(sys.argv[1:],
                           "L:H:W:p:h:f:t:l:r:T:c:q",
                           ["cMin=", "cMax=", "iconwidth=", "padding=", "colorbarheight=", "fontsize=", "title=", "leftlabel=", "rightlabel=", "tickheight=",
                            "caption=",
                            "quiet"]
                           )
if (len(args) != 1): usage()

outputFile = args[0]
for opt, arg in opts:
    if opt in ('-W', '--iconwidth'):
        iconWidth = int(arg)
    elif opt in ('-L', '--cMin'):
        colorLow = arg.split(r',')
    elif opt in ('-H', '--cMax'):
        colorHigh = arg.split(r',')
    elif opt in ('-p', '--padding'):
        padding = int(arg)
    elif opt in ('-h', '--colorbarheight'):
        colorBarHeight = int(arg)
    elif opt in ('-f', '--fontsize'):
        fontSize = float(arg)
    elif opt in ('-t', '--title'):
        title = arg
    elif opt in ('-c', '--caption'):
        caption = arg
    elif opt in ('-l', '--leftlabel'):
        leftLabel = arg
    elif opt in ('-r', '--rightlabel'):
        rightLabel = arg
    elif opt in ('-T', '--tickheight'):
        tickHeight = float(arg)
    elif opt in ('-q', '--quiet'):
        quietMode = True

###
### Load the color map from the input file
###
#colorMap = ColorMap(inputFile)
colorInterp = ColorInterp(0, 1,
                          colorLow[0], colorLow[1], colorLow[2],
                          colorHigh[0], colorHigh[1], colorHigh[2])

###
### Set left and/or right label strings from the color map,
### if they weren't specified on the command line
###
if leftLabel == None:
    leftLabel = "???"
if rightLabel == None:
    rightLabel = "???"

###
### Compute the vertical height needed for text labels; this is
### the max height of the left label, right label, and title.
### This code is probably overkill, since most likely all three
### strings will have the same height.  But better safe than sorry.
###
labelHeight = 0
if leftLabel != None:
    rect = stringsize(FONT, fontSize, leftLabel)
    if (rect[1] > labelHeight): labelHeight = rect[1]
if rightLabel != None:
    rect = stringsize(FONT, fontSize, rightLabel)
    if (rect[1] > labelHeight): labelHeight = rect[1]
if title != None:
    rect = stringsize(FONT, fontSize, title)
    if (rect[1] > labelHeight): labelHeight = rect[1]


###
### Compute the vertical height needed for the caption.
###
captionHeight = 0
if caption != None:
    rect = stringsize(FONT, fontSize, caption)
    captionHeight = rect[1]


###
### Compute the total height of the icon image, based on everything else:
###
iconHeight = ir(padding + labelHeight + tickLabelPad + tickHeight + colorBarHeight + tickLabelPad + tickHeight + captionHeight + padding)

###
### Compute the width to be used for the color bar (full width of icon, minus padding):
###
colorBarWidth  = iconWidth - 2 * padding

###
### Create a GD image object
###
im = gd.image((iconWidth, iconHeight))

###
### Allocate some colors for drawing in it
###
white = im.colorAllocate((255, 255, 255))
black = im.colorAllocate((  0,   0,   0))

###
### Fill it with white
###
im.rectangle((0,0),(iconWidth,iconHeight),white)

###
### Draw the color bar, by drawing one vertical line at a time from
### the left edge to the right edge, using colors from the ColorMap.
###
colorBarXOffset = (iconWidth - colorBarWidth) / 2
colorBarYOffset = padding + labelHeight + tickLabelPad + tickHeight;
for x in range(0,colorBarWidth-1):
    color = colorInterp.interp(float(x)/float(colorBarWidth-1))
    gdColor = im.colorAllocate((ir(color[0]), ir(color[1]), ir(color[2])))
    px  = colorBarXOffset + x
    im.line((ir(px),ir(colorBarYOffset)),(ir(px),ir(colorBarYOffset+colorBarHeight)),gdColor)

###
### draw the left tick mark and label
###
labelY = colorBarYOffset-tickHeight-tickLabelPad
leftTickX = colorBarXOffset+1
if tickHeight > 0:
    im.line((leftTickX,colorBarYOffset),(leftTickX,colorBarYOffset-tickHeight),black)
im.string_ttf(FONT, fontSize, 0.0, (ir(leftTickX),ir(labelY)), leftLabel, black)

###
### draw the right tick mark and label (label is right-justified)
###
rightTickX = colorBarXOffset+colorBarWidth-2
if tickHeight > 0:
    im.line((rightTickX,colorBarYOffset),(rightTickX,colorBarYOffset-tickHeight),black)
rect = stringsize(FONT, fontSize, rightLabel)
im.string_ttf(FONT, fontSize, 0.0, (ir(rightTickX-rect[0]),ir(labelY)), rightLabel, black)

###
### draw the title, if any
###
if title != None:
    rect = stringsize(FONT, fontSize, title)
    x = iconWidth/2 - rect[0]/2
    im.string_ttf(FONT, fontSize, 0.0, (x, labelY), title, black)

###
### draw the caption, if any
###
captionY = colorBarYOffset + colorBarHeight + tickLabelPad + tickHeight + fontSize
if caption != None:
    rect = stringsize(FONT, fontSize, caption)
    x = iconWidth/2 - rect[0]/2
    im.string_ttf(FONT, fontSize, 0.0, (x, int(captionY)), caption, black)

###
### write the output (png) file
###
dir = os.path.dirname(outputFile)
if dir != '' and not os.path.exists(dir):
    os.mkdir(dir)
f=open(outputFile,"w")
im.writePng(f)
f.close()
if not quietMode: print "wrote file %s [%1d X %1d]" % (outputFile, iconWidth, iconHeight)
