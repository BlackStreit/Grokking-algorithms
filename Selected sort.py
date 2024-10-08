# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:45:05 2024

@author: Admin
"""

def findSmaller(arr):
    """
    Находит индекс наименьшего элемента в списке.

    Аргументы:
    arr -- список элементов

    Возвращает:
    Индекс наименьшего элемента в списке.
    """
    smallest = arr[0]  # Инициализируем наименьший элемент первым элементом списка
    smallest_index = 0  # Инициализируем индекс наименьшего элемента

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i  # Обновляем индекс наименьшего элемента
            smallest = arr[i]  # Обновляем наименьший элемент

    return smallest_index  # Возвращаем индекс наименьшего элемента

def selectionSort(arr):
    """
    Сортирует список методом выбора.

    Аргументы:
    arr -- список элементов

    Возвращает:
    Новый отсортированный список.
    """
    newArr = []  # Создаем новый список для отсортированных элементов

    for i in range(len(arr)):
        smallest = findSmaller(arr)  # Находим индекс наименьшего элемента
        newArr.append(arr.pop(smallest))  # Удаляем наименьший элемент из исходного списка и добавляем его в новый список

    return newArr  # Возвращаем отсортированный список

print(selectionSort([5, 3, 6, 2, 10]))  # Ожидаемый результат: [2, 3, 5, 6, 10]


