def linear_search(list_of_values, value):
    """
    Searching value in list in linear way. If value is in list return its index, if not return -1.
    >>> linear_search(['sun', 'wind', 'cloud', 'fog', 'rainbow'], 'cloud')
    2
    >>> linear_search(['sun', 'wind', 'cloud', 'fog', 'rainbow'], 'rain')
    -1
    """
    for ind, val in enumerate(list_of_values):
        if val == value:
            return ind
    return -1

def merge_sort(lst):
    """
    Sorting list by merge way.
    >>> merge_sort([2, 6, 1, 8, 0, 4])
    [0, 1, 2, 4, 6, 8]
    >>> merge_sort([-56, 34, 67, 0])
    [-56, 0, 34, 67]
    """
    if len(lst) > 1:
        left_lst = merge_sort(lst[:len(lst)//2])
        right_lst = merge_sort(lst[len(lst)//2:])
        i = j = k = 0
        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] < right_lst[j]:
                lst[k] = left_lst[i]
                i += 1
            else:
                lst[k] = right_lst[j]
                j += 1
            k += 1
        while i < len(left_lst):
            lst[k] = left_lst[i]
            i += 1
            k += 1
        while j < len(right_lst):
            lst[k] = right_lst[j]
            j += 1
            k += 1
    return lst

def binary_search(list_of_values, value):
    """
    Searching value in list in binary way. If value is in list return its index, if not return -1.
    >>> binary_search([1, 3, 6, 8, 18], 8)
    3
    >>> binary_search([3, 5, 9, 23, 56, 89], 5)
    1
    >>> binary_search([4, 6, 9, 13, 78], 5)
    -1
    """
    left, right = 0, len(list_of_values) - 1
    while left <= right:
        mid = (left + right) // 2
        if list_of_values[mid] < value:
            left = mid + 1
        elif list_of_values[mid] > value:
            right = mid - 1
        else:
            return mid
    return -1

def selection_sort(lst):
    """
    Sorting list by selection way.
    >>> selection_sort([6, 3, 8, 5, 9, 1])
    [1, 3, 5, 6, 8, 9]
    """
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

def quick_sort(lst):
    """
    Sorting list by quick way.
    >>> quick_sort([3, 7, 4, 6, 1, 9, 8])
    [1, 3, 4, 6, 7, 8, 9]
    """
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
