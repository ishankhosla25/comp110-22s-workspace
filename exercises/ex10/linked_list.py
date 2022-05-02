"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730245028"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next is None:
            return head.data
        else:
            return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Returns the data of Node at certain index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.data
    else:
        return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> int:
    """Finds the max data value."""
    if head is None:
        raise ValueError("last cannot be called with None")
    if head.next is None:
        return head.data
    if head.data >= max(head.next):
        return head.data
    else:
        return max(head.next)


def linkify(items: list[int]) -> Optional[Node]:
    """Creates a linked list with the given values."""
    if len(items) == 0:
        return None
    if len(items) == 1:
        head: Node = Node(items[0], None)
        return head
    else:
        head: Node = Node(items[0], linkify(items[1:]))
        return head


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Scales all the values by factor."""
    new_result: Optional[Node] = head
    if new_result is None:
        return None
    if new_result.next is None:
        new_result.data *= factor
    else:
        new_result.data *= factor
        new_result.next = scale(new_result.next, factor)
    return new_result


head: Node = Node(1, Node(2, Node(3, None)))
print(last(head))
print(value_at(head, 1))
print(max(head))
items: list[int] = [25]
print(linkify(items))
print(scale(linkify([1, 2, 3, 4]), 2))