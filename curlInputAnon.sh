#!/usr/bin/env bash
set -o errexit
set -o nounset
set -o pipefail

YEAR="${1}"
DAY="${2}"

#echo "year: $YEAR"
#echo "day: $DAY"

#days on server aren't always dd, set url, then rationalise to dd for my dirs
URL="https://adventofcode.com/$YEAR/day/$DAY/input"
echo "url: $URL"

if [ ${#DAY} = "1" ]; then
  DAY="0$DAY"
  #echo "day: $DAY"
fi
OUTPATH="./$YEAR/$DAY"

echo "outpath: $OUTPATH"
COOKIE="session={yoursessionhere}"
curl $URL --cookie $COOKIE > "$OUTPATH/input.txt"