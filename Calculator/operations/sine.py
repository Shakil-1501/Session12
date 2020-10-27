import math
#from sympy import *
from scipy.misc import derivative

__all__ = ['calc_sine']


def calc_sine(x):
    #k=round(math.sin(x),2)
    print('The value after calculation is {0}'.format(math.sin(x)))
    return round(math.sin(x),2)



def derivative_sine(x):
    #l=round(derivative(calc_sine,math.pi/3,dx=1e-9),2)
    #print('The value after calculation is {0}'.format(k))
    return round(derivative(calc_sine,x,dx=1e-9),2)



'''
if __name__ == '__main__':
    s=calc_sine(math.pi/3)
    l=derivative_sine(math.pi/3)
    print(s)
    print(l)

'''