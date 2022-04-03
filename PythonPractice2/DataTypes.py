# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Работа со строками
str1 = "  This is first string   "
str2 = "This is second string"
print(str1+str2)
print(len(str1))
print(str1.title())
print(str1.lower())
print(str1.upper())
print(str1.rstrip())
print(str1.lstrip())
print(str1.strip())
print(str1.strip('0'))

print("-----")
print(str2[5]) #i
str3 = str2[0:4] #левый индекс включительно, правый - нет
print(str3)
print(str2[1:])
print(str2[:4])
print(str2[:])
print(str2[1:6:2]) #a[start:stop:step] start through not past stop, by step

#Работа с числами
a = 10/7
b = 10%7
c = 2**3
result1 = str1 + str(c)
print(a,b,c,result1)

#сложение чисел
# a, b = map(int, input("Введите два числа: ").split())
# print("Результат:",a+b)

#функция format
a = 1/3
print("{:6.2f}".format(a))
print("{:.2f}".format(a))

a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))

#Сложение чисел с функцией format
a, b = map(float, input("Введите два числа: ").split())
print("Результат: {:.3f}".format(a+b))