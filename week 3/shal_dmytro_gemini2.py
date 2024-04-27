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

def main():
  """
  Головна функція програми.
  """
  # Введення оцінок
  grades = []
  for _ in range(5):
    grade = float(input())
    if not 0 <= grade <= 100:
      print("None")
      return
    grades.append(grade)

  # Розрахунок середньої оцінки
  percent_grade = sum(grades) / len(grades)
  percent_grade = round(percent_grade, 1)

  # Виведення результату
  letter_grade = get_letter_grade(percent_grade)
  print(f"Average grade = {percent_grade} -> {letter_grade}")

if __name__ == "__main__":
  main()
