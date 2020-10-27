import math
#from sympy import *
from scipy.misc import derivative
import numpy as np

__all__ = ['calc_sigmoide']


def calc_sigmoide(x):
    return 1/(1+np.exp(-x))


def derivative_sigmoid(x):
    return derivative(calc_sigmoide,x,dx=1e-9)



'''
if __name__ == '__main__':
    q = calc_sigmoid(np.array([[1,2,3],[4,5,6]]))
    s = derivative_sigmoid(np.array([[1,2,3],[4,5,6]]))
    print(q)
    print(s)

'''