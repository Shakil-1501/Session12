import math
#from sympy import *
from scipy.misc import derivative

__all__ = ['calc_loge']

def calc_loge(x):
    #k=round(math.sin(x),2)
    #print('The value after calculation is {0}'.format(k))
    return round(math.log(x),2)



def derivative_log(x):
    #l=round(derivative(calc_sine,math.pi/3,dx=1e-9),2)
    #print('The value after calculation is {0}'.format(k))
    return derivative(calc_loge,x,dx=1e-9)



'''
if __name__ == '__main__':
    s=calc_log(2)
    l=derivative_log(2)
    print(s)
    print(l)
'''