#!/bin/bash

ffmpeg -i "$1" -f segment -segment_time 8 -c copy segment/temp%03d.mp3
