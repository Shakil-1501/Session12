import Calculator
import math
import numpy as np
from Calculator.operations.cose import derivativ_cose
from Calculator.operations.sine import derivative_sine 
from Calculator.operations.tane import derivative_tan
from Calculator.operations.tanhe import derivative_tanh
from Calculator.operations.ee import derivative_exp
from Calculator.operations.loge import derivative_log
from Calculator.operations.relue import derivative_relu
from Calculator.operations.softmaxe import derivative_softmax
from Calculator.operations.sigmoide import derivative_sigmoid

'''
print(Calculator.calc_sine(math.pi/6))
print(Calculator.calc_cose(math.pi/3))
print(derivative_sine(math.pi/6))
print(derivativ_cose(math.pi/6))
print(derivative_tan(math.pi/4))
print(derivative_tanh(math.pi/4))
print(derivative_exp(2))
print(derivative_log(2))
print(derivative_sigmoid(np.array([[1,2,3],[4,5,6]])))
print(derivative_relu(np.array([[1,2,3],[4,5,6]])))
print(derivative_softmax(np.array([[1,2,3],[4,5,6]])))
print(Calculator.calc_tane(math.pi/4))
print(Calculator.calc_tanhe(math.pi/4))
print(Calculator.calc_expe(2))
print(Calculator.calc_loge(2))
print(Calculator.calc_sigmoide(np.array([[1,2,3],[4,5,6]])))
print(Calculator.calc_relue(np.array([[1,2,3],[4,5,6]])))
print(Calculator.calc_softmaxe(np.array([[1,2,3],[4,5,6]])))
'''

a= Calculator.calc_sine(math.pi/6)
b= Calculator.calc_cose(math.pi/3)
c= derivative_sine(math.pi/6)
d= derivativ_cose(math.pi/6)
e= derivative_tan(math.pi/4)
f= derivative_tanh(math.pi/4)
g= derivative_exp(2)
h= derivative_log(2)
i= derivative_sigmoid(np.array([[1,2,3],[4,5,6]]))
j= Calculator.calc_tane(math.pi/4)
k= Calculator.calc_tanhe(math.pi/4)
l= Calculator.calc_expe(2)
m= Calculator.calc_loge(2)
n= Calculator.calc_sigmoide(np.array([[1,2,3],[4,5,6]]))
o= Calculator.calc_relue(np.array([[1,2,3],[4,5,6]]))
p= Calculator.calc_softmaxe(np.array([[1,2,3],[4,5,6]]))
q= derivative_relu(np.array([[1,2,3],[4,5,6]]))
r= derivative_softmax(np.array([[1,2,3],[4,5,6]]))


#print(a)
#print(b)
#print(c)
#print(d)



