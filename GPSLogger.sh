#!/bin/bash

sudo gpspipe -r -d -l -o /media/pi/DATA/data.`date +"%Y%m%d%h%m%s"`.nmea
if [ "$?"-ne 0]; then echo "command failed"; exit 1; fi

exit 0
