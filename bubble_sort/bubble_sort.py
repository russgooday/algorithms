'''bubblesort function'''

def bubble_sort(lst: list) -> list:
    '''sorts list in ascending order'''
    indexes_to_be_sorted = len(lst)
    sorted_list = False

    while not sorted_list:
        sorted_list = True
        indexes_to_be_sorted -= 1

        for i in range(indexes_to_be_sorted):
            if lst[i] > lst[i + 1]:
                sorted_list = False
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

    return lst
