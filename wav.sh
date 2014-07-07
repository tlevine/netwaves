#!/bin/sh
set -e
infile="$1"
outfile="$2"
ffmpeg -i "$infile" -ar 8000 -ac 1 -acodec pcm_u8 "$outfile"
