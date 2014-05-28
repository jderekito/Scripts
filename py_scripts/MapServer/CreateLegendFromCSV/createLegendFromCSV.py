#! /usr/bin/python

import Image, ImageDraw, os
import ImageFont, csv

fontsize = 17  # starting font size
font = ImageFont.truetype("arial.ttf", fontsize)
fontBold = ImageFont.truetype("arialbd.ttf", fontsize)
os.chdir('C:/Data/PhD/Teaching/GISProgramming/ArcGIS/CreateLegendFromCSV')

#1. First determine the canvas height by reading in the CSV values
vals = csv.DictReader(open("EVT.csv", 'rb'), delimiter=',', quotechar='"')
i = 0
for line in vals:	
	i = i + 1
	print line['cat']

cavasHeightY = i*20+60
recBottomLeftY = 10
recTopRightY = 30
textY = 12

#2. Now create the cavas
# PIL create an empty image and draw object to draw on
# legendCanvas = Image.new('RGBA', (300, cavasHeightY),(255, 255, 255))#white
legendCanvas = Image.new('RGBA', (900, cavasHeightY))#transparent
draw = ImageDraw.Draw(legendCanvas)

#3. Title
draw.text((10, textY), "LANDFIRE Existing Veg Type", fill="black", font=fontBold)
recBottomLeftY = recBottomLeftY + 20
recTopRightY = recTopRightY + 20
textY = textY + 20

	
#4. Now loop through the CSV creating the legend items on the Canvas
# do the PIL image/draw (in memory) drawings
# [ x, y, x, y ] or [ (x, y), (x, y) ]
# draw.text(position, string, options)
i = 0
vals = csv.DictReader(open("EVT.csv", 'rb'), delimiter=',', quotechar='"')
for line in vals:
	draw.rectangle((10, recBottomLeftY, 40, recTopRightY), fill=(int(line['r']), int(line['g']), int(line['b'])), outline="black")
	draw.text((45, textY), line['cat']+' - '+line['id'], fill="black", font=font)
	recBottomLeftY = recBottomLeftY + 20
	recTopRightY = recTopRightY + 20
	textY = textY + 20
	i = i + 1

filename = "EVTLegend.png"
legendCanvas.save(filename)
