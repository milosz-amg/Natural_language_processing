#!/bin/bash
tmp_file=$(mktemp)

while IFS= read -r line; do
    echo "$line" >> "$tmp_file"
    ((i=i+1))
done
# Pobierz tekst ze standardowego wejścia (możesz zmienić na odczyt z pliku)
tr '[:punct:]' ' ' < tmp_file > tmp_file
cat $tmp_file

