from random import randint

def get_random_values():
    a = randint(1, 10000)
    b = randint(1, 10000)
    c = randint(1, 10000)
    print(f"Random values: a = {a}, b = {b}, c = {c}")
    return (a, b, c)

def determine_largest_variable(values):
    a, b, c = values
    if a >= b and a >= c:
        return 'a'
    elif b >= a and b >= c:
        return 'b'
    else:
        return 'c'

def test_determine_largest_variable():
    values = get_random_values()
    largest = max(values)
    expected = 'a' if largest == values[0] else 'b' if largest == values[1] else 'c'
    assert determine_largest_variable(values) == expected
