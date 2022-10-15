def sum_list(l):
    res = 0
    for i in l:
        res += i
    return res


def map(l, func):
    res = []
    for i in l:
        res.append(func(i))
    return res

def for_each(l, func):
    for i in l: 
        func(i)

def cross_multiple(x_list, y_list):
    res = []
    for i in range(len(y_list)):
        res.append(x_list[i]*y_list[i])
    return res

def square_dif(l): 
    n = len(l)
    return sum_list(map(l, lambda x: x**2))/n - (sum_list(l)/n)**2