# Lesson 26
## Task 1

def binary_search_recursive(arr, low, high, target):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search_recursive(arr, low, mid - 1, target)
        else:
            return binary_search_recursive(arr, mid + 1, high, target)
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7
result = binary_search_recursive(arr, 0, len(arr) - 1, target)
print(f"Element find on index: {result}")

## Task 2

def fibonacci_search(arr, target):
    n = len(arr)
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib_m = fib_m_minus_1 + fib_m_minus_2
    while fib_m < n:
        fib_m = fib_m_minus_1 + fib_m_minus_2
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib_m
    offset = -1
    while fib_m > 1:
        i = min(offset + fib_m_minus_2, n - 1)
        if arr[i] == target:
            return i
        elif arr[i] < target:
            fib_m = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1
            offset = i
        else:
            fib_m = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1
    if fib_m_minus_1 and arr[offset + 1] == target:
        return offset + 1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7
result = fibonacci_search(arr, target)
print(f"Element find on index: {result}")
