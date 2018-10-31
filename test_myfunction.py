from myfunctions import *


# we could also write a bunch of other tests here
def f(r):
    return r


def test_mybisection():
    assert abs(mybisection(f, -0.5, 0.55, 0.001)) <= 0.001
