"""Exercise 06!"""

__author__ = "730245028"

"""Invert."""


def invert(my_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the key: value pairing of a given dict."""
    inverted_dict: dict[str, str] = dict()
    for key in my_dict:
        # if my_dict[key] in inverted_dict:
        #     raise KeyError("Duplicate Keys!")
        inverted_dict[my_dict[key]] = key
    print(inverted_dict)
    return inverted_dict


def favorite_color(my_dict: dict[str, str]) -> str:
    """Determines the most frequent color!"""
    counter_dict: dict[str, int] = dict()
    for key in my_dict:
        if my_dict[key] in counter_dict:
            counter_dict[my_dict[key]] += 1
        else:
            counter_dict[my_dict[key]] = 0
    max_key = max(counter_dict, key=counter_dict.get)
    print(max_key)
    return max_key


def count(x: list[str]) -> dict[str, int]:
    """Provides the frequency of str's in a list."""
    new_dict: dict[str, int] = {}
    i: int = 0
    while i < len(x):
        if x[i] in new_dict:
            new_dict[x[i]] += 1
        else:
            new_dict[x[i]] = 1
        i += 1
    print(new_dict)
    return new_dict


random_dict: dict[str, str] = dict()
random_dict = {"A": "B", "C": "B", "E": "F"}
print(random_dict)
invert(random_dict)
color_dict: dict[str, str] = dict()
color_dict = {'Ishan': 'Blue', 'Kris': 'Blue', 'Sam': 'Green', 'Jake': 'Blue'}
favorite_color(color_dict)
rand_list: list[str] = ['a', 'b', 'c', 'a', 'a', 'b']
count(rand_list)