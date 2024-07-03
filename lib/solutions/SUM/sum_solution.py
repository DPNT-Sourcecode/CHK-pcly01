# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if validate_input(x) or validate_input(y):
        raise ValueError('value out of range')
    return x + y

def validate_input(num):
    return num < 0 or num > 100


