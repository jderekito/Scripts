#!/bin/bash

for f in *.shp
do
    tablename=${f%.shp}
    shp2pgsql -s 4326 "$f" public."$tablename" | psql -d grownc -U geo1
done
