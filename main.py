# chis1: int = 12398
# chis1 = 12398
from tkinter.messagebox import YES


# chis2: float = 12398.0
# chis2 = 12398.0

# stroka: str = "привет"
# stroka = "привет"

# flag: bool = False
# flag: bool = True
# flag: bool = 0 # -> False
# flag: bool = 1 # -> True

# print("hello world")

# a = input()
# print(type(a))
# print(a / 4)

# a = 1 + 2
# a = 5 * 3
# a = 15 / 3
# a = 3 - 2
# a = 5**2 # возведение в степень
# a = 15 // 2 # деление без остатка
# a = 15 % 2 # остаток от деления

# chis = 12
# ost = chis % 2 # 0
# itog = str(ost) # "0"
# a = chis // 2 # 6
# ost = a % 2 # 0
# itog = str(ost) + itog # "00"
# a = a // 2 # 3
# ost = a % 2 # 1
# itog = str(ost) + itog # "100"
# a = a // 2 # 1
# itog = str(a) + itog # "100"
# print(itog)

# a = int(input())
# if a > 0:
#     print("Положительное")
# elif a < 0:
#     print("Отрицательное")
# else:
#     print("Это 0")

# Напишите программу, которая в последовательности натуральных чисел определяет максимальное число, кратное 5. 
# Программа получает на вход 3 числа. В последовательности всегда имеется число, кратное 5. 
# Программа должна вывести одно число  — максимальное число, кратное 5.

# a = int(input())
# b = int(input())
# c = int(input())
# if a % 5 == 0: # в if равно удваивается для сравнения, а не присваивания
#     maxi = a
# if b % 5 == 0 and b > maxi: # в if равно удваивается для сравнения, а не присваивания
#     maxi = b
# if c % 5 == 0 and c > maxi: # в if равно удваивается для сравнения, а не присваивания
#     maxi = c
# print("ответ", maxi)

# for i in 23, 24, 25, 26:
#     pass

# for i in range(0, 10, 1):
#     pass

# for i in range(0, 101, 1):
#     print(i)

# a = int(input())
# for i in range(1, a + 1):
#     print(i**2)

# for i in range(0, 10, 1):
#     print(i)

# i = 0
# while i < 10:
#     print(i)
#     i = i + 1

# chis = 12
# ost = chis % 2 # 0
# itog = str(ost) # "0"
# a = chis // 2 # 6
# ost = a % 2 # 0
# itog = str(ost) + itog # "00"
# a = a // 2 # 3
# ost = a % 2 # 1
# itog = str(ost) + itog # "100"
# a = a // 2 # 1
# itog = str(a) + itog # "100"
# print(itog)

# chis = int(input()) # 2
# itog = ""
# while chis >= 1: # 2 # 1
#     ost = chis % 2 # 0 # 1
#     itog = str(ost) + itog # "0" # "10"
#     chis = chis // 2 # 1 # 0
# print(itog)

# a = int(input())
# itog = a
# while a != 0:
#     a = int(input())
#     itog += a
# print(itog)

# ex1 = "Тестовая строка"
# ex2 = "123"
# ex3 = "asdljsalkdjlskadssss"
# ex4 = str(532) # "532"

# print(len(ex1))
# print(ex1[5]) # "в"
# print(ex1[5:7]) # "ва"
# print(ex1[5:8:2]) # "вя"
# print(ex1[-2]) # "к"
# print(ex1[::-1]) # "акортс яавотсеТ"

# print(ex1.find("строка")) # 9
# print(ex1.replace("строка", "")) # Тестовая
# print(ex1.count("а")) # 2
# print(ex1.split()) # ['Тестовая', 'строка']

# class Car:
#     weight = 10
#     speed = 200

#     def __init__(self):
#         pass

#     def start_engine(self):
#         print("Машина завелась")

#     def drive(self):
#         print("Машина поехала")


# a = Car()
# a.speed
# a.start_engine()
# a.drive()

