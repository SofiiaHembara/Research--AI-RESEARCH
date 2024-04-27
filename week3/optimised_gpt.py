"""
calculation
"""
def find_max_1(f, points):
    """ 
    (function, list(number)) -> (number)
    
    Find and return maximal value of function f in points.
    
    >>> find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12
    """
    return max(map(f, points))

def find_max_2(f, points):
    """ 
    (function, list(number)) -> (number
    
    Find and return list of points where function f has the maximal value.
    
    >>> find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    [3]
    """
    maximal = max(map(f, points))
    return [point for point in points if f(point)==maximal]

def compute_limit(seq):
    """
    (function) -> (number)
    
    Compute and return limit of a convergent sequence.
    
    >>> compute_limit(lambda n: (n ** 2 + n) / n ** 2)
    1.0
    """
    lst = []
    i = 0
    while True:
        n = 10 ** i
        lst.append(seq(n))
        if i != 0 and abs(lst[i] - lst[i - 1]) < 0.001:
            return round(lst[i], 2)
        i += 1

def compute_derivative(f, x_0):
    """
    (function, number) -> (number)
    
    Compute and return derivative of function f in the point x_0.
    
    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.0
    """
    dx = 1.0
    aprox = []
    i = 0
    while True:
        x = x_0 + dx
        dF = f(x)
        x = x_0
        dF -= f(x)
        der = dF / dx
        aprox.append(der)
        if i != 0 and abs(aprox[i] - aprox[i - 1]) < 0.001:
            return round(aprox[i], 2)
        i += 1
        dx /= 10.0

def get_tangent(f, x_0):
    """
    (function, number) -> (str)
    
    Compute and return tangent line to function f in the point x_0.
    
    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '- 3.0 * x + 4.0'
    """
    a = compute_derivative(f, x_0)
    b = f(x_0) - a * x_0
    if b == 0:
        equation = f"{abs(round(a, 2))} * x"
    else:
        equation = f"{'- ' if a < 0 else ''}{abs(round(a, 2))} * x {'-' if b < 0 else '+'} {abs(round(b, 2))}"
    return equation

def get_root(f, a, b):
    """
    (function, number, number) -> (number)
    
    Compute and return root of the function f in the interval (a, b).
    
    >>> get_root(lambda x: x, -1, 1)
    0.0
    """
    tolerance = 1e-6
    if f(a) * f(b) >= 0:
        raise ValueError("The function values at endpoints must have opposite signs.")
    while (b - a) / 2 > tolerance:
        c = (a + b) / 2
        if f(c) == 0:
            return round(c, 2)
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    root = (a + b) / 2
    return round(root, 2)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

