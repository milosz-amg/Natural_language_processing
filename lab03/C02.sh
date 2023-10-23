#!/bin/bash

#linie mozna podac recznie lub z pliku auta komenda ./C02.sh < auta.in
max_predkosc=0
najszybszy_samochod=""

while IFS=, read -r marka model predkosc; do
    if (( $(echo "$predkosc > $max_predkosc") )); then
        max_predkosc="$predkosc"
        najszybszy_samochod="$marka $model"
    fi
done

# echo "$najszybszy_samochod"
echo $max_predkosc
