# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 12:48:11 2022

@author: LENOVO
"""

import pandas as pd
from scipy import stats
df = pd.read_csv("LabTAT.csv")
df.head()
df['Laboratory 1'].mean()
df['Laboratory 2'].mean()
df['Laboratory 3'].mean()
df['Laboratory 4'].mean()
import scipy.stats as ftable
ft = ftable.f(dfn=3, dfd=476)
ft.ppf(0.95).round(4)
# Anova ftest statistics: stats.f_oneway(col-1,col-2,col-3,col-4)
F_oneway=stats.f_oneway(df.iloc[:,0],df.iloc[:,1],df.iloc[:,2],df.iloc[:,3])
F_oneway
p_val = -2.11 
# H0 = There is no difference in average TAT among the different laboratories
# H1 = There is a difference in average TAT among the different laboratories
if p_val<0.05:
    print("H0 is rejected, H1 is accepted")
else:
    print("H1 is rejected, H0 is accepted")
# Since H0 is rejected and H1 is accpeted, we can conclude that there is 
# a difference in average TAT among the different laboratories at 5% SL.