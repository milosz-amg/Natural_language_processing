#!/bin/bash
#./C07.sh < pl.in
tmp_file=$(mktemp)
i=1

while IFS= read -r line; do
    echo "$i $line" >> "$tmp_file"
    ((i=i+1))
done

tac $tmp_file > odwrotnie.out
cat odwrotnie.out #wyswietlam na terminalu dla wygody
rm $tmp_file