def merge_sort(lst: list) -> list:

    if (len(lst) == 1):
        return lst

    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])

    return merge(left, right)

def merge(left, right):
    # print(f'left: {left}, right: {right}')
    target = []
    leftLen = len(left)
    rightLen = len(right)
    i = j = 0

    while i < leftLen and j < rightLen:
        if left[i] < right[j]:
            target.append(left[i])
            i += 1
        else:
            target.append(right[j])
            j += 1

    # clean up remaining numbers
    while i < leftLen:
        target.append(left[i])
        i += 1

    while j < rightLen:
        target.append(right[j])
        j += 1

    return target

print(merge_sort([9, 12, 15, 2, 6, 7, 11]))
