import pytest
from merge_sort_both_directions import merge_sort

# Test cases
test_cases = [
    ([4, 2, 7, 1, 9], [1, 2, 4, 7, 9]),
    ([9, 8, 7, 6, 5], [5, 6, 7, 8, 9]),
    ([3, 3, 3, 3, 3], [3, 3, 3, 3, 3]),
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([5, 3, 9, 1, 5, 7], [1, 3, 5, 5, 7, 9]),
]

# Test cases for reverse sorting
test_cases_reverse = [
    ([4, 2, 7, 1, 9], [9, 7, 4, 2, 1]),
    ([9, 8, 7, 6, 5], [9, 8, 7, 6, 5]),
    ([3, 3, 3, 3, 3], [3, 3, 3, 3, 3]),
    ([], []),
    ([1], [1]),
    ([2, 1], [2, 1]),
    ([5, 3, 9, 1, 5, 7], [9, 7, 5, 5, 3, 1]),
]

@pytest.mark.parametrize("input_list, expected_output", test_cases)
def test_merge_sort(input_list, expected_output):
    assert merge_sort(input_list) == expected_output

@pytest.mark.parametrize("input_list, expected_output", test_cases_reverse)
def test_merge_sort_reverse(input_list, expected_output):
    assert merge_sort(input_list, reverse=True) == expected_output

# Test case for invalid reverse argument
def test_invalid_reverse():
    with pytest.raises(ValueError):
        merge_sort([1, 2, 3], reverse='invalid')

if __name__ == '__main__':
    pytest.main()
