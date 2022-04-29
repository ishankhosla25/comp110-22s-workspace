"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730245028"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_invalid_index() -> None:
    """If index is greater than len of list, IndexError."""
    head = Node(1, Node(2, Node(3, None)))
    with pytest.raises(IndexError):
        value_at(head, 6)


def test_value_at_valid_index() -> None:
    """If valid index, correct head.data value provided."""
    head = Node(1, Node(2, Node(3, None)))
    assert value_at(head, 2) == 3


def test_max_empty() -> None:
    """If empty linked list is given, ValueError raised."""
    with pytest.raises(ValueError):
        max(None)


def test_max_tied_values() -> None:
    """Correct value given even if 2 max values are tied."""
    head = Node(30, Node(10, Node(30, None)))
    assert max(head) == 30


def test_linkify_single_item() -> None:
    """Linked list made with correct value even if only one value is given."""
    items: list[int] = [25]
    assert str(linkify(items)) == "25 -> None"


def test_linkify_duplicate_items() -> None:
    """Provides a correct linked list, with duplicate items."""
    item: list[int] = [1, 1, 2, 2]
    assert str(linkify(item)) == "1 -> 1 -> 2 -> 2 -> None"


def test_scale_factor_is_0() -> None:
    """Provides a linked list of 0s if factor is 0."""
    head = Node(1, Node(2, Node(3, None)))
    assert str(scale(head, 0)) == "0 -> 0 -> 0 -> None"


def test_scale_duplicate_items() -> None:
    """Correctly scales duplicate items."""
    head = Node(2, Node(2, Node(3, None)))
    assert str(scale(head, 2)) == "4 -> 4 -> 6 -> None"