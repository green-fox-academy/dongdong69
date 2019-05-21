def add(a, b):
    return a + b

def max_of_three(a, b, c):
    number_list = [a,b,c]
    return max(number_list)

def median(pool):
    pool.sort()
    return pool[int((len(pool) - 1) / 2)]

def is_vovel(char):
    return char in ['a', 'u', 'o', 'e', 'i']

def translate(hungarian):
    teve = ""

    for char in hungarian:
        if is_vovel(char):
            teve = teve + char +'v'+ char
        else:
            teve += char
    return teve
