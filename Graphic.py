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




         #------------ Traitement mathématique et graphique

data_in ='/home/pressions/SATELITIME/sdatats/Graph_data/'

#files = os.listdir(data_in) #Liste les fichiers.
#files.sort() #Trie les fichiers.
#print len(files) #len = longueur de la liste de fichiers.

d = {}
i = 1       #.
j = 1       #Nombre de ZI choisies dans le script précédent.
key = 1     #Compteur pour le dictionnaire.

for myfile in data_in:
 
    while i <= j:

        if myfile.endswith("ZI"+str(i)+".npy"):
            
            print myfile            
            data = myfile
            data_mean = numpy.mean((data))             
            d[str(key)+'ZI'+str(i)] = data_mean
            print d[str(key)+'ZI'+str(i)]
            key = key +1
            

    i = i+1


print d

temps = 1
for f in d:
        
    plt.plot(temps, f, 'bs')
    temps = temps +1
    
plt.axis([1, 4, 0.01, 10])
plt.title('Test')

plt.show()