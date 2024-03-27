'''bubble sort with optional comparator function'''

def swap(obj, x, y):
    '''swaps key values of object'''
    obj[x], obj[y] = obj[y], obj[x]
    return obj

def bubble_sort_callable(lst: list, comparator = None) -> list:
    '''sorts a list in order by comparator function'''

    # default comparator
    def compare_ascending(x, y):
        return x > y

    if comparator:
        if not callable(comparator):
            raise TypeError('The comparator must be a function')
    else:
        comparator = compare_ascending

    indexes_to_be_sorted = len(lst)
    sorted_list = False

    while not sorted_list:
        sorted_list = True
        indexes_to_be_sorted -= 1

        for i in range(indexes_to_be_sorted):
            if comparator(lst[i], lst[i + 1]):
                swap(lst, i, i + 1)
                sorted_list = False

    return lst
