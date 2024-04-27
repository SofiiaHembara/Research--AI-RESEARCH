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

if __name__ == "__main__":
    # Зчитування введених користувачем оцінок
    grade1 = int(input())
    grade2 = int(input())
    grade3 = int(input())
    grade4 = int(input())
    grade5 = int(input())
    
    # Виклик функції та виведення результату
    result = calculate_grades(grade1, grade2, grade3, grade4, grade5)
    if result is None:
        print("None")
    else:
        average_grade, letter_grade = result
        print(f"Average grade = {average_grade} -> {letter_grade}")
