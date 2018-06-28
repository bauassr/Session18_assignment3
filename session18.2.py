# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:23:56 2018

@author: avatash.rathore
"""

import numpy as np
import pandas as pd
import scipy.stats as stats
import scipy as s
import matplotlib.pyplot as plt
import math
print("""In one state, 52% of the voters are Republicans, and 48% are Democrats. In a second
state, 47% of the voters are Republicans, and 53% are Democrats. Suppose a simple
random sample of 100 voters are surveyed from each state.
What is the probability that the survey will show a greater percentage of Republican
voters in the second state than in the first state?
      """)
print(""" let,
      p = the proportion of Republican voters in the first state
      p1 = the proportion of Republican voters in the second state 
      s_p = the proportion of Republican voters in the sample from the first state
      s_p1 = the proportion of Republican voters in the sample from the second state
      The number of voters sampled from the first state (n1) = 100,
      the number of voters sampled from the second state (n2) = 100. \n\n """)

p=0.52
p1=1 -p
s_p = 0.53
s_p1 =1- s_p
n1=100
n2=100
E = 0.52 - 0.47 
print("the mean of the difference in sample proportions: E(p1 - p2) = P1 - P2 =% .4f \n\n" % E)
Std =math.sqrt((p*p1/n1)+(s_p*s_p/n2))

print("Find the standard deviation of the difference:% .4f \n\n" % round(Std,4))

print("""This problem requires us to find the probability that p is less than p1.
      This is equivalent to finding the probability that p - p1 is less than zero. \n\n """)
Z =(0-E)/Std
print("Z-score : % .3f\n" %Z)
P_value = s.special.ndtr(Z)
print("Therefore, the probability that the survey will show a greater percentage of Republican voters in the second state than in the first state is % .2f" %P_value)