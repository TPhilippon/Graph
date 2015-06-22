# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:49:45 2015

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




         #------------ Traitement mathématique (moyenne) et sauvegarde en .npy

data_in ='/home/pressions/SATELITIME/sdatats/Graph_data/'
os.chdir(data_in)

files = os.listdir(data_in) #Liste les fichiers.
files.sort() #Trie les fichiers.
print len(files) #len = longueur de la liste de fichiers.
raw_input()
#d = {}
i = 2     #ZI concernée(s). Inclure nouvelle boucle pour x courbe sur 1 graphe.
#key = 1     #Compteur pour le dictionnaire.

print "début boucle"

day= 185
day2= 0

#for a in range (2002,2003):
#    print a
#    while day2 < 365:
#        day2= day+7
#        if day2 > 365:
#            day2 = 365
#        if a % 4 == 0 and day2 == 365:
#            day2 = 366
#
#        filen = data_in+'A'+str(a)+str(format(day,'03'))+str(a)+str(format(day2,'03'))+'.L3m_8D_CHL_chlor_a_4km_ZI'   #
#        myfile = filen+str(i)+'.npy'
for myfile in files:
    print myfile     
    data = numpy.load(myfile)
    data_mean = numpy.mean(data)
    print data_mean  
     
#numpy.save(filen+str(i)+'_mean', data_mean)
        #d[str(key)+'ZI'+str(i)] = data_mean
        #print d[str(key)+'ZI'+str(i)]
        #key = key +1
        

#        day= day+8
#    if a == 2015 and day2 == 32:
#        day2 = 365
#    day= 1
#    day2= 0


print 'fin'
