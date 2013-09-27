#!/bin/bash

for f in *.shp
do
   ogr2ogr -t_srs EPSG:4326 "./newproj/$f" "$f"
done
