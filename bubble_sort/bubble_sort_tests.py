from package.utils import prettify_log
from bubble_sort_callable import bubble_sort_callable
from bubble_sort import bubble_sort

def print_sorted(lst: list, title: str=''):
    sorted_list = bubble_sort(lst.copy())

    print (
        title,
        f'original: {lst}',
        f'sorted: {sorted_list}\n',
        sep = '\n'
    )

def print_sorted_callable(lst: list, fn, title: str=''):
    sorted_list = prettify_log(bubble_sort_callable(lst.copy(), fn))

    print (title, sorted_list, '', sep = '\n')

def main():
    nums = [4,5,3,2,1]
    letters =['a','h','d','e','f']
    students = [
        {'name': 'Anna', 'age': 21},
        {'name': 'Harry', 'age': 24},
        {'name': 'Lisa', 'age': 22},
        {'name': 'Thomas','age': 29}
    ]

    # bubble sort tests
    print_sorted(nums, 'Numbers ascending:')
    print_sorted(letters, 'Letters ascending:')

    # bubble sort callable tests
    print_sorted_callable(
        nums,
        lambda x, y: x < y,
        'Numbers sorted in reverse order:'
    )

    print_sorted_callable(
        students,
        lambda x, y: x['name'] > y['name'],
        'Students by name in alphabetical order:'
    )

    print_sorted_callable(
        students,
        lambda x, y: x['age'] < y['age'],
        'Students by age in descending order:'
    )

if __name__ == '__main__':
    main()