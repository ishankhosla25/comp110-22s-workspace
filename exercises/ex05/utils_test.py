"""Tests for Utils functions!"""
__author__ = "730245028"

from utils import only_evens, sub, concat

# Only Evens Tests:


def test_only_evens_empty_list() -> None:
    """Tests whether only_evens returns an empty list if it is given one."""
    empty_list: list[int] = []
    assert only_evens(empty_list) == []


def test_only_evens_odd_only() -> None:
    """Tests if only_evens returns an empty list if given only odd numbers."""
    odd_list: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(odd_list) == []


def test_only_evens_list_w_zero() -> None:
    """Tests if only_evens is able to correctly identify 0 as an even number."""
    list_w_zero: list[int] = [0, 0, 0, 2, 5]
    assert only_evens(list_w_zero) == [0, 0, 0, 2]


# Sub Tests:


def test_sub_endindex_noninclusive() -> None:
    """Tests whether end index is noninclusive in the list"""
    rand_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sub(rand_list, 0, 4) == [1, 2, 3, 4]


def test_sub_incorrect_startend_index() -> None:
    """Test whether an empty list is returned when incorrect start/end index are given."""
    rand_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sub(rand_list, -3, -2) == []


def test_sub_large_end_index() -> None:
    """Tests whether sub is able to appropriately reclassify end index to len(list)."""
    rand_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sub(rand_list, 0, 12) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Concat Tests


def test_concat_merge_2emptylists() -> None:
    """Tests whether 2 empty lists merge into one empty list."""
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []


def test_concat_merge_lists_in_order() -> None:
    """Tests whether the items in list 1 precede the items in list 2."""
    list_1: list[int] = [1, 2, 3, 4, 5]
    list_2: list[int] = [6, 7, 8, 9, 10]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_concat_duplicates() -> None:
    """Tests whether duplicate items are added correctly."""
    list_1: list[int] = [1, 1, 2, 2, 3, 3]
    list_2: list[int] = [1, 2, 3]
    assert concat(list_1, list_2) == [1, 1, 2, 2, 3, 3, 1, 2, 3]