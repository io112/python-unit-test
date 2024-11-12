def min_of_three_vars(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c


def main():
    min_of_three_vars(1, 2, 3)

if name == '__main__':
    main()