# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:49:45 2015

@author: upression1
"""

import os
import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt

         #------------ Traitement mathématique (moyenne) et sauvegarde en .npy

data_in ='/home/pressions/SATELITIME/sdatats/Graph_data/ZI/'
os.chdir(data_in)
files = os.listdir(data_in) #Liste les fichiers.
files.sort() #Trie les fichiers.
print len(files) #len = longueur de la liste de fichiers.
f=len(files)   #('Combien de fichiers ? --> ')   #Nb fichiers : Nb lignes.



# -------------------------- Creation matrice vide----------------------------------
ZIs= np.load(files[0])
j=len(ZIs)/2 # Nombre de ZI (1er element de la liste = coord, 2e element = data)
expr=[]
for numzi in range(1,j+1):
    expr=expr+[('zi'+str(numzi)+'n','f8'),('zi'+str(numzi)+'moy','f8'),('zi'+str(numzi)+'et','f8'),('zi'+str(numzi)+'min','f8'),('zi'+str(numzi)+'max','f8'),('zi'+str(numzi)+'nan','f8')]
expr=[('date','i8')]+expr    
print expr
arr = np.zeros((f,),dtype=expr)
# ------------------------- Fin creation matrice ----------------------------------

# ------------------------- Boucle data stockage -----------------------------------
i = 0
for myfile in files:
    
    date= int(myfile[1:15])
    ZIs= np.load(myfile)
    
    n = 0  
    dline=[]
    while n <= j: # boucle sur les ZI
        
        coord = ZIs[n]
        data = ZIs[n+1]
        data_num=data.size
        data_mean = np.nanmean(data)
        data_nanmin=np.nanmin(data)
        data_nanmax=np.nanmax(data)
        data_nanstd=np.nanstd(data)
        data_nan=np.isnan(data).sum()
        dline=dline+[data_num,data_mean,data_nanstd,data_nanmin,data_nanmax,data_nan]
        n=n+2
    dline=[date]+dline
    print dline
    arr[i]=tuple(dline)
    i=i+1

# ------------------------- Plot graphique -----------------------------------

plt.plot(arr['zi1moy'], label='Moyenne')
plt.plot(arr['zi1et'], label='Ecart-type')

#plt.axis([0,arr.all['date'],0,1])
#plt.title('Valeurs moyennes de concentration en chlorophylle-a') 
plt.xlabel('Temps')
#plt.ylabel('[chlor-a] : mg/m3')

plt.show()

print 'fin'


