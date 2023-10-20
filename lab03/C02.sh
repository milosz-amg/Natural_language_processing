#!/bin/bash

#linie mozna podac recznie lub z pliku auta komenda ./C02.sh < auta.in
najszybsza_predkosc=0
najszybszy_samochod=""

while IFS=, read -r marka model predkosc; do
    if (( $(echo "$predkosc > $najszybsza_predkosc") )); then
        najszybsza_predkosc=$predkosc
        najszybszy_samochod="$marka $model"
    fi
done

echo "$najszybszy_samochod $najszybsza_predkosc"
