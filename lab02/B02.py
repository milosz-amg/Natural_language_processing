import csv
import re

def check_pattern(chain):
    intiger_pattern = r'^[+-]?\d+$'
    # ^ poczatek slowa
    # [+-]? opcjonalny plus lub minus
    #  \d+ jedna lub więcej cyfr
    # $ koniec slowa
    if re.match(intiger_pattern,chain):
        return True
    else:
        return False

with open('./B02input.csv') as f:
    csvreader = csv.reader(f, delimiter=';')
    f_correct = 0
    for row in csvreader:
        # zakładam, że w kolumnie 1 też może być liczba, gdyż jest ona dowolnym ciągiem znaków
        # ale wykluczam wszystkie znaki biale
        if re.match(r'\S',row[0]) and check_pattern(row[1])==True and check_pattern(row[2])==True:
            print(row,' - OK')
        else:
            print(row,' - BLEDNE DANE')
            f_correct = 1

    if f_correct == 1:
        print("\nPlik zawiera bledne dane :((")
    else:
        print("\nCały plik jest poprawny :))")

    