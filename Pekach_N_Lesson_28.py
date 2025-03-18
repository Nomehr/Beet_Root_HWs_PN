# Lesson 28
## Task 1

def bubble_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        start += 1


arr = [9, 0, 8, 1, 7, 2, 6, 3, 5]
bubble_sort(arr)
print(arr)

## Task 2

def merge_sort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    temp = []
    i, j = left, mid + 1

    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for k in range(len(temp)):
        arr[left + k] = temp[k]


arr = [8, 9, 3, 7, 6, 5, 2, 1]
merge_sort(arr, 0, len(arr) - 1)
print(arr)

## Task 3

import random

INSERTION_SORT_THRESHOLD = 10

def insert_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quick_sort(arr, left, right):
    if right - left + 1 <= INSERTION_SORT_THRESHOLD:
        insert_sort(arr, left, right)
        return

    pivot = partition(arr, left, right)
    quick_sort(arr, left, pivot - 1)
    quick_sort(arr, pivot + 1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


arr = [random.randint(0, 100) for _ in range(50)]
quick_sort(arr, 0, len(arr) - 1)
print(arr)

'''
Маленький список → InsertionSort
Почти отсортирован → CocktailSort
Огромный массив → MergeSort без slice / QuickSort + InsertionSort
'''