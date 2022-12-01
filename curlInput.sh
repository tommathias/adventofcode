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
COOKIE="session=53616c7465645f5f8a935e9d049a52ddbc50a9a30523ad241643d073dda2effb3279faa578e81a30168c8fb8282741af9855c570c0f4f90693569a93052e7348"
curl $URL --cookie $COOKIE > "$OUTPATH/input.txt"