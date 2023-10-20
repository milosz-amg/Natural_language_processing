#!/bin/bash
# ./C01.sh < liczby.in
read numbers
numbers=$(echo $numbers | tr ' ' '\n')
sorted_numbers=$(echo "$numbers" | sort -n -r -u)
echo $sorted_numbers