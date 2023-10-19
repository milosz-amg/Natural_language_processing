#!/bin/bash
cars=""

while read -r linia
do
  if [ "$linia" = "EOF" ]; then
    break
  fi
  zmienna="${zmienna}${linia}$"
done
champion=$(sort -t',' -k3 -n -r | head -n 1)
echo $champion