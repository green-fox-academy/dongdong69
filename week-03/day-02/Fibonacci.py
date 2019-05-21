def fibonacci(index):
    number1 = 0
    number2 = 1

    if index is 0:
        return 0
    if index is 1:
        return 1
    
    for i in range(index-1):
        result = number1 + number2
        number1, number2 = number2, result

    return result