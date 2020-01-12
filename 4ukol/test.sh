#!/bin/bash
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

for IN in `ls ./tests/ | grep parking | grep ".*\.in"`; do
    TEST="`echo "$IN" | cut -d "." -f 1`"
    OUT="$TEST.out"
    ./$1 < ./tests/$IN | diff -u ./tests/$OUT -
    if [[ $? -eq 0 ]]; then
        echo -e "${YELLOW}Test $TEST: ${GREEN}OK${NC}"
    else
        echo -e "${YELLOW}Test $TEST: ${RED}FAIL${NC}"
    fi
done
