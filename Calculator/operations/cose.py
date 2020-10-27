import math
#from sympy import *
from scipy.misc import derivative

__all__ = ['calc_cose']

def calc_cose(x):
    #k=round(math.sin(x),2)
    print('The value after calculation is {0}'.format(math.cos(x)))
    return round(math.cos(x),2)



def derivativ_cose(x):
    #l=round(derivative(calc_sine,math.pi/3,dx=1e-9),2)
    #print('The value after calculation is {0}'.format(k))
    return round(derivative(calc_cose,x,dx=1e-9),2)



'''
if __name__ == '__main__':
    s=calc_cose(math.pi/3)
    l=derivative_cose(math.pi/3)
    print(s)
    print(l)
'''