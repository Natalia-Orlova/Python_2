# 1. Создайте список из N натуральных чисел(0 до N),
# упорядоченных по возрастанию. Среди чисел не хватает
# одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.

from random import choice

def fill_list(num):
    array = [i for i in range(num+1)]
    array.remove(choice(array))
    return array

def check_number(array):
    for i in range(1, len(array)):
        if array[i] - 1 != array[i - 1]:
            return array[i] - 1
    return -1

array = fill_list(int(input("Enter the positive number: ")))
print(array)
print(check_number(array))













#к дз

# from itertools import groupby, starmap
# from os import path


# def rle_encode(text="text_words.txt", code_text="text_code_words.txt"):
#     if path.exists(text) and not path.exists(code_text):
#         with open(text) as my_f_1, \
#                 open(code_text, "a") as my_f_2:
#             for i in my_f_1:
#                 my_f_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
#     else:
#         print("The files do not exist in the system!")
