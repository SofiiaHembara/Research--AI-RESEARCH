import unittest

def calculate_grades(grade1, grade2, grade3, grade4, grade5):
    # Перевірка чи всі оцінки в діапазоні [0, 100]
    if not all(0 <= grade <= 100 for grade in [grade1, grade2, grade3, grade4, grade5]):
        return None
    
    # Обчислення середньої оцінки
    average_grade = (grade1 + grade2 + grade3 + grade4 + grade5) / 5
    # Округлення до одного десяткового знаку
    average_grade = round(average_grade, 1)
    
    # Визначення оцінки за шкалою ECTS
    if average_grade >= 90:
        letter_grade = "A"
    elif average_grade >= 80:
        letter_grade = "B"
    elif average_grade >= 75:
        letter_grade = "C"
    elif average_grade >= 65:
        letter_grade = "D"
    elif average_grade >= 60:
        letter_grade = "E"
    else:
        letter_grade = "F"
    return average_grade, letter_grade

class TestCalculateGrades(unittest.TestCase):
    def test_valid_grades(self):
        result = calculate_grades(90, 85, 80, 75, 70)
        self.assertEqual(result, (80.0, 'B'))

    def test_invalid_grades(self):
        result = calculate_grades(90, 85, 80, 105, 70)
        self.assertIsNone(result)

    def test_rounding(self):
        result = calculate_grades(88, 88, 88, 88, 88)
        self.assertEqual(result, (88.0, 'B'))

    def test_letter_grade(self):
        result = calculate_grades(91, 80, 76, 68, 55)
        self.assertEqual(result, (74.0, 'D'))

    def test_lower_bound(self):
        result = calculate_grades(0, 0, 0, 0, 0)
        self.assertEqual(result, (0.0, 'F'))

    def test_upper_bound(self):
        result = calculate_grades(100, 100, 100, 100, 100)
        self.assertEqual(result, (100.0, 'A'))

if __name__ == '__main__':
    unittest.main()
