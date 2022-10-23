import sys
import re

numbers = input("Введите последовательность чисел через пробел")
pattern = re.compile(r'((-?\d+\.?\d*)\s)*(-?\d+\.?\d*)')
def isValid(numbers):
    if re.fullmatch(pattern, numbers):
        pass
    else:
        print("Введенное число не соответствует заданному условию")
        sys.exit()
    return

isValid(numbers)

num = input("Введите любое число, входящее в последовательность")
if float(num) or int(num):
    pass
else:
    print("Введенное число не соответствует заданному условию")
    sys.exit()
num = float(num)

numbers = numbers.replace(" ",",")
numbers = numbers.split(",")
numbers = list(numbers)

numbers = [float(x) for x in numbers]

def sort(array:list):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if float(array[j]) > float(array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
    print(array)
    return array

sort(numbers)

def binary_search (a: float, array: list):
    if a > array[0] and a < array [-1]:
        left, right = 0, len(array)
        while left < right:
            middle = (right + left) // 2
            if array[middle] < a:
                left = middle + 1
            else:
                right = middle
        if float(array [left - 1]) < a and float(array [left + 1]) >= a:
            print(array[left-1])
        else:
            print("Введенное число не соответствует заданному условию")
    else:
        print("Введенное число не соответствует заданному условию")
    return

binary_search(num, numbers)