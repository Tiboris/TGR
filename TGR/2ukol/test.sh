#!/bin/bash
for IN in `ls ./tests/ | grep $1 | grep in`; do
    OUT="`echo "$IN" | cut -d "." -f 1`.out"
    ./$1 < ./tests/$IN | diff -u ./tests/$OUT -
done
