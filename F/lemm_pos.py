# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# W FOLDERZE Z PLIKIEM MAXMATCH.PY NALEZY UMIESCIC SLOWNIK, JEST ZA DUZY BY PRZESYLAC GO PRZEZ TEAMSA   #
# NAZWE PLIKU ZDEFINIOWANO W ZMIENNEJ GLOBALNEJ PONIŻEJ                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

POLIMORF_PATH= "PoliMorf-0.6.7.tab"

def load_polimorf_dict(file_path):
    dictionary_data = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            components = line.split()
            word = components[0]
            dictionary_data[word] = line.strip()
    return dictionary_data

def search_word(dictionary, word):
    return dictionary.get(word, "Nie znaleziono takiego słowa")

def generate_tokens(input_string):
    tokens = input_string.replace(':', ' : ').split()
    tokens = [token for token in tokens if token != ':']
    return tokens

# ['pójdę', 'pójść', 'fin', 'sg', 'pri', 'perf', 'pospolita']
#   word     steam    pos    ...    ...     ...     ...

# Mogłem dać formy skrótowe, ale estetyczniej jest pełnym słowem po polsku :))
# Interpretacja systemu znaczników morfologicznych zaczerpnięta z:
# https://bcpw.bg.pw.edu.pl/Content/4598/tekst_pol.pdf
def POS_tagger(tokens):
    pos_dict={
        "subst":"rzeczownik",
        "depr":"rzeczownik deprecjatywny",
        "num":"liczebnik główny",
        "numcol":"liczebnik zbiorowy",
        "adj":"przymiotnik",
        "adja":"przymiotnik przyprzymiotnikowy",
        "adjp":"przymiotnik poprzyimkowy",
        "adv":"przysłówek",
        "ppron12":"zaimek nietrzecioosobowy",
        "ppron3":"zaimek trzecioosobowy",
        "siebie":"zaimek siebie",
        "fin":"forma nieprzeszła",
        "bedzie":"forma przyszła być",
        "aglt":"aglutynant być",
        "praet":"pseudoimiesłów",
        "impt":"rozkaźnik ",
        "imps":"bezosobnik",
        "inf":"bezokolicznik ",
        "pcon":"im. przys. współczesny",
        "pant ":"im. przys. uprzedni",
        "ger":"odsłownik",
        "pact":"im. przym. czynny",
        "ppas":"im. przym. bierny",
        "winien":"winien",
        "pred":"predykatyw",
        "prep":"przyimek",
        "conj":"spójnik",
        "qub ":"kublik",
        "xxs ":"ciało obce nominalne",
        "xxx":"ciało obce luźne",
        "ign":"forma nierozpoznana",
        "interp":"interpunkcja",
    }
    return pos_dict[tokens[2]]

def lemmatizer(tokens):
    return tokens[1]

if __name__ == "__main__":
    print("Ładowanie słownika...")
    dictionary_data = load_polimorf_dict(POLIMORF_PATH)
    # word = "wykopała"
    word = input("Podaj słowo do lematyzacji i postagging'u: ")
    search_result = search_word(dictionary_data, word)
    tokens = generate_tokens(search_result)
    # print(tokens)
    print("Lemat: ",lemmatizer(tokens))
    print("POS: ",POS_tagger(tokens))

    
