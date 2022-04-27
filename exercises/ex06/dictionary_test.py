"""Tests for Dictionary Functions!"""
__author__ = '730245028'

from dictionary import invert, favorite_color, count

"""INVERT TESTS!"""


def test_invert_multiple_items() -> None:
    """Tests whether multiple items can be inverted."""
    random_dict: dict[str, str] = dict()
    random_dict = {"A": "B", "C": "D", "E": "F"}
    assert invert(random_dict) == {"B": "A", "D": "C", "F": "E"}


def test_invert_numeric_str() -> None:
    """Tests if numeric strs are still inverted."""
    random_dict: dict[str, str] = dict()
    random_dict = {"1": "2", "3": "4"}
    assert invert(random_dict) == {"2": "1", "4": "3"}


# def test_invert_duplicate_keys() -> None:
#     """Tests whether duplicate keys returns an error!"""
#     random_dict: dict[str, str] = dict()
#     random_dict = {"A": "B", "C": "B", "E": "F"}
#     assert invert(random_dict) == KeyError


"""FAVORITE COLOR TESTS!"""


def test_favorite_color_one_item() -> None:
    """Tests if the function performs correctly with just one item in the dict."""
    color_dict: dict[str, str] = dict()
    color_dict = {'Ishan': 'Blue'}
    assert favorite_color(color_dict) == "Blue"


def test_favorite_color_tie() -> None:
    """Tests if the first color is picked during a tie."""
    color_dict: dict[str, str] = dict()
    color_dict = {'Ishan': 'Blue', 'Kris': 'Green', 'Sam': 'Green', 'Jake': 'Blue'}
    assert favorite_color(color_dict) == "Blue"


def test_favorite_color_key_color_name() -> None:
    """Tests if the correct color is picked if a key is the name of a color."""
    color_dict: dict[str, str] = dict()
    color_dict = {'Ishan': 'Green', 'Green': 'Green', 'Sam': 'Green', 'Jake': 'Blue'}
    assert favorite_color(color_dict) == "Green"


"""COUNT TESTS!"""


def test_count_multiple_items() -> None:
    """Tests if appropiate frequencies are given for multiple items"""
    rand_list: list[str] = ['a', 'b', 'c', 'a', 'a', 'b']
    assert count(rand_list) == {'a': 3, 'b': 2, 'c': 1} 


def test_count_frequency_tie() -> None:
    """Tests if appropriate frequencies are given even in a tie."""
    rand_list: list[str] = ['a', 'b', 'c', 'a', 'b', 'c']
    assert count(rand_list) == {'a': 2, 'b': 2, 'c': 2}


def test_count_empty_list() -> None:
    """Tests if an empty dict is rerturned if an empty list is given."""
    rand_list: list[str] = []
    assert count(rand_list) == {}