"""Examples of importing in Python."""


from lessons import helpers as hp


def main() -> None:
    """Entrypoint of program."""
    print(hp.powerful(2, 4))
    print(f'The Answer {hp.THE_ANSWER}')


if __name__ == "__main__":
    main()