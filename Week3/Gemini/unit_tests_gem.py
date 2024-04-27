from optimized_gem import calculate_expression
import unittest

class TestCalculateExpression(unittest.TestCase):
    def test_correct_addition(self):
        self.assertEqual(calculate_expression('Скільки буде 5 додати 5?'), 10)

    def test_correct_multiplication_and_addition(self):
        self.assertEqual(calculate_expression('Скільки буде 2 помножити на 10 додати 7?'), 27)

    def test_correct_multiplication_and_subtraction(self):
        self.assertEqual(calculate_expression('Скільки буде 2 помножити на 10 відняти 3?'), 17)

    def test_correct_division(self):
        self.assertEqual(calculate_expression('Скільки буде 20 поділити на 2?'), 10)

    def test_invalid_expression_no_question_mark(self):
        self.assertEqual(calculate_expression('Скільки буде 3 в квадраті?'), 'Неправильний вираз!')

    def test_invalid_expression_no_starting_phrase(self):
        self.assertEqual(calculate_expression('Скільки сезонів в році?'), 'Неправильний вираз!')

    def test_invalid_expression_incorrect_operand(self):
        self.assertEqual(calculate_expression('Скільки буде 2 2 додати?'), 'Неправильний вираз!')

    def test_invalid_expression_direct_input(self):
        self.assertEqual(calculate_expression(12 - 2), 'Неправильний вираз!')

    def test_invalid_expression_division_by_zero(self):
        self.assertEqual(calculate_expression('Скільки буде 2 помножити на 10 поділити на 0?'), 'Неправильний вираз!')

    def test_empty_expression(self):
        self.assertEqual(calculate_expression(''), 'Неправильний вираз!')

    def test_negative_numbers_in_addition(self):
        self.assertEqual(calculate_expression('Скільки буде 5 додати -5?'), 0)

    def test_negative_numbers_in_multiplication(self):
        self.assertEqual(calculate_expression('Скільки буде 2 помножити на -10?'), -20)

    def test_negative_numbers_in_subtraction(self):
        self.assertEqual(calculate_expression('Скільки буде 5 відняти -5?'), 10)

    def test_decimal_numbers_in_division(self):
        self.assertEqual(calculate_expression('Скільки буде 10 поділити на 2?'), 5.0)

    def test_multiple_operations_in_expression(self):
        self.assertEqual(calculate_expression('Скільки буде 5 помножити на 2 додати 3 відняти 1?'), 12)
