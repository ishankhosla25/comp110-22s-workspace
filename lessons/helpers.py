"""Defining a medule imported elsewhere."""


THE_ANSWER: int = 42


def main() -> None:
    print(powerful(2, 10))
    print("helpers.py was run as a module")


def powerful(x: float, n: float) -> float:
    return x ** n


if __name__ == "__main__":
    main()
else:
    print(f'helpers.py was imported: {__name__}')