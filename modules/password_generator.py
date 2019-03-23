from nltk.corpus import wordnet as wn 
import random

def get_word_list(part_of_speach):
    word_list = []
    for synset in list(wn.all_synsets(part_of_speach))[:1000]:
        for l in synset.lemmas():
            word_list.append(l.name())
    return word_list

print("Password = " + get_word_list('n')[random.randrange(900)] + get_word_list('a')[random.randrange(900)] + str(random.randint(100,900)))