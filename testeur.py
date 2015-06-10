# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:33:04 2015

@author: upression1
"""
            #-------------------Scrip testeur

import os
import sys
from pyhdf.SD import SD, SDC
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
import numpy

data_in ='/home/pressions/SATELITIME/sdatats/Graph_data/'

files = os.listdir(data_in) #Liste les fichiers.
files.sort() #Trie les fichiers.

for data in files:
    i =1
    #data = numpy.load()
    print i
    print data
    i = i+1

f = os.listdir('/home/pressions/SATELITIME/sdatats/Graph_data/')  
f.sort()  
print f
print f[0]

numpy.load('/home/pressions/SATELITIME/sdatats/Graph_data/A20021852002192.chl_8d_ZI1.npy')


