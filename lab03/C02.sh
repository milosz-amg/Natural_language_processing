#!/bin/bash

# Deklaracja tablicy do przechowywania danych
declare -a car_data

# Pętla odczytująca dane ze standardowego wejścia
while IFS= read -r line; do
  car_data+=("$line")
done

# Sortujemy dane według prędkości (3. kolumny, rozdzielone przecinkiem)
sorted_data=($(printf "%s\n" "${car_data[@]}" | tr ',' ' ' | sort -k 3 -n -r | tr ' ' ',' | head -n 1))

# Wyświetlamy posortowane wyniki
for car in "${sorted_data[@]}"; do
  echo "$car"
done
