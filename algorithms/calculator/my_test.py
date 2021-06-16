import unittest
from algorithms.calculator.converter import ReversePolishNotationConverter


class Tests(unittest.TestCase):
    def test_ideal(self):
        """идеальный случай, на вход подается инфиксная запись, конвертер преобразует
        ее в постфиксную"""
        example = '2^2+3*6-(7+1)'
        expected_res = '22^36*+71+'
        res = ReversePolishNotationConverter()
        res.convert(example)

        self.assertEqual(expected_res, res)

    def test_isalpha(self):
        """на вход подается слово,в результате конвертер выдает пустую строку"""
        example = 'hello'
        expected_res = ''
        res = ReversePolishNotationConverter()
        res.convert(example)

        self.assertEqual(expected_res, res)

    def test_space(self):
        """на вход подается инфиксная запись с пробелами, конвертер должен преобразовать
        ее в постфиксную"""
        example = '3 + 8 ^ 3 / ( 6 - 8 )'
        expected_res = '383^68-/+'
        res = ReversePolishNotationConverter()
        res.convert(example)

        self.assertEqual(expected_res, res)

    def test_negative(self):
        "проверка на то, что конвертер правильно преобразует выражения с отрицательными числами"
        example = '-6+8'
        expected_res = '6-8+'
        res = ReversePolishNotationConverter()
        res.convert(example)

        self.assertEqual(expected_res, res)

    def test_letters(self):
        """конвертер может определить случаи, когда вместо числа пользователь вводит букву"""
        example = '7+o*3'
        expected_res = '703*+'
        res = ReversePolishNotationConverter()
        res.convert(example)

        self.assertEqual(expected_res, res)