#!/bin/bash

sudo killall gpspipe
if [ "$?"-ne 0]; then echo "command failed"; exit 1; fi

exit 0
