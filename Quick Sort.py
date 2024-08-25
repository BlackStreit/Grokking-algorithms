import random

arr = [1, 5, 3, 5, 2]

def sum1(arr):
    """
    Рекурсивно вычисляет сумму элементов списка.

    Аргументы:
    arr -- список элементов

    Возвращает:
    Сумму элементов списка.
    """
    if len(arr) == 0:
        return 0  # Базовый случай: если список пуст, возвращаем 0
    else:
        return arr[0] + sum1(arr[1:])  # Рекурсивный случай: первый элемент + сумма оставшихся элементов

#print(sum1(arr))  # Ожидаемый результат: 30

def arr_count(arr):
    """
    Рекурсивно считает количество элементов в списке.

    Аргументы:
    arr -- список элементов

    Возвращает:
    Количество элементов в списке.
    """
    if len(arr) == 0:
        return 0  # Базовый случай: если список пуст, возвращаем 0
    else:
        return 1 + arr_count(arr[1:])  # Рекурсивный случай: 1 (текущий элемент) + количество оставшихся элементов

def find_max(arr):
    """
    Рекурсивно находит максимальный элемент в списке.

    Аргументы:
    arr -- список элементов

    Возвращает:
    Максимальный элемент в списке.
    """
    if len(arr) == 1:
        return arr[0]  # Базовый случай: если в списке один элемент, возвращаем его
    else:
        max_of_rest = find_max(arr[1:])  # Рекурсивный случай: находим максимум в оставшейся части списка
        return arr[0] if arr[0] > max_of_rest else max_of_rest  # Сравниваем первый элемент с максимумом оставшейся части
	
	
def quicksort(arr):
    """
    Выполняет быструю сортировку списка.

    Аргументы:
    arr -- список элементов

    Возвращает:
    Новый отсортированный список.
    """
    if len(arr) <= 1:
        return arr  # Базовый случай: если список пуст или содержит один элемент, он уже отсортирован
    else:
        pivot = arr[len(arr) // 2]  # Выбираем опорный элемент (pivot)
        left = [x for x in arr if x < pivot]  # Все элементы меньше опорного
        middle = [x for x in arr if x == pivot]  # Все элементы равные опорному
        right = [x for x in arr if x > pivot]  # Все элементы больше опорного
        return quicksort(left) + middle + quicksort(right)  # Рекурсивно сортируем подмассивы и объединяем их

# Пример использования
arr = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(arr))  # Ожидаемый результат: [1, 1, 2, 3, 6, 8, 10]


def merge_sort(arr):
    """
    Выполняет сортировку слиянием списка.

    Аргументы:
    arr -- список элементов

    Возвращает:
    Новый отсортированный список.
    """
    if len(arr) <= 1:
        return arr  # Базовый случай: если список пуст или содержит один элемент, он уже отсортирован

    # Разделяем список на две половины
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно сортируем каждую половину
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Сливаем отсортированные половины
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    Сливает два отсортированных списка в один отсортированный список.

    Аргументы:
    left -- первый отсортированный список
    right -- второй отсортированный список

    Возвращает:
    Новый отсортированный список, содержащий элементы из обоих списков.
    """
    result = []
    i = j = 0

    # Сливаем списки, пока есть элементы в обоих списках
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы из левого списка
    result.extend(left[i:])
    # Добавляем оставшиеся элементы из правого списка
    result.extend(right[j:])

    return result

# Пример использования
print(merge_sort(arr))  # Ожидаемый результат: [1, 1, 2, 3, 6, 8, 10]
