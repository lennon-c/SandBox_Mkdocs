# calculator/calculations.py"""

"""Provide several sample math calculations.

This module allows the user to make mathematical calculations.
"""

from typing import Union, Optional, Any

class Two_numbers(): 
    """Several sample math calculations using two numbers.
    
    Examples:
        ```pycon exec="true" source="console"  
        >>> from sandbox.calculations import Two_numbers
        >>> nums = Two_numbers(4, 2)
        >>> print(f'{nums.add()=}')
        ```
 
    """

    def __init__(self, first: Union[float, int], second: Union[float, int]):
        """Initiate my number.

        Args:
            first: the first number 
            second: the second number  
        """
        self.first: Union[float, int]= first
        """The first number."""
        self.second = second
        """The second number."""
 
    
    def add(self, *args) -> Union[float, int]:
        """Add my two numbers, and if additional numbers are provided, add them to the sum.
        
        Returns:
            A number representing the arithmetic of all the numbers.
        """
        if len(args) > 0:
            return sum(args) + add(self.first, self.second)
        return add(self.first, self.second)
    
    def subtract(self) -> Union[float, int]:
        """Subtract my two numbers."""
        return subtract(self.first, self.second)
    
    def multiply(self) -> Union[float, int]:
        """Multiply my two numbers."""
        return multiply(self.first, self.second)
    
    def divide(self) -> Union[float, int]:
        """Divide my two numbers."""
        return divide(self.first, self.second)
 

def add(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the sum of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a: A number representing the first addend in the addition.
        b: A number representing the second addend in the addition.

    Returns:
        A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a + b)

def subtract(a: Union[float, int], b: Union[float, int]) -> float:
    """Calculate the difference of two numbers.

    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0

    Args:
        a: A number representing the minuend in the subtraction.
        b: A number representing the subtrahend in the subtraction.

    Returns:
        A number representing the difference between `a` and `b`.
    """
    return float(a - b)

def multiply(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the product of two numbers.

    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0

    Args:
        a: A number representing the multiplicand in the multiplication.
        b: A number representing the multiplier in the multiplication.

    Returns:
        A number representing the product of `a` and `b`.
    """
    return float(a * b)

def divide(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the quotient of two numbers.

    Examples:
        >>> divide(4.0, 2.0)
        2.0
        >>> divide(4, 2)
        2.0
        >>> divide(4, 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: division by zero

    Args:
        a: A number representing the dividend in the division.
        b: A number representing the divisor in the division.

    Returns:
        A number representing the quotient of `a` and `b`.

    Raises:
        ZeroDivisionError: An error occurs when the divisor is `0`.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)

# help(add)
# print(add.__doc__)