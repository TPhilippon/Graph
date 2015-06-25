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

j =raw_input('Combien de ZI ? --> ')   #Nombre de ZI par date.
f =raw_input('Combien de fichiers ? --> ')   #Nb fichiers : Nb lignes.

#j = j+1   #Nombre de colonnes.
#f=f+1   #Nb de lignes.

n = 0


print "démarrage..."


date = []
m_ZI = []
date_y = 0
mean_y = 0
k = 2
i = 1
def c
            #------------ Colonnes des ZI.
            
#while i <= j:
#    
#    stock = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l'][i]
#    stock[i] = 'ZI'+str(i)
#    i = i+1
#    raw_input()

expr=''
for numzi in range(1,j+1):
    expr=expr+'(\'zi'+str(j)+'n\',\'f8\'),(\'zi'+str(j)+'moy\',\'f8\'),(\'zi'+str(j)+'et\',\'f8\'),(\'zi'+str(j)+'min\',\'f8\'),(\'zi'+str(j)+'max\',\'f8\'),(\'zi'+str(j)+'nan\',\'f8\')'
dtype='[]
arr = np.zeros((5,)
matrix = np.ndarray(shape=(f,i))

for myfile in files:
    
    i = 0
    print myfile
    print myfile[1:15]   
    date[int(date_y)] = [str(myfile[1:15])]
    
    while n < j:
        n=n+1
        
        data = np.load(myfile)
        data_mean = np.mean(data)
        print data_mean
        
        filen[mean_y] = data_mean
        
        mean_y = mean_y+1
        raw_input()
        
    date_y = date_y+1
    

date = np.array(date)
m_ZI = np.array(data_mean)


np.savez('ZI_allmean', date)





print 'fin'


