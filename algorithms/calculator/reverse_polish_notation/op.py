"""
Programming for linguists

Interfaces and classes for Operators
"""
from typing import Type

from algorithms.calculator.reverse_polish_notation.digit import Digit
from algorithms.calculator.reverse_polish_notation.element import Element


class OpFactory:
    """
    Class to provide functionality for creating concrete instance of Op
    """
    _registry = {}

    @staticmethod
    def add_op_class(op_class: Type['Op']):
        """
        Function to add a new Operator class to registry
        :param op_class: class of Operator
        """
        if not op_class.symbol:
            return
        OpFactory._registry[op_class.symbol] = op_class

    @staticmethod
    def get_op_by_symbol(op_symbol: str) -> 'Op':
        """
        Function to get Operator class by symbol
        :param op_symbol: symbol of the operator to return
        :return: class of Operator
        """
        try:
            return OpFactory._registry[op_symbol]()
        except KeyError as error:
            raise AssertionError from error


class OpMeta(type):
    """
    Metaclass for all Operators
    """
    def __new__(cls, *args, **kwargs):
        """
        Method to create a Operator class
        :param args:
        :param kwargs:
        """
        op_class: Type[Op] = super().__new__(cls, *args, **kwargs)
        OpFactory.add_op_class(op_class)
        return op_class


class Op(Element, metaclass=OpMeta):
    """
    Base class for Operators
    """
    priority = None
    symbol = None

    @staticmethod
    def _function(*args, **kwargs) -> float:
        """
        Functions to calculate the operation.
        Arguments depends on the specific operator.
        """
        raise NotImplementedError

    def __call__(self, *args, **kwargs) -> Digit:
        """
        Public method to call operator.
        Makes instances of the Op class callable:
        op = Op();
        result = op(Digit1, Digit2)
        """
        res = self._function(*args, **kwargs)
        return Digit(res)

    def __gt__(self, other: 'Op') -> bool:
        return self.priority > other.priority

    def __eq__(self, other: 'Op') -> bool:
        return self.symbol == other.symbol
