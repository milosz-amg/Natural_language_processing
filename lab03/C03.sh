#!/bin/bash
n=123
declare -a lines

while IFS= read -r line; do
  lines+=("$line")
done

echo "${lines[n-1]}"

# ./C03.sh < linie.in
