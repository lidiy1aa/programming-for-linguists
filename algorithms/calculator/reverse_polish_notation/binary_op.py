"""
Programming for linguists

Interfaces and classes of Binary operators
"""

from algorithms.calculator.reverse_polish_notation.digit import Digit
from algorithms.calculator.reverse_polish_notation.op import Op


class BinaryOp(Op):
    """
    Base class for Binary operators (operators with two arguments)
    """

    @staticmethod
    def _function(first_element: float, second_element: float) -> float:
        """
        The static function that computes the result of the binary operator
        Must be implemented in each  class of particular operator

        :param first_element: float - first operand of the binary operator
        :param second_element: float - second operand of the binary operator
        :return: float - result of computing the operation in the "raw" (floating) format
        """
        raise NotImplementedError

    def __call__(self, first_element: Digit, second_element: Digit) -> Digit:
        """
        Magic method to provides computing of the operation. It is the wrapper for the static `function` method
        The main goal of this method is encapsulate work with operands as instances of Digit class

        :param first_element: Digit - first operand of the binary operator
        :param second_element: Digit - second operand of the binary operator
        :return: float - result of computing the operation as an instance of Digit class
        """
        first_digit = first_element.digit
        second_digit = second_element.digit
        return super().__call__(first_digit, second_digit)


class Plus(BinaryOp):
    """
    Implementation of operator +
    """
    priority = 0
    symbol = '+'

    @staticmethod
    def _function(first_element: float, second_element: float) -> float:
        return first_element + second_element


class Minus(BinaryOp):
    """
    Implementation of operator -
    """
    priority = 0
    symbol = '-'

    @staticmethod
    def _function(first_element: float, second_element: float) -> float:
        return first_element - second_element


class Multiplier(BinaryOp):
    """
    Implementation of operator *
    """
    priority = 1
    symbol = '*'

    @staticmethod
    def _function(first_element: float, second_element: float) -> float:
        return first_element * second_element


class Divider(BinaryOp):
    """
    Implementation of operator /
    """
    priority = 1
    symbol = '/'

    @staticmethod
    def _function(first_element: float, second_element: float) -> float:
        return first_element / second_element


class Power(BinaryOp):
    """
    Implementation of operator ^
    """
    priority = 2
    symbol = '^'

    @staticmethod
    def _function(first_element: float, second_element: float) -> float:
        return first_element ** second_element