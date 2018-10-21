#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 14:36:53 2018

@author: Brettmccausland
"""

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

#----------- Question 1 Horners ----------
l=[4,5,6,7,8]
r=Horners(l,2)
print(r)
#----------- Question 2 ----------