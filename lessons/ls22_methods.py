"""Magic Methods!"""
from __future__ import annotations


class Point:
    """Attributes."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Constructor."""
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        """Produce a str rep of a Point for python!"""
        return f"Point({self.x}, {self.y})"
    
    def __mul__(self, factor: float) -> Point:
        """Overload the * operator for Point * float."""
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, rhs: Point) -> Point:
        """Overloading Add."""
        return Point(self.x + rhs.x, self.y + rhs.y)
    
    def __getitem__(self, index: int) -> float:
        """Overload subsription notation."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError


a: Point = Point(1.0, 2.0)
b: Point = a * 2.0
c: Point = a + b
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

print(a[0])
print(b[1])