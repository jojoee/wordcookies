import sys
from wordcookies import cli

USAGE = """wordcookies
Usage:
------
    $ wordcookies cli
    $ wordcookies cli --word="word"
    $ wordcookies cli --word="word" --exit

Available options are:
    -h, --help         Show this help
"""


def main():
    if sys.argv[1] == "cli" and len(sys.argv) >= 2:
        args = sys.argv[2:]

        word = ""
        is_exit = False

        # parsing
        for arg in args:
            if arg.startswith("--word"):
                word = str(arg.split("=", 1)[1])
            elif arg.startswith("--exit"):
                is_exit = True
            else:
                print("you are passing invalid argument", arg)
                sys.exit(0)

        if word:
            cli.proceed(word)
            if not is_exit:
                cli.main()
        else:
            cli.main()

    else:
        print(USAGE)
        sys.exit(0)


if __name__ == "__main__":
    main()
