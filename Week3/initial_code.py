"""
Create table
"""
def create_table(n, m):
    """
    Функція рекурсивно побудовує таблицю чисел розміром n на m
    згідно з виразом 𝐴[𝑖][𝑗]=𝐴[𝑖−1][𝑗]+𝐴[𝑖][𝑗−1]
    та іншими наведеними правилами.
    """
    if n == 0 or m == 0:
        return []

    if n == 1 and m == 1:
        return [[1]]

    if n == 1:
        return [[1] * m]

    if m == 1:
        return [[1] * n] * m

    prev_table = create_table(n - 1, m)
    last_row = prev_table[-1]
    new_row = [1]
    for j in range(1, m):
        new_row.append(new_row[-1] + last_row[j])

    return prev_table + [new_row]

def flatten(lst):
    """
    Функція рекурсивно розгортає вкладені списки
    та повертає один список з усіх не порожніх елементів кожного списку.
    """
    if not isinstance(lst, list):
        return lst

    result = []
    for item in lst:
        result.extend(flatten(item))
    return [x for x in result if x]
