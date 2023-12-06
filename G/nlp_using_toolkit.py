import spacy

# # # # # # # # # # # # #
# spacy version: 3.7.2  #
# # # # # # # # # # # # #

def tokenize(doc):
    tokens=[]
    for token in doc:
        tokens.append(token)
    return tokens

def is_command(tokens):
    guar=0
    sentence=[token.text for token in tokens]
    for token in tokens:
        print("> ",token.text, token.pos_, token.morph.get('VerbForm', 'nieznany'))
        if token.tag_ == "IMPT" or token.tag_ == "PRAET": #IMPT / PRAET - tryb rozkazujący czasownika - token.tag_
            command_verb=token.text
            guar=1

    if guar != 0:
        print(f'akcja: {command_verb}')    
        for i in range(len(sentence)-1):
            if sentence[i] != command_verb:
                sentence[i]=""
            else:
                break
        print("obiekt:"," ".join(sentence[1:]))
    else:
        print("KONIEC")
    

if __name__ == "__main__":
    print("Ładowanie toolkitu spacy...")
    nlp = spacy.load("pl_core_news_sm")
    sentence = input("Podaj zdanie wejściowe: ")
    # sentence = "zmniejsz głośność odtwarzacza muzyki"
    doc = nlp(sentence)
    tokens=tokenize(doc)
    is_command(tokens)