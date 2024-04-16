def compute_LPS(needle: str)-> list:
    length = len(needle)
    lps = [0] * length
    i = 0
    j = 1

    while j < length:
        # if a match scute both pointers along 1
        if needle[j] == needle[i]:
            i += 1
            lps[j] = i
            j += 1
        # else if comparing from first char
        # scute j pointer along 1
        elif i == 0:
            j += 1
        # else if i > 0, roll back to last matched index
        else:
            i = lps[i-1]

    return lps

def KMP_Search(needle, haystack):
    lenHaystack = len(haystack)
    lenNeedle = len(needle)
    lps = compute_LPS(needle)

    i = 0
    j = 0

    while j < lenHaystack:
        if needle[i] == haystack[j]:
            i += 1
            j += 1
        elif (i == 0):
            j += 1
        else:
            i = lps[i-1]

        if (i == lenNeedle):
            return [j - lenNeedle, j]

    return -1

if __name__ == '__main__':
    print(compute_LPS('AABAAAC')) # [0, 1, 0, 1, 2, 2, 0]
    print(compute_LPS('onions')) # [0, 0, 0, 1, 2, 0]
    print(KMP_Search('onions', 'onionionslp')) # [3, 9]
    print('onionionslp'[slice(*KMP_Search('onions', 'onionionslp'))]) # onions
