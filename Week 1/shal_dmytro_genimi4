from itertools import combinations_with_replacement

def partition(n):
    # Generate partitions of n
    partitions = []
    for k in range(1, n + 1):
        for combo in combinations_with_replacement(range(1, n + 1), k):
            if sum(combo) == n:
                partitions.append(list(combo))
    return partitions

def prod(partitions):
    # Calculate products of partitions
    products = []
    for partition in partitions:
        product = 1
        for num in partition:
            product *= num
        products.append(product)
    return sorted(list(set(products)))

def stats(products):
    # Calculate range, average, and median
    prod_len = len(products)
    prod_sum = sum(products)
    prod_min = min(products)
    prod_max = max(products)
    prod_avg = prod_sum / prod_len
    if prod_len % 2 == 0:
        prod_median = (products[prod_len // 2 - 1] + products[prod_len // 2]) / 2
    else:
        prod_median = products[prod_len // 2]
    return f"Range: {prod_max - prod_min} Average: {prod_avg:.2f} Median: {prod_median:.2f}"

def part(n):
    partitions = partition(n)
    products = prod(partitions)
    return stats(products)

# Test cases
print(part(5))  # Example test case
