dictionary = {
    "jabłko": "apple",
    "gruszka": "pear",
    "banan": "banana",
    "winogrono": "grape",
    "brzoskwinia": "peach",
    "pomarańcza":"orange",
    "wiśnia":"cherry",
    "truskawka":"strawberry",
    "jeżyna":"blackberry,",
    "smoczy owoc":"dragon fruit",
}

while(1):
    polish_word = input('podaj nazwe owocu po polsku: ')
    if polish_word in dictionary:
        print(" ",polish_word," to po angielski ","\"", dictionary[polish_word],"\"")
    else:
        print(" ","niestety nie znam takiego slowa, podaj inne:")
