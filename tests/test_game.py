from wordcookies import game
from typing import List, Dict
import json


# helper
# https://stackoverflow.com/questions/36420022/how-can-i-compare-two-ordered-lists-in-python/36420107
def is_list_equals(actual: List[any], expected: List[any]) -> bool:
    actual = sorted(actual)
    expected = sorted(expected)
    return actual == expected


# helper
# https://medium.com/@stschindler/comparing-nested-python-dictionaries-with-no-hassle-9ffe35ae076e
def is_same_dict(d1: Dict, d2: Dict) -> bool:
    dump1 = json.dumps(d1, sort_keys=True, indent=2)
    dump2 = json.dumps(d2, sort_keys=True, indent=2)
    return dump1 == dump2


class TestClean:
    def test_normal(self):
        assert is_list_equals(game.clean("word"), ['d', 'o', 'r', 'w'])
        assert is_list_equals(game.clean("apple"), ['a', 'e', 'l', 'p', 'p'])
        assert is_list_equals(game.clean("cookies"), ['c', 'e', 'i', 'k', 'o', 'o', 's'])
        assert is_list_equals(game.clean("superman"), ['a', 'e', 'm', 'n', 'p', 'r', 's', 'u'])

    def test_remove_space(self):
        assert is_list_equals(game.clean("word cookies"), ['c', 'd', 'e', 'i', 'k', 'o', 'o', 'o', 'r', 's', 'w'])
        assert is_list_equals(game.clean("thai baht"), ['a', 'a', 'b', 'h', 'h', 'i', 't', 't'])

    def test_only_alphabet_is_allowed(self):
        assert is_list_equals(game.clean("123w4or/d+* 9"), ['d', 'o', 'r', 'w'])

    def test_order(self):
        assert is_list_equals(game.clean("word"), ['d', 'o', 'r', 'w'])

    def test_convert_to_lowercase(self):
        assert is_list_equals(game.clean("WoRD"), ['d', 'o', 'r', 'w'])


class TestGetPossibleAnswers:
    def test_normal(self):
        # none match
        word_set = {'milk', 'non', 'wood'}
        word = 'mile'
        assert is_list_equals(game.get_possible_answers(word_set, game.clean(word)), [])

        # 3 chars match
        word_set = {
            'co', 'eo', 'kk', 'ae',
            'ceo', 'eco', 'seo', 'abc', 'ahf',
        }
        word = 'ceo'
        assert is_list_equals(game.get_possible_answers(word_set, game.clean(word)), [
            'eo', 'co',
            'ceo', 'eco',
        ])

        # 7 chars match
        word_set = {
            'co', 'so', 'kk', 'ae',
            'ceo', 'eco', 'seo', 'abc', 'ahf',
            'cook', 'sick', 'sock', 'anvc',
            'cokes', 'fives',
            'cookie', 'ancjkq',
            'cookies', 'popular'
        }
        word = 'cookies'
        assert is_list_equals(game.get_possible_answers(word_set, game.clean(word)), [
            'co', 'so',
            'ceo', 'eco', 'seo',
            'cook', 'sick', 'sock',
            'cokes',
            'cookie',
            'cookies',
        ])


class TestGroup:
    def test_normal(self):
        n = 7
        answers = [
            'co', 'so',
            'ceo', 'eco', 'seo',
            'sock', 'cook', 'sick',
            'cokes',
            'cookie',
            'cookies',
        ]
        assert is_same_dict(game.group(answers, n), {
            2: ['co', 'so'],
            3: ['ceo', 'eco', 'seo'],
            4: ['cook', 'sick', 'sock'],
            5: ['cokes'],
            6: ['cookie'],
            7: ['cookies'],
        })
