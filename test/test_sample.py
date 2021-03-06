# Testing Basics

import pytest

def add(x: int ,y: int):
    return x + y

def subtract(x: int, y: int):
    return x - y

# multiple sets of value to test a function
@pytest.mark.parametrize("x, y, result", [
    (1,2,3),
    (2,3,5),
    (5,2,7)
] )
# Unit Test for add function
def test_add(x, y, result):
    # raise assetiong exception is expected value is not returned
    assert add(x,y) == result

@pytest.mark.parametrize("x, y, result", [
    (3,2,1),
    (10,8,2),
    (5,1,4)
])
def test_subtract(x, y, result):
    
    assert subtract(x, y) == result