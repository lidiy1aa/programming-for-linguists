"""
Programming for linguists

Implementation of the Reverse Polish Notation Converter
"""
from algorithms.calculator.reverse_polish_notation import BinaryOp, Digit, OpFactory, Op, ReversePolishNotation
from data_structures.queue_.queue_ import Queue_
from data_structures.stack.stack import Stack


class ReversePolishNotationConverter:
    """
    Class for converting infix expressions to reverse polish notation
    """
    point = '.'

    def __init__(self, infix_string: str):
        self._infix_notation = Queue_(infix_string)
        self._postfix_notation = ReversePolishNotation()
        self.stack = Stack()

    def convert(self) -> ReversePolishNotation:
        """
        Main method of the class.
        Convert infix the expression to reverse polish notation

        :return: ReversePolishNotation object
        """
        while not self._infix_notation.empty():
            character = self._infix_notation.get()
            if self.is_part_of_digit(character):
                digit = self.read_digit(character)
                self._postfix_notation.put(digit)
                continue
            elif self.is_opening_bracket(character):
                self.stack.push(character)
                continue
            elif self.is_closing_bracket(character):
                self.pop_from_stack_until_opening_bracket()
                continue

            operator = OpFactory.get_op_by_symbol(character)
            if self.is_binary_operation(operator):
                self.pop_from_stack_until_prioritizing(operator)
            else:
                raise Exception(character)
        while not self.stack.empty():
            self._postfix_notation.put(self.stack.top())
            self.stack.pop()
        return self._postfix_notation

    def pop_from_stack_until_opening_bracket(self):
        while not self.is_opening_bracket(self.stack.top()):
            self._postfix_notation.put_operator(self.stack.top())
            self.stack.pop()
        self.stack.pop()

    def pop_from_stack_until_prioritizing(self, operator: Op):
        current_priority = operator.priority
        while not self.stack.empty() and self.stack.top().priority > current_priority:
            self._postfix_notation.put(self.stack.top())
            self.stack.pop()
        self.stack.push(operator)

    def read_digit(self, character: str):
        digit = character
        while not self._infix_notation.empty() and self.is_part_of_digit(self._infix_notation.top()):
            digit += self._infix_notation.get()
        return Digit(digit)

    @staticmethod
    def is_part_of_digit(character: str) -> bool:
        return character.isdigit() or character == ReversePolishNotationConverter.point

    @staticmethod
    def is_opening_bracket(character: str) -> bool:
        if character == '(':
            return True
        return False

    @staticmethod
    def is_closing_bracket(character: str) -> bool:
        if character == ')':
            return True
        return False

    @staticmethod
    def is_binary_operation(operator: Op) -> bool:
        return isinstance(operator, BinaryOp)
