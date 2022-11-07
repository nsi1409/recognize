#!/bin/bash

ffmpeg -i "$1" -f segment -segment_time 8 -c copy out%03d.mp3
