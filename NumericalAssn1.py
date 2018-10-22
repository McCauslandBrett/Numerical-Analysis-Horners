#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 14:36:53 2018

@author: Brettmccausland
"""
import math 
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import operator
from operator import itemgetter, attrgetter
from sklearn.preprocessing import Imputer
from sklearn.cross_validation import train_test_split

#precondiotion:
# The equation has been properly parsed and zero 0 coeffints have been added
# for every missing pow x includeing 0 power
#postcondition: value at x is returned
def Horners(poly_coef,x):
  sum=0
  count=len(poly_coef)
  print(poly_coef[count-1])
  for i in range(count-1):
    sum = (sum+poly_coef[i])*x
  return sum + poly_coef[count-1]

#precondiotion:
# The 
#postcondition: value at x is returned
def sin(x,accurate_to):
  stop=1
  for stop in range(1000000):
    t=(2*stop)+1
    total= ((pow(x,t)*1/math.factorial(t)))
    if(total < accurate_to):
     break           
    
  sum=0
  for i in range(stop):
    t=(2*i)+1
    sum += (pow(-1,i)*(pow(x,t)*1/math.factorial(t)))
  return sum 

def cos(x,accurate_to):
  
  stop=1
  for stop in range(1000000):
    t=(2*stop)
    total= ((pow(x,t)*1/math.factorial(t)))
    if(total < accurate_to):
     break           
    
  sum=0
  for i in range(stop):
    t=(2*i)
    sum += (pow(-1,i)*(pow(x,t)*1/math.factorial(t)))
  return sum
 
def e_tothe_negx(x,accurate_to):
  stop=1
  for stop in range(1000000):
    total= ((pow(x,stop)*1/math.factorial(stop)))
    if(total < accurate_to):
     break  
 
    
  sum=0
  neg_x = x
  print(neg_x,"-neg_x")
  for i in range(stop):
    sum += (pow(-1,i)*(pow(neg_x,i)*1/math.factorial(i)))
  return sum

#----------- Question 1 Horners ----------
l=[4,5,6,7,8]
r=Horners(l,2)
print(r)
#----------- Question 2 ----------
equResult= (cos(1,0.000000001)-e_tothe_negx(1,0.000000001))/sin(1,0.000000001)
#equResult=sin(1,0.0000000001)
print(equResult)



















