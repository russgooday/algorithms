def merge_sort(lst: list) -> list:
    if len(lst) <= 1:
        return lst

    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])

    return merge(left, right)

def merge(left, right):
    target = []
    left_len = len(left)
    right_len = len(right)
    i = j = 0

    while i < left_len and j < right_len:
        if left[i] < right[j]:
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
