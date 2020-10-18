from wordcookies import game
from pprint import pprint


def proceed(word: str) -> None:
    chars = game.clean(word)
    print(chars)
    answers = game.get_possible_answers(chars)
    g = game.group(answers)
    pprint(g, width=80)


def main():
    while True:
        try:
            word = input("\nenter chars: ")
            proceed(word)

        except KeyboardInterrupt:
            print("\nbye !")
            exit(0)


if __name__ == '__main__':
    main()
