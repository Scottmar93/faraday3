import numpy as np
import matplotlib.pyplot as plt


def myfunc(x):
    """
    Returns the value of the defined function at the input point x
    
    Parameters
    -----------
    x : float, int
        Point at which function is to be evaluated
    
    Returns
    ---------
    y : float
        Function value at input point x
    
    """
    
    y = -(x - 2)**2 + 4
    return y


def mytrapz(x,y):
    """
    Calculates approximation to the integral of a function over the domain with spatial points :math:`x` using the trapezium rule.
    The spacing between spatial points is assumed uniform with grid size :math:`h` and the integral :math:`I` is approximated by
    
    .. math::
       
       I = \\frac{h}{2}(y_{0} + y_{N} + 2\\sum_{i=1}^{N-1} y_{i})

    
    where :math:`h` is calculated by :math:`x_1-x_0`.

    Parameters
    ----------
    x : float
        Spatial points for the domain of integration. Grid size is assumed uniform and calculated by :math:`x_1-x_0`.
    
    y : float
        Function points calculated at the spatial points in :math:`x`. Each element of the list :math:`y_i` is the function evaluated at :math:`x_i`.

    Returns
    -------
    result : float
        Approximation to the integral of the function.
    
    """
    
    h = x[1] - x[0]
    result = 0.5*h*(y[0] + y[-1] + 2*np.sum(y[1:-1]))
    return result


"""
# Choose integration limits (a,b) and number of points N
a = 0
b = 4
N = 100

# Integrate myfunc using mytrapz
x = np.linspace(a, b, N)
y = myfunc(x)
integral = mytrapz(x, y)
print(integral)

plt.plot(x, y)
plt.title('A plot of the function to be integrated')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
"""
