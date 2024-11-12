def min_of_three_vars(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c

    
if name == '__main__':
    min_of_three_vars(1, 2, 3)