def sqrt(x):
    if x < 0:
        raise ValueError("Input must be a non-negative number.")
    return x ** 0.5

def degree_to_radian(degree):
    return degree * (3.14159 / 180)

def radian_to_degree(radian):
    return radian * (180 / 3.14159)

def power(base, exponent):
    return base ** exponent