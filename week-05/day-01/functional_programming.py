from functools import reduce

list_1 = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]
even_list = filter(lambda x: x%2==0, list_1)
print(list(even_list))

squared_positives = map(lambda x: x*x, filter(lambda x: x > 0, list_1))
print(list(squared_positives))

squared_above_20 = filter(lambda x: x > 20, map(lambda x: x*x, list_1))
print(list(squared_above_20))

avg_odd = sum(list(filter(lambda x: x%2 == 1, list_1)))/len(list(filter(lambda x: x%2==1, list_1)))
print(avg_odd)

sum_numbers = reduce(lambda x, y: x+y, filter(lambda x: x%2==0 and x <= 10, list_1))
print(sum_numbers)

contain_even_numbers = any(filter(lambda x: x%2==1, list_1))
print(contain_even_numbers)

all_positive = all(map(lambda x: x>0, list_1))
print(all_positive)

def test(x):
    return x + 10

def foreach(iters, func):
    return [func(iter) for iter in iters]

print(foreach(list_1, test))

def my_map(func, iters):
    return [func(iter) for iter in iters]

def my_filter(func, iters):
    return [iter for iter in iters if func(iter)]

def fizz_buzz():
    n = 1
    while True:
        if n % 3 == 0 and n % 5 == 0:
            yield  "Fizz Buzz"
        elif n % 3 == 0:
            yield "Fizz"
        elif n % 5 == 0:
            yield "Buzz"
        else:
            yield n
        n = n + 1

a = fizz_buzz()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

def fibonacci_genertor():
    number1 = 0
    number2 = 1
    while True:
        yield number1 + number2

        number1, number2 = number2, number1 + number2


a = fibonacci_genertor()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))