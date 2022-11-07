#!/bin/bash
yt-dlp -x --audio-format mp3 --output "fd/%(uploader)s%(title)s.%(ext)s" "$1"
