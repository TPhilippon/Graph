# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:01:09 2015

@author: upression1
"""

import os
import sys
from pyhdf.SD import SD, SDC
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
import numpy

a=10
i=0
x=1
d = {}
while a>0:
    x=x*2
    d["tour"+str(i)]=x
    i=i+1
    a=a-1

for key, value in d.iteritems():
    print key, value
    
print d['tour1']
print d['tour9']
i=4
y=int(d['tour'+str(i)])*5.5
print y




