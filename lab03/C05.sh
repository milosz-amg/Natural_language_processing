#!/bin/bash

tmp_file=$(mktemp)

while IFS= read -r line; do
    echo "$line" >> "$tmp_file"
done

echo "cz,sz count:" 
grep -o "cz\|sz" "$tmp_file" | wc -l
rm $tmp_file

# ./C5.sh < linie.in