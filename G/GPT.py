import spacy

# Załaduj model dla języka polskiego
nlp = spacy.load("pl_core_news_sm")

def okresl_tryb_czasownika(tekst):
    # Przetwórz zdanie
    doc = nlp(tekst)

    # Wypisz czasowniki i ich tryby
    for token in doc:
        if token.pos_ == "VERB":
            print(f"Czasownik: {token.text}, Tryb: {token.morph.get('VerbForm', 'nieznany')}")

# Przykładowe użycie:
zdanie = "Oni jutro pojadą na wycieczkę."

okresl_tryb_czasownika(zdanie)
