import math
from scipy.misc import derivative
import numpy as np

__all__ = ['calc_relue']

def calc_relue(x):
    return np.maximum(0,x)


def derivative_relu(x):
    return derivative(calc_relue,x,dx=1e-9)



'''
if __name__ == '__main__':
    q = calc_relu(np.array([[1,2,3],[4,5,6]]))
    s = derivative_relu(np.array([[1,2,3],[4,5,6]]))
    print(q)
    print(s)
'''