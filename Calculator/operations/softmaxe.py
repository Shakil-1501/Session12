import math
from scipy.misc import derivative
import numpy as np

__all__ = ['calc_softmaxe']

def calc_softmaxe(x):
    expo = np.exp(x)
    expo_sum = np.sum(np.exp(x))
    return expo/expo_sum


def derivative_softmax(x):
    return derivative(calc_softmaxe,x,dx=1e-9)



'''
if __name__ == '__main__':
    q = calc_softmax(np.array([[1,2,3],[4,5,6]]))
    s = derivative_softmax(np.array([[1,2,3],[4,5,6]]))
    print(q)
    print(s)
'''