import math

def manhattan(x, y):
    return sum(abs(val1-val2) for val1, val2 in zip(x,y))