from helpers import square_dif, sum_list, cross_multiple, map


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


def get_devitation_b(x_list, y_list, b):
    s_y = square_dif(y_list)
    s_x = square_dif(x_list)
    n = len(y_list)
    return 2*((s_y/s_x - b**2)/(n-2))**0.5


def get_devitation_a(x_list, dev_b):
    s_x = square_dif(x_list)
    mid_x = sum_list(x_list)/len(x_list)
    return dev_b*(s_x + mid_x**2)**0.5
