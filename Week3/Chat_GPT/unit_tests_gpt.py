from optimized_gpt import calculate_expression
import unittest


class TestCalculateExpression(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate_expression("Скільки буде 8 додати 3?"), 11)

    def test_subtraction(self):
        self.assertEqual(calculate_expression("Скільки буде 7 відняти 3?"), 4)

    def test_multiplication(self):
        self.assertEqual(calculate_expression("Скільки буде 7 помножити на 3?"), 21)

    def test_division(self):
        self.assertEqual(calculate_expression("Скільки буде 10 поділити на 2?"), 5)

    def test_complex_expression(self):
        self.assertEqual(calculate_expression("Скільки буде 7 додати 3 помножити на 5?"), 50)

    def test_negative_divisor(self):
        self.assertEqual(calculate_expression("Скільки буде 10 поділити на -2?"), -5)

    def test_invalid_expression(self):
        self.assertEqual(calculate_expression("Скільки буде 3 в кубі?"), 'Неправильний вираз!')

    def test_non_mathematical_expression(self):
        self.assertEqual(calculate_expression("Скільки сезонів в році?"), 'Неправильний вираз!')

    def test_invalid_syntax(self):
        self.assertEqual(calculate_expression("Скільки буде 2 2 додати?"), 'Неправильний вираз!')

    def test_non_string_input(self):
        self.assertEqual(calculate_expression(12 - 2), 'Неправильний вираз!')

    def test_division_by_zero(self):
        self.assertEqual(calculate_expression("Скільки буде 2 помножити на 10 поділити на 0?"), 'Неправильний вираз!')

    def test_invalid_start(self):
        self.assertEqual(calculate_expression("Яка сума чисел 2 і 3?"), 'Неправильний вираз!')

    def test_invalid_end(self):
        self.assertEqual(calculate_expression("Скільки буде 2 додати 3"), 'Неправильний вираз!')

    def test_invalid_operator(self):
        self.assertEqual(calculate_expression("Скільки буде 5 взяти з 7?"), 'Неправильний вираз!')

    def test_division_by_zero_check(self):
        self.assertEqual(calculate_expression("Скільки буде 2 помножити на 10 поділити на 0?"), 'Неправильний вираз!')
    def test_invalid_expression_end(self):
        self.assertEqual(calculate_expression("Скільки буде 2 додати 3"), 'Неправильний вираз!')
    def test_multiplication_false(self):
        self.assertEqual(calculate_expression("Скільки буде 7 помножи на 3?"), 'Неправильний вираз!')
    