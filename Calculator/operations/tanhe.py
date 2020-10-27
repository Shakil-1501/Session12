import math
#from sympy import *
from scipy.misc import derivative

__all__ = ['calc_tanhe']


def calc_tanhe(x):
    #k=round(math.sin(x),2)
    print('The value after calculation is {0}'.format(math.tanh(x)))
    return round(math.tanh(x),2)



def derivative_tanh(x):
    #l=round(derivative(calc_sine,math.pi/3,dx=1e-9),2)
    #print('The value after calculation is {0}'.format(k))
    return round(derivative(calc_tanhe,x,dx=1e-9),2)



'''
if __name__ == '__main__':
    s=calc_tanh(math.pi/4)
    l=derivative_tanh(math.pi/4)
    print(s)
    print(l)
'''