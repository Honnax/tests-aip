def task_1(two_dim_words):
    """
        Здесь должен быть ваш код.
        Переменная two_dim_words - ваш двумерный список.
        Заполнять список значениями не нужно.
        Финальное значение должно быть помещено в переменную sorted_words.
        """

    return sorted_words

def task_4_1(words):
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    return res


def task_4_2(words):  # можно сделать тесты
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    return res


def task_4_3(words):
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    return res


def task_5(lst1, lst2):
    """
        Здесь должен быть ваш код.
        Переменные lst1 и lst2 - два данных списка.
        Финальное значение должно быть помещено в переменную diff.
        """
list1 = [2, 5, 8, 7, 6, 1, 2]
list2 = [7, 3, 1, 2, 6, 9, 4]
set1 = set(list1)
set2 = set(list2)
set3 = set(list1)
set3 &= set2
set1 = set1.difference(set3)
list3 = list(set1)
list3.sort()
print(list3)

    return diff


def task_6(lst):
    """
        Здесь должен быть ваш код.
        Переменная lst - ваш список.
        Финальное значение должно быть помещено в переменную res.
        """
list1 = [1, 43, 5, 34, 3]
set1 = set(list1)
list2 = list(set1)
list2.sort(reverse=True)
tuple1 = tuple(list2)
print(tuple1)


    return res