# print("w x y z")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for w in range(0, 2):
#             for z in range(0, 2):
#                 f = (not(w == (not x)) or (not(not(z) or w))) or (not y)
#                 if f == 0:
#                     print(w, x, y, z)

# [0, 170, 255]
# onePixel: list = [0, 170, 255]
# print(onePixel[1]) # 170
# onePixel[0] = 100 # замена первого элемента на 100
# print(onePixel) # [100, 170, 255]

# for i in onePixel: # перебор элементов в списке
#     print(i)

# for i in range(len(onePixel)): # перебор элементов в списке
#     print(onePixel[i])

# onePixel.append(0) # добавление нуля в список
# print(onePixel)
# onePixel.remove(0) # удаление нуля из списка
# print(onePixel)
# onePixel.append(12)
# print(onePixel)
# onePixel.pop(3) # удаление 12 из списка по позиции
# print(onePixel)
# print(onePixel[1:3]) # [170, 255]

# a: str = input() # 1 int
# spis = a.split() # разделение сроки в список
# print(spis)
# strSpiska = " ".join(spis) # соединение элементов списка в строку через пробел
# print(strSpiska)

# max(spis) # поиск максимального в списке
# min(spis) # поиск минимального в списке
# if "1" in spis: 
#     print("Элемент в списке")
# if "1" not in spis:
#     print("Элемент не в списке")
# print(spis.count('2')) # подсчёт элементов внутри списка
# print(spis.index('2')) # поиск позоции где стоит элемент

# тестовое изменение

# a = []

# for i in range(1, 101): # полный генератор списка от 1 до 100
#     a.append(i)

# print(a)

# print([i for i in range(1, 101)]) # короткий генератор списка от 1 до 100

# a = ["1", "2", "3", "4"]
# print(a)
# a = [int(i) for i in a]
# print(a)

def f(x): # Базовая математическая функция
    y = 1 * x**2 - 2 * x + 3
    print("Test") # Будет видно при вызове функции =
    return y # будет видно только если напечатать результат функции print(f(0))

def from10to2(chis, osnov):
    itog = ""
    while chis >= 1: 
        ost = chis % osnov 
        itog = str(ost) + itog 
        chis = chis // osnov
    return itog

# a = int(input())
# osnov = int(input())
# print(from10to2(a, osnov))

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

def factorial(n):
    if n == 0:
        return 1
    else:
        if n > 0:
            return n * factorial(n - 1)
        else:
            return n * factorial(n + 1)


def F(n):
    if n <= 1:
        return 0
    elif n > 1 and n % 2 == 1:
        return F(n-1) + 3*n**2
    else:
        return n/2 + F(n - 1) + 2
# print(F(22))

# a = [1, 1, 1, 2, 3, 3]
# b = {1, 2, 3, 4, 3, 3}
# print(b)

# b.add(5)

# def indexM(b, i):
#     for n, e in enumerate(b):
#         if n == i:
#             return e

# print(indexM(b, 1))

# dictionary = {
#     "Автомобиль": "Car",
#     "Кошка": "Cat",
#     "Яблоко": "Apple"
# }

# print(dictionary["Яблоко"])
# dictionary["Дверь"] = "Door"
# print(dictionary["Дверь"])
# dictionary.pop("Дверь", "Door")
# print(dictionary)
# del dictionary["Яблоко"]
# print(dictionary)

# for i in dictionary:
#     print(i, dictionary[i])

# for i in dictionary.keys():
#     print(i)

# for i in dictionary.values():
#     print(i)

# n = int(input())
# a = str(input())
# m = set()
# while a != "HELP":
#     if a == "YES":
#         x = b.split()
#         for i in x:
#             m.add(int(i))
#     elif a == "NO":
#         x = b.split()
#         for i in x:
#             if int(i) in m:
#                 m.remove(int(i))
#     else: b = a
#     a = str(input())
# print(m)