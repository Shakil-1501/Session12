import math
import numpy as np
import pytest , os , inspect , re , random,main




def test_sine():
    r1=main.a
    #print(r1)
    assert  r1 == 0.5,"Wrong value coming"

def test_cose():
    r2=main.b
    assert r2 == 0.5,"Wrong value coming"



def test_tan():
    r10 = main.j
    assert r10 == 1.0 ,"Wrong value coming"


def test_tanh():
    r11 = main.k
    assert r11 == 0.66,"Wrong value coming"

def test_exp():
    r12=main.l
    assert r12 == 7.39,"Wrong value coming"

def test_log():
    r13=main.m
    assert r13 == 0.69,"Wrong value coming"