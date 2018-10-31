from myfunctions import *


# we could also write a bunch of other tests here
def f(x):
    return x

print(mybisection(f, -3.0, 3.0, 0.001))


def test_mybisection():
    assert np.abs(mybisection(f, -3.0, 3.0, 0.001)) <= 0.001
