import string
from collections import Counter

def charFrequency(sentence):
    return sorted([tuple([char, sentence.count(char)]) for char in sorted(set(sentence))], key=lambda x: x[1], reverse=True)

print(charFrequency("Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."))