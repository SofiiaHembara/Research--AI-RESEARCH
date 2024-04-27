import unittest

def get_letter_grade(percent_grade):
    """
    Конвертує середню оцінку в процентах в оцінку за шкалою ECTS.

    Args:
        percent_grade: Число з плаваючою крапкою, яке представляє середню оцінку.

    Returns:
        Символ ("A", "B", "C", "D", "E" або "F"), який представляє оцінку за шкалою ECTS.
    """
    if percent_grade >= 90:
        return "A"
    elif percent_grade >= 80:
        return "B"
    elif percent_grade >= 75:
        return "C"
    elif percent_grade >= 65:
        return "D"
    elif percent_grade >= 60:
        return "E"
    else:
        return "F"

class TestGetLetterGrade(unittest.TestCase):
  """
  Тестовий клас для функції get_letter_grade
  """
  def test_a_grade(self):
    """
    Тест для оцінки A
    """
    self.assertEqual(get_letter_grade(95), "A")

  def test_b_grade(self):
    """
    Тест для оцінки B
    """
    self.assertEqual(get_letter_grade(85), "B")

  def test_c_grade(self):
    """
    Тест для оцінки C
    """
    self.assertEqual(get_letter_grade(78), "C")

  def test_d_grade(self):
    """
    Тест для оцінки D
    """
    self.assertEqual(get_letter_grade(67), "D")

  def test_e_grade(self):
    """
    Тест для оцінки E
    """
    self.assertEqual(get_letter_grade(62), "E")

  def test_f_grade(self):
    """
    Тест для оцінки F
    """
    self.assertEqual(get_letter_grade(55), "F")

  def test_invalid_input(self):
    """
    Тест для недійсного введення
    """
    self.assertEqual(get_letter_grade(-10), "F")

if __name__ == "__main__":
  unittest.main()
