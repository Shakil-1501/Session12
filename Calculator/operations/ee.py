import math
#from sympy import *
from scipy.misc import derivative

__all__ = ['calc_expe']

def calc_expe(x):
    #k=round(math.sin(x),2)
    print('The value after calculation is {0}'.format(math.exp(x)))
    return round(math.exp(x),2)



def derivative_exp(x):
    #l=round(derivative(calc_sine,math.pi/3,dx=1e-9),2)
    #print('The value after calculation is {0}'.format(k))
    return derivative(calc_expe,x,dx=1e-9)



'''
if __name__ == '__main__':
    s=calc_exp(2)
    l=derivative_exp(2)
    print(s)
    print(l)
'''