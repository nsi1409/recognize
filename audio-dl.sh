#!/bin/bash
echo $1
youtube-dl -x --audio-format mp3 $1
