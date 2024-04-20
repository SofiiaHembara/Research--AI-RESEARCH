"""Basic algorithms"""


def linear_search(list_of_values, value):
    """
    Searches for a value in a list using linear search.

    Args:
        list_of_values: The list to search.
        value: The value to search for.

    Returns:
        The index of the value if found, otherwise -1.

    >>> linear_search(['sun', 'wind', 'cloud', 'fog', 'rainbow'], 'cloud')
    2
    >>> linear_search(['sun', 'wind', 'cloud', 'fog', 'rainbow'], 'rain')
    -1
    """
    for i, val in enumerate(list_of_values):
        if val == value:
            return i
    return -1


def merge_sort(lst):
    """
    Sorts a list using the merge sort algorithm.

    Args:
        lst: The list to sort.

    Returns:
        The sorted list.

    >>> merge_sort([2, 6, 1, 8, 0, 4])
    [0, 1, 2, 4, 6, 8]
    >>> merge_sort([-56, 34, 67, 0])
    [-56, 0, 34, 67]
    """
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])

    return merge(left_half, right_half)


def merge(left_half, right_half):
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left_half: The first sorted list.
        right_half: The second sorted list.

    Returns:
        The merged and sorted list.
    """
    i, j, k = 0, 0, 0
    merged_list = [None] * (len(left_half) + len(right_half))

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged_list[k] = left_half[i]
            i += 1
        else:
            merged_list[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        merged_list[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        merged_list[k] = right_half[j]
        j += 1
        k += 1

    return merged_list


def binary_search(list_of_values, value):
    """
    Searches for a value in a sorted list using binary search.

    Args:
        list_of_values: The sorted list to search.
        value: The value to search for.

    Returns:
        The index of the value if found, otherwise -1.

    >>> binary_search([1, 3, 6, 8, 18], 8)
    3
    >>> binary_search([3, 5, 9, 23, 56, 89], 5)
    1
    >>> binary_search([4, 6, 9, 13, 78], 5)
    -1
    """
    low = 0
    high = len(list_of_values) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        if list_of_values[mid] < value:
            low = mid + 1
        elif list_of_values[mid] > value:
            high = mid - 1
        else:
            return mid

    return -1


def selection_sort(lst):
    """
    Sorts a list using the selection sort algorithm.

    Args:
        lst: The list to sort.

    Returns:
        The sorted list.

    >>> selection_sort([6, 3, 8, 5, 9, 1])
    [1, 3, 5, 6, 8, 9]
    """
    for ind, _ in enumerate(lst):
        min_idx = ind
        for j in range(ind + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[ind], lst[min_idx] = lst[min_idx], lst[ind]
    return lst


def quick_sort(lst):
    """
    Sorts a list using the quick sort algorithm.

    Args:
        lst: The list to sort.

    Returns:
        The sorted list.

    >>> quick_sort([3, 7, 4, 6, 1, 9, 8])
    [1, 3, 4, 6, 7, 8, 9]
    """
    if len(lst) <= 1:
        return lst

    pivot = lst[0]  # Choose the first element as the pivot (can be random too)
    left, right = [], []

    for item in lst[1:]:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)

    return quick_sort(left) + [pivot] + quick_sort(right)
