#!/bin/bash
n=10
m=20
declare -a lines

while IFS= read -r line; do
    lines+=("$line")
done

for ((i = n-1; i < m; i++)); do
    echo "$((i+1)): ${lines[i]}"
done

# ./C04.sh < linie.in