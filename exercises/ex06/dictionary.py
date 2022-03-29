"""Exercise 06!"""

__author__ = "730245028"

"""Invert."""


def invert(x) -> dict:
    invert_dict: dict[str, str]
    invert_dict = dict()
    for key in x:
        temp = x[key]
        invert_dict[temp] = key
    x = invert_dict
    return x


random_dict: dict[str, str]
random_dict = dict()
random_dict['A'] = 'B'
print(random_dict['A'])
invert(random_dict)
print(random_dict)