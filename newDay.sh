#!/usr/bin/env bash
set -o errexit
set -o nounset
set -o pipefail

YEAR="${1}"
DAYIN="${2}"
DAY=$DAYIN

if [ ${#DAY} = "1" ]; then
  DAY="0$DAY"
  #echo "day: $DAY"
fi

git checkout -b "${YEAR}-${DAY}"
DIR="${YEAR}/${DAY}"
mkdir $DIR
. curlInput.sh $YEAR $DAYIN
touch "${DIR}/test.txt"
cp template.py "${DIR}"
cd $DIR
