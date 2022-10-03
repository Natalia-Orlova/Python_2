# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.


number = int(input("Enter the number "))
num = 1
for i in range(number):
    print(num, end=", ")
    num *= -3


