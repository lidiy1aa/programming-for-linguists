import unittest
from algorithms.calculator.converter import ReversePolishNotationConverter


class Tests(unittest.TestCase):
    def ideal_test(self):
        """идеальный случай, на вход подается инфиксная запись, конвертер преобразует
        ее в постфиксную"""
        example = '2^2+3*6-(7+1)'
        expected_res = '22^36*+71+'
        res = ReversePolishNotationConverter(example)
        res.convert()

        self.assertEqual(expected_res, res)

    def isalpha_test(self):
        """на вход подается слово,в результате конвертер выдает пустую строку"""
        example = 'hello'
        expected_res = ''
        res = ReversePolishNotationConverter(example)
        res.convert()

        self.assertEqual(expected_res, res)

    def space_test(self):
        """на вход подается инфиксная запись с пробелами, конвертер должен преобразовать
        ее в постфиксную"""
        example = '3 + 8 ^ 3 / ( 6 - 8 )'
        expected_res = '383^68-/+'
        res = ReversePolishNotationConverter(example)
        res.convert()

        self.assertEqual(expected_res, res)

    def negative_test(self):
        "проверка на то, что конвертер правильно преобразует выражения с отрицательными числами"
        example = '-6+8'
        expected_res = '6-8+'
        res = ReversePolishNotationConverter(example)
        res.convert()

        self.assertEqual(expected_res, res)

    def letters(self):
        """конвертер может определить случаи, когда вместо числа пользователь вводит букву"""
        example = '7+o*3'
        expected_res = '703*+'
        res = ReversePolishNotationConverter(example)
        res.convert()

        self.assertEqual(expected_res, res)