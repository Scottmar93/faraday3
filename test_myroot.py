from myfunctions import *


# we could also write a bunch of other tests here
def test_mybisection():
    assert abs(mybisection(x, -3.0, 3.0, 0.001)) <= 0.001
