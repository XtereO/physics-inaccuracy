from MLS import get_a, get_b, get_devitation, get_devitation_a, get_devitation_b
from helpers import cross_multiple, for_each, map


def calculate_MLS():
    x_list = [
        13.23,
        11.19,
        9.90,
        8.82,
        7.90,
        7.35,
        6.64,
        6.22,
        5.82,
        5.43,
        4.95,
        4.69,
        4.47,
        4.24,
        4.19
    ]
    y_list = [
        0.0,
        0.15323870451819271,
        0.25172296915602754,
        0.3332910589727331,
        0.40266175845957813,
        0.4451377263734592,
        0.49882075471698106,
        0.5301204819277108,
        0.5604458965981164,
        0.5906468891635764,
        0.624180790960452,
        0.6465537801097067,
        0.6621621621621622,
        0.6802110817941953,
        0.6833956219967966,
    ]

    if(len(x_list) != len(y_list)):
        raise Exception(f"Lengths are different: x is {x_list}, y is {y_list}")

    b = get_b(x_list, y_list)
    a = get_a(x_list, y_list, b)
    dev_b = get_devitation_b(x_list, y_list, b)
    dev_a = get_devitation_a(x_list, dev_b)
    devitation = get_devitation(x_list, y_list, a, b)

    print("a is equal to", a)
    print("b is equal to", b)
    print("devitation a is equal to", dev_a)
    print("devitation b is equal to", dev_a)
    print("devitation y is equal to", devitation)


def divide_list():
    x = [
        17,
        14.4,
        11.0,
        8.0,
        7.0,
        6.0,
        4.4,
        4.0,
        3.2,
        2.6,
        2.0,
        1.4,
        1.2,
        1.0,
        0.8
    ]
    for_each(map(x, lambda x: x/50), lambda x: print(x))


def mult_list():
    x_list = [
        13.23,
        11.19,
        9.90,
        8.82,
        7.90,
        7.35,
        6.64,
        6.22,
        5.82,
        5.43,
        4.95,
        4.69,
        4.47,
        4.24,
        4.19
    ]
    k = 0.68
    for_each(map(x_list, lambda x: (x**2)*k), lambda x: print(x))


def cross_mult_lists():
    x_list = [
        0,
        15.33,
        22.28,
        26.28,
        28.44,
        29.25,
        29.61,
        29.48,
        29.16,
        28.67,
        27.62,
        27.11,
        26.46,
        25.78,
        25.60
    ]
    y_list = [
        118.28,
        100.04,
        88.51,
        78.85,
        70.63,
        65.71,
        59.36,
        55.61,
        52.03,
        48.54,
        44.25,
        41.93,
        39.96,
        37.90,
        37.46
    ]

    for_each(cross_multiple(x_list, map(
        y_list, lambda x: 1/x)), lambda x: print(x))


if __name__ == "__main__":
    calculate_MLS()
