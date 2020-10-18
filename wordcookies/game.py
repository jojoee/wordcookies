import pickle
from typing import List, Dict, Set
from itertools import permutations
import re

# init Word Cookies
model_path = "./wordcookies/all_words.pickle"
all_words = pickle.load(open(model_path, "rb"))
print({"n": len(all_words), "example": list(all_words)[:10]})


def clean(inp: str) -> List[str]:
    """
    Clean an input
    - only alphabet
    - convert to lowercase
    - sort
    - make it list

    :param inp:
    :return:
    """
    inp = re.sub("[^a-zA-Z]+", "", inp)  # only alphabet
    inp = inp.lower()  # force lowercase
    chars = sorted(list(inp))  # make it list and sort

    return chars


def get_possible_answers(word_set: Set, chars: List[str]) -> List[str]:
    """
    Get possible answers

    :param word_set:
    :param chars:
    :return:
    """
    answers = []

    # proceed
    # TODO: 2, can be variable
    for n in range(2, len(chars) + 1):
        s = "".join(chars)

        print("s", s)

        items = permutations(s, n)  # list of  tuple
        items = ["".join(map(str, item)) for item in items]  # make it list of string
        items = list(set(items))  # make it unique, e.g. "local" can generate duplicate answer

        for item in items:
            if item in word_set:
                answers.append(item)

    return answers


def group(answers: List[str], n: int) -> Dict[int, List[str]]:
    """
    group an answers into group-of-word-length

    :param answers:
    :param n:
    :return:
    """
    answers.sort()  # sort

    # make it group to display
    answers_group = {}
    for n in range(2, n + 1):
        answers_group[n] = []

    for item in answers:
        answers_group[len(item)].append(item)

    print("answers_group", answers_group)

    return answers_group
