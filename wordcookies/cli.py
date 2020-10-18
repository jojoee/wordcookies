from wordcookies import game
from pprint import pprint

while True:
    try:
        s = input("\nenter chars: ")
        chars = game.clean(s)
        print(chars)
        answers = game.get_possible_answers(chars)
        g = game.group(answers)
        pprint(g, width=80)

    except KeyboardInterrupt:
        print("\nbye !")
        exit(0)
