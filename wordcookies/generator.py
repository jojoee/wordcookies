import nltk
from nltk.corpus import words, stopwords, wordnet
import requests
import pickle
from urllib.request import urlopen
from typing import List


def get_prepared_words() -> List[str]:
    # init
    nltk.download('words')
    nltk.download('stopwords')
    nltk.download('wordnet')

    # prepare
    prepared_words = []
    r = requests.get(
        'https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json'
    )
    dwyl_words = list(r.json().keys())
    ahmadly_words = list(
        pickle.load(
            urlopen(
                "https://github.com/jojoee/WordCookiesCheat/blob/master/all_words.pickle?raw=true"
            )))
    wordnet_words = list(wordnet.words())

    # proceed
    prepared_words = stopwords.words() + words.words(
    ) + wordnet_words + ahmadly_words
    prepared_words = [
        word.lower() for word in prepared_words if word.isalpha()
    ]
    prepared_words = list(set(prepared_words))

    # sort
    prepared_words.sort()

    # debug
    print("stopwords size: %d" % len(stopwords.words()))
    print("words size: %d" % len(words.words()))
    print("wordnet size: %d" % len(list(wordnet.words())))
    print("dwyl_words size: %d" % len(dwyl_words))
    print("prepared_words size: %d" % len(prepared_words))

    return prepared_words


def generate_dict(model_path: str = "") -> None:
    prepared_words = get_prepared_words()

    # save as "set" for search performance
    model_path = model_path
    pickle.dump(set(prepared_words), open(model_path, 'wb'))
