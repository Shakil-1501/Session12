import math
#from sympy import *
from scipy.misc import derivative

__all__ = ['calc_tane']


def calc_tane(x):
    #k=round(math.sin(x),2)
    print('The value after calculation is {0}'.format(math.tan(x)))
    return round(math.tan(x))



def derivative_tan(x):
    #l=round(derivative(calc_sine,math.pi/3,dx=1e-9),2)
    #print('The value after calculation is {0}'.format(k))
    return round(derivative(calc_tane,x,dx=1e-9),2)



'''
if __name__ == '__main__':
    s=calc_tan(math.pi/4)
    l=derivative_tan(math.pi/4)
    print(s)
    print(l)

'''
