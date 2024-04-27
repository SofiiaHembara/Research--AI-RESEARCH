numbers = [int(input()) for _ in range(5)]
if all(0 <= num <= 100 for num in numbers):
    average = sum(numbers) / len(numbers)
    if average < 60:
        grade = 'F'
    elif average < 65:
        grade = 'D'
    elif average < 70:
        grade = 'C'
    elif average < 90:
        grade = 'B'
    elif average > 80:
        grade = 'A'
    print(f'Average grade = {average:.1f} -> {grade}')
else:
    print("None")
