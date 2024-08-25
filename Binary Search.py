# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:52:29 2024

@author: Admin
"""

def binary_search(data, value):
    """
    Выполняет бинарный поиск значения в отсортированном списке.

    Аргументы:
    data -- отсортированный список элементов
    value -- значение, которое нужно найти

    Возвращает:
    Индекс элемента, если значение найдено, иначе None.
    """
    low = 0  # Начальный индекс
    high = len(data) - 1  # Конечный индекс

    while low <= high:
        mid = (low + high) // 2  # Средний индекс
        guess = data[mid]  # Предполагаемое значение

        if guess == value:
            return mid  # Значение найдено, возвращаем индекс
        elif guess > value:
            high = mid - 1  # Ищем в левой половине
        else:
            low = mid + 1  # Ищем в правой половине

    return None  # Значение не найдено

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))  # Ожидаемый результат: 1
print(binary_search(my_list, -1))  # Ожидаемый результат: None
