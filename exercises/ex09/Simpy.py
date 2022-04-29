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
        while i <= abs((stop / step) - abs(step)):
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
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload of power!"""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs)
                i += 1
            return result
        else:
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
            return result
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Testing if floats at certain indexes are equal."""
        result: list[bool] = []
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs)
                i += 1
            return result
        else:
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
            return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Tests if a float is greater than another at a certain index."""
        result: list[bool] = []
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs)
                i += 1
            return result
        else:
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
            return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Ads subscription notation to a Simpy."""
        if isinstance(rhs, int):
            float_result: float = 0.0
            float_result = self.values[rhs]
            return float_result
        else:
            simpy_result: Simpy = Simpy([])
            if rhs.__eq__(rhs):
                i: int = 0
                while i < len(self.values):
                    simpy_result.values.append(self.values[i])
                    i += 1
            if rhs.__gt__(rhs):
                i: int = 0
                while i < len(self.values):
                    simpy_result.values.append(self.values[i])
                    i += 1
            # if rhs.__eq__:
            return simpy_result
