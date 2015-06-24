# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:49:45 2015

@author: upression1
"""

import os
import numpy as np




         #------------ Traitement mathématique (moyenne) et sauvegarde en .npy

data_in ='/home/pressions/SATELITIME/sdatats/Graph_data/ZI/'
os.chdir(data_in)

files = os.listdir(data_in) #Liste les fichiers.
files.sort() #Trie les fichiers.
print len(files) #len = longueur de la liste de fichiers.

i = 2     #Nombre de ZI par date.

#d = {}
#key = 1     #Compteur pour le dictionnaire.

print "début boucle"
l = []
s = 0
#ll = np.array([])

for myfile in files:
    print myfile     
    data = np.load(myfile)
    data_mean = np.mean(data)
    print data_mean  
    l[s] = data_mean
    
    s=s+1
    


np.savez('ZI_mean', l)





print 'fin'


