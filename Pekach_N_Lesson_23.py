# Lesson 23

def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:  # O(n)
        if el_first_list in second_list:  # O(n) (поиск в списке)
            res.append(el_first_list)  # O(1)
    return res


'''
Внешний цикл выполняется n раз.    
Внутри цикла происходит поиск элемента в списке second_list, что занимает O(n).
Итоговая сложность: O(n * n) = O(n²).
Ответ: 2 - n².
'''


def question2(n: int) -> int:
    for _ in range(10):  # Фиксированное число итераций (10)
        n **= 3  # O(1)
    return n


'''
Цикл выполняется 10 раз, независимо от размера входных данных.
Каждая операция возведения в степень занимает O(1).
Итоговая сложность: O(1).
Ответ: 5 - 1.
'''


def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    temp: List[int] = first_list[:]  # O(n)
    for el_second_list in second_list:  # O(n)
        flag = False
        for check in temp:  # O(n)
            if el_second_list == check:  # O(1)
                flag = True
                break
        if not flag:
            temp.append(second_list)  # O(1)
    return temp


'''
Внешний цикл выполняется n раз.
Внутренний цикл также выполняется n раз.
Итоговая сложность: O(n * n) = O(n²).
Ответ: 4 - n².
'''


def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:  # O(n)
        if el > res:  # O(1)
            res = el  # O(1)
    return res


'''
Один цикл, который выполняется n раз.
Итоговая сложность: O(n).
Ответ: 3 - n.
'''

def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):  # O(n)
        for j in range(n):  # O(n)
            res.append((i, j))  # O(1)
    return res


'''
Внешний цикл выполняется n раз.
Внутренний цикл также выполняется n раз.
Итоговая сложность: O(n * n) = O(n²).
Ответ: 2 - n².
'''


def question6(n: int) -> int:
    while n > 1:  # O(log n)
        n /= 2  # O(1)
    return n


'''
На каждой итерации значение n уменьшается в 2 раза.
Количество итераций: log₂(n).
Итоговая сложность: O(log n).
Ответ: 1 - log n.
'''