# 2. Создайте список, в который попадают числа,
# описывающие возрастающую последовательность.
# Порядок элементов менять нельзя.

from random import choices

def get_list(n):
    return choices(range(n*2), k = n)

def find_lists(ls):
    res_list = []
    for i in range(len(ls)):
        temp = ls[i]
        temp_ls = [temp]
        for j in range(i, len(ls)):
            if ls[j] > temp:
                temp_ls.append(ls[j])
                temp = ls[j]
        if len(temp_ls) > 1:
            res_list.append(temp_ls)
    return res_list

n = int(input("Введите длину списка: "))
ls = get_list(n)
print(ls)
print(find_lists(ls))

# Алгоритм RLE
# https://fb.ru/article/369240/algoritm-rle-opisanie-osobennosti-pravila-i-primeryi
# from os import path
# exists
# from itertools import groupby, starmap

# Эмодзи
# https://unicode-table.com/ru/emoji/

# Стратегии выигрыша
# https://informatika.shkolkovo.net/catalog/igry/prostejshie-igry-poisk-vyigryshnoj-strategii