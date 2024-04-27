"""
Create table
"""
def create_table(n, m):
    """
    Функція рекурсивно побудовує таблицю чисел розміром n на m
    згідно з виразом 𝐴[𝑖][𝑗]=𝐴[𝑖−1][𝑗]+𝐴[𝑖][𝑗−1]
    та іншими наведеними правилами.

    Приклад:
    >>> create_table(4, 6)
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]]
    >>> create_table(1, 1)
    [[1]]
    >>> create_table(3, 3)
    [[1, 1, 1], [1, 2, 3], [1, 3, 6]]
    """
    if n == 0 or m == 0:
        return []

    if n == 1 and m == 1:
        return [[1]]

    if n == 1:
        return [[1] * m]

    if m == 1:
        return [[1] * n for _ in range(m)]

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

    Приклад:
    >>> flatten([1, [2]]) 
    [1, 2]
    >>> flatten([1, 2, [3, [4, 5], 6], 7])
    [1, 2, 3, 4, 5, 6, 7]
    >>> flatten(['wow', [2,[[]]], [True]]) 
    ['wow', 2, True]
    >>> flatten([]) 
    []
    >>> flatten([[]])
    []
    >>> flatten(3)
    3
    """
    if not isinstance(lst, list):
        return lst
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        elif item:
            result.append(item)
    return result
