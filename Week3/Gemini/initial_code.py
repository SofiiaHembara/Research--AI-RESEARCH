"""
A function for calculating simple mathematical actions written in a sentence
"""
def calculate_expression(expression: str) -> int:
    """
    (str) -> int
    Returns the result of an expression written 
    in a sentence(expression).
    If the expression is formulated incorrectly, it returns
    'Неправильний вираз'
    >>> calculate_expression('Скільки буде 5 додати 5?')
    10
    >>> calculate_expression('Скільки буде 2 помножити на 10 додати 7?')
    27
    >>> calculate_expression('Скільки буде 3 в квадраті?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки сезонів в році?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 2 2 додати?')
    'Неправильний вираз!'
    >>> calculate_expression(12 - 2)
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 2 помножити на 10 поділити на 0?')
    'Неправильний вираз!'
    """
    if not isinstance(expression, str):
        return 'Неправильний вираз!'
    if not expression.startswith('Скільки буде '):
        return 'Неправильний вираз!'
    if not expression.endswith('?'):
        return 'Неправильний вираз!'
    expression = expression.replace('?','')
    to_delete = ['Скільки', 'буде', 'на']
    new_ex = []
    for i in expression.split():
        if i not in to_delete:
            new_ex.append(i)
    result = int(new_ex[0])
    for i in range(1, len(new_ex), 2):
        if i+1 > (len(new_ex) - 1):
            return 'Неправильний вираз!'
        if not new_ex[i+1].lstrip('-').isdigit():
            return 'Неправильний вираз!'
        if new_ex[i] == 'додати' or new_ex[i] == 'плюс':
            result += int(new_ex[i+1])
        elif new_ex[i] == 'відняти' or new_ex[i] == 'мінус':
            result -= int(new_ex[i+1])
        elif new_ex[i] == 'поділити':
            result /= int(new_ex[i+1])
        elif new_ex[i] == 'помножити':
            result *= int(new_ex[i+1])
    return result
