"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730245028"


class Simpy:
    # Attribute Definitions
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructor method!"""
        self.values = values
    
    def __str__(self) -> str:
        """Converts Simpy object to a str representation."""
        # result: list[str] = []
        # i: int = 0
        # while i < len(self.values):
        #     result.append(str(self.values[i]))
        #     i += 1
        return f'Simpy({str(self.values)})'
    
    def fill(self, x: float, n: int):
        """Fills simpy with x value n amount of times."""
        result_list: list[float] = []
        i: int = 0
        while i < n:
            result_list.append(x)
            i += 1
        self.values = result_list

    def arange(self, start: float, stop: float, step: float = 1):
        """Fill in values with a range."""
        self.step = step
        result: list[float] = []
        i: float = 0
        while i < abs((stop / step) - abs(step)):
            result.append(start + (step * i))
            i += 1
        self.values = result
    
    def sum(self) -> float:
        """Sums values in Simpy."""
        result: float = sum(self.values)
        return result
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload of add."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs)
                i += 1
            return result
        else:
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
            return result
    
    