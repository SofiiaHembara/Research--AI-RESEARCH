def calculate_expression(expression: str) -> int:
    if not isinstance(expression, str):
        return 'Неправильний вираз!'
    if not expression.startswith('Скільки буде '):
        return 'Неправильний вираз!'
    if not expression.endswith('?'):
        return 'Неправильний вираз!'
    expression = expression.replace('?', '')
    to_delete = ['Скільки', 'буде', 'на']
    new_ex = []
    for i in expression.split():
        if i not in to_delete:
            new_ex.append(i)
    result = int(new_ex[0])
    for i in range(1, len(new_ex), 2):
        if i + 1 > (len(new_ex) - 1):
            return 'Неправильний вираз!'
        if not new_ex[i + 1].lstrip('-').isdigit():
            return 'Неправильний вираз!'
        if new_ex[i] == 'додати' or new_ex[i] == 'плюс':
            result += int(new_ex[i + 1])
        elif new_ex[i] == 'відняти' or new_ex[i] == 'мінус':
            result -= int(new_ex[i + 1])
        elif new_ex[i] == 'поділити':
            if int(new_ex[i + 1]) == 0:
                return 'Неправильний вираз!'
            result /= int(new_ex[i + 1])
        elif new_ex[i] == 'помножити':
            result *= int(new_ex[i + 1])
        else:
            return 'Неправильний вираз!'
    return result
