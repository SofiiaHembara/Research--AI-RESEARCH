"""Basic algoritms"""
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
    if len(lst)>1:
        left_lst = lst[:len(lst)//2]
        right_lst = lst[len(lst)//2:]
        merge_sort(left_lst)
        merge_sort(right_lst)
        i = 0
        j = 0
        k = 0
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
    res = 0
    full = len (list_of_values)
    while res < full:
        mid = (res + full)//2
        if list_of_values [mid] < value:
            res = mid + 1
        else:
            full = mid
    return res if value in list_of_values else -1

def selection_sort(lst):
    """
    Sorting list by selection way.
    >>> selection_sort([6, 3, 8, 5, 9, 1])
    [1, 3, 5, 6, 8, 9]
    """
    for ind, _ in enumerate(lst):
        min_idx = ind
        for j in range(ind+1, len (lst)) :
            if lst [j] < lst [min_idx]:
                min_idx = j
        lst [ind], lst [min_idx] = lst [min_idx], lst [ind]
    return lst
def quick_sort(lst):
    """
    Sorting list by quick way.
    >>> quick_sort([3, 7, 4, 6, 1, 9, 8])
    [1, 3, 4, 6, 7, 8, 9]
    """
    length = len(lst)
    if length <= 1:
        return lst
    else:
        pivot = lst.pop()
    items_upper = []
    items_lower = []
    for item in lst:
        if item > pivot:
            items_upper.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] +  quick_sort(items_upper)
