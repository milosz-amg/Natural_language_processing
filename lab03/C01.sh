#!/bin/bash
read numbers
#numery podajemy w jednej lini i sa obcinane spacje i znak konca lini
numbers=$(echo $numbers | tr ' ' '\n')
#sortuje -n wartosc, numeryczna, -r malejaco, uniq bez powtorzen
sorted_numbers=$(echo "$numbers" | sort -n -r -u)
echo $sorted_numbers