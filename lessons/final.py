"""Final Practice Exam!"""


def reverse_multiply(x: list[int]) -> list[int]:
    """Docstring."""
    result: list[int] = []
    i: int = len(x) - 1
    while i >= 0:
        result.append(x[i] * 2)
        i -= 1
    return result


rand_list: list[int] = [1, 2, 3]
print(reverse_multiply(rand_list))