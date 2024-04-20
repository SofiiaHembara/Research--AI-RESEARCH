from itertools import combinations_with_replacement
from functools import reduce  # Adding this import

def partitions(n):
    if n == 0:
        yield []
        return
    for p in partitions(n - 1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            p[0] += 1
            yield p

def part(n):
    products = set()
    for partition in partitions(n):
        products.add(reduce(lambda x, y: x * y, partition, 1))
    products = sorted(products)
    length = len(products)
    median = (products[length // 2] + products[(length - 1) // 2]) / 2
    average = sum(products) / length
    return "Range: {} Average: {:.2f} Median: {:.2f}".format(products[-1] - products[0], average, median)

# Test cases
print(part(5))  # Example for n = 5
print(part(8))
