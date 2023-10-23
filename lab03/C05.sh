#!/bin/bash

tmp_file=$(mktemp)

while IFS= read -r line; do
    echo "$line" >> "$tmp_file"
done

echo "cz,sz count:" 
grep -io "cz\|sz" "$tmp_file" | wc -l
rm $tmp_file

# ./C05.sh < linie.in