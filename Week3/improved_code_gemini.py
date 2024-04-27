"""
Create table
"""
def create_table(n, m):
    """
    Функція рекурсивно будує таблицю чисел розміром n на m, де n - це кількість рядків,
    а m - це кількість стовпчиків в таблиці.

    Args:
        n (int): Кількість рядків в таблиці.
        m (int): Кількість стовпчиків в таблиці.
s
    Returns:
        List[List[int]]: Таблиця чисел, заповнена згідно з заданими правилами.

    Raises:
        TypeError: Якщо n або m не є цілими числами.

    Examples:
        >>> create_table(4, 6)
        [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]]
        >>> create_table(1, 1)
        [[1]]
        >>> create_table(0, 0)
        []
    """
    if not isinstance(n, int) or not isinstance(m, int):
        raise TypeError("n and m must be integers")

    if n == 0 or m == 0:
        return [[]] * m

    table = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                table[i][j] = 1
            else:
                table[i][j] = table[i - 1][j] + table[i][j - 1]

    return table


def flatten(lst):
    """
    Функція рекурсивно розгортає вкладені списки.

    Args:
        lst (list): Вхідний список, який може містити інші списки.

    Returns:
        List: Розгорнутий список, який містить всі не порожні елементи 
        з вхідного списку lst.

    Examples:
        >>> flatten([1, [2]])
        [1, 2]
    """
    if not isinstance(lst, list):
        return lst
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        elif item is not None:
            result.append(item)

    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)