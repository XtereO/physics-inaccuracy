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


def cross_multiple(x_list, y_list):
    res = []
    for i in range(len(y_list)):
        res.append(x_list[i]*y_list[i])
    return res


def get_a(x_list, y_list, b):
    return (sum_list(y_list) - b*sum_list(x_list)) / len(y_list)


def get_b(x_list, y_list):
    n = len(y_list)
    return (sum_list(cross_multiple(x_list, y_list)) - sum_list(x_list)*sum_list(y_list)/n)/(sum_list(map(x_list, lambda x: x**2)) - (1/n)*(sum_list(x_list)**2))


def get_devitation(x_list, y_list, a, b):
    res = 0
    for i in range(len(y_list)):
        res += ((y_list[i] - a - b*x_list[i])**2)/(len(y_list) - 2)
    return res


def main():
    x_list = [
        2.5,
        6,
        8.2,
        21.2,
        22, 
        23.5,
        24.5,
        26.5
    ]
    y_list = [
        1.58,
        3.58,
        5.58,
        8.50,
        9.58,
        11.58,
        13.58,
        15.58
    ]

    b = get_b(x_list, y_list)
    a = get_a(x_list, y_list, b)
    deviatation = get_devitation(x_list, y_list, a, b)

    print("a is equal to", a)
    print("b is equal to", b)
    print("deviatation is equal to", deviatation)


if __name__ == "__main__":
    main()
