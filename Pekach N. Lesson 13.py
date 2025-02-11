# Lesson 13
## Task 1

def variables_count(func):
    res = func.__code__.co_nlocals
    return res


def variables_case():
    a = 2
    b = 'test_text'

result = variables_count(variables_case)

print('Count of local variables is: ', result)

## Task 2

## Task 2

def a_func(x):
    return x * 2


def b_func(f):
    def c_func(x):
        return f(x)
    return c_func

result = b_func(a_func)
print(result(7))

## Task 3


def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):
        return square_nums(nums)
    else:
        return remove_negatives(nums)


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]