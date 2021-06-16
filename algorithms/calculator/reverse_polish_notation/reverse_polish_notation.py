"""
Programming for linguists

Class for Reverse Polish Notation
"""

from algorithms.calculator.reverse_polish_notation.element import Element


class ReversePolishNotation:
    """
    Reverse Polish Notation class

    It just a wrapper for Queue_.
    To add some interests for this class we add iterations using magic methods
    """

    def __init__(self):
        self._expression_queue = None

    def put(self, element: Element):
        """
        Put the element to the RPN
        :param element: element to put
        """
        self._expression_queue.put(element)

    def __iter__(self):
        return self

    def __next__(self) -> Element:
        """
        Get next element in Reverse Polish Notation
        :return: next element from rpn if exists. Raise StopIteration Error if does not exist
        """
        if self._expression_queue.empty():
            raise StopIteration
        return self._expression_queue.get()
