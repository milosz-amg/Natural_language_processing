import re

vulgarities = ['kurw','korw','jeba','pierdol','chuj','huj']

def find_vulgarities(sentence):
    pattern = r"(?:^|\s)(?:{})(?:$|\s)".format('|'.join(map(re.escape, vulgarities)))
    matches = re.findall(pattern, sentence, flags=re.IGNORECASE)
    return matches

sentence = "To jest przykład zdania z wulgaryzmami, takimi jak kurw, jeba, chuj i pierdol."
found_vulgarities = find_vulgarities(sentence)

if found_vulgarities:
    print("Znalezione wulgaryzmy:", found_vulgarities)
else:
    print("Brak wulgaryzmów w zdaniu.")
