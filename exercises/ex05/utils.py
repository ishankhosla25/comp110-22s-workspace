"""Utils function skeletons!"""
__author__ = "730245028"


def only_evens(rand_list: list[int]) -> list[int]:
    """A function that produces a list of even integers from a given list!"""
    i: int = 0
    evens_list: list[int] = []
    while i < len(rand_list):
        if rand_list[i] % 2 == 0:
            evens_list.append(rand_list[i])
        i += 1
    print(evens_list)
    return evens_list


def sub(rand_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Generates a sub list from a given list!"""
    empty_list: list[int] = []
    a_list: list[int] = []
    i: int = start_index
    if start_index < 0:
        i = 0
    if start_index > len(rand_list) or len(rand_list) == 0 or end_index <= 0:
        return empty_list
    if end_index > len(rand_list):
        end_index = len(rand_list)
    while i < end_index:
        a_list.append(rand_list[i])
        i += 1
    print(a_list)
    return a_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Merges two lists!"""
    a_list: list[int] = []
    i: int = 0
    while i < len(list_1):
        a_list.append(list_1[i])
        i += 1
    i = 0
    while i < len(list_2):
        a_list.append(list_2[i])
        i += 1
    print(a_list)
    return a_list


def main() -> None:
    only_evens([1, 2, 3, 4, 5, 6])
    rand_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    sub(rand_list, 0, 30)
    list_1 = [1, 2, 3, 4, 5, 6]
    list_2 = [6, 7, 8, 9, 10]
    concat(list_1, list_2)


if __name__ == "__main__":
    main()