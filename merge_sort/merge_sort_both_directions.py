''' mergesort ascending and descending '''

def merge_sort(lst: list, reverse=False) -> list:
    ''' mergesorts a list in ascending or descending order '''
    if not isinstance(reverse, bool):
        raise ValueError('reverse must be a boolean')

    reverse_order = {
        False: lambda x, y: x < y,
        True: lambda x, y: x > y
    }

    def sort(lst: list) -> list:

        if len(lst) <= 1:
            return lst

        middle = len(lst) // 2
        left = sort(lst[:middle])
        right = sort(lst[middle:])

        return merge(left, right)

    def merge(left, right):
        target = []
        left_len = len(left)
        right_len = len(right)
        i = j = 0

        while i < left_len and j < right_len:
            # depending on reverse being True or False,
            # call the appropriate function to compare the numbers
            if reverse_order[reverse](left[i], right[j]):
                target.append(left[i])
                i += 1
            else:
                target.append(right[j])
                j += 1

        # clean up remaining numbers
        while i < left_len:
            target.append(left[i])
            i += 1

        while j < right_len:
            target.append(right[j])
            j += 1

        return target

    return sort(lst)
