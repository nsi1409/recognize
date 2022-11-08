#!/bin/bash

mkdir segment/"$1"
ffmpeg -i fd/"$1" -f segment -segment_time 8 -c copy segment/"$1"/temp%03d.mp3
