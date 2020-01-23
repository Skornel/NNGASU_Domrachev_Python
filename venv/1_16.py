import math
# значение K
k = 101
# Функция для определения простого числа
def number_is_simple(number):
    for i in range(2, int(math.sqrt(number)) + 1):

        if number % i == 0:
            return False
    return True
# Генерируем последовательность от 2 до K и находим простые числа
def gen_primes(k):
    lst = []
    for i in range(2, k + 1):
        if number_is_simple(i):
            lst.append(i)
    return lst
print(gen_primes(k))