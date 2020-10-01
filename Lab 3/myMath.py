
def add(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def evenNum(x):
    even_list = [num for num in x if num % 2 == 0]
    return len(even_list)

def maximum(x):
    return max(x)

def minimum(x):
    return min(x)

def absolute(x):
    return abs(x)

def sumTotal(x):
    return sum(x)

def clear(x):
    cleared_list = []
    for num in x:
        cleared_list.append(0)
    return cleared_list