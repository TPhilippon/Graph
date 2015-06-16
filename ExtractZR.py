# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 14:20:45 2015

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


     #------------ Choix de la zone d'étude

print "Choix de la zone régionale, patienez..."
#m = Basemap(projection='cyl',resolution='c')
#m.drawlsmask(land_color='black',ocean_color='None',lakes=True)

#plt.show()

print "Entrez vos coordonnées:"
urcrnrlat =raw_input('ymax : ')
llcrnrlat =raw_input('ymin : ')
urcrnrlon =raw_input('xmax : ')
llcrnrlon =raw_input('xmin : ')

i = 1
while i > 0:
    choix =raw_input('Valider o/n?: ')
    
    if choix =="o": 
        
        print "Coordonnées validées."
        i = 0
    else:
        print "recommencez"
        urcrnrlat =raw_input('ymax : ')
        llcrnrlat =raw_input('ymin : ')
        urcrnrlon =raw_input('xmax : ')
        llcrnrlon =raw_input('xmin : ')

ymax = urcrnrlat #Mémoire ZR
ymin = llcrnrlat
xmax = urcrnrlon
xmin = llcrnrlon


    #------------ Lecture hdf et Extraction (npy save)

data_out ='/home/pressions/SATELITIME/sdatats/Graph_data/'
data_in ='/home/pressions/SATELITIME/ddata/'+'chl_8d'+'/hdf/'
    #nsst_8d
    #pic_8d
    #sst11mic_8d
    #chl_8d

files = os.listdir(data_in) #Liste les fichiers.
files.sort() #Trie les fichiers.
print len(files) #len = longueur de la liste de fichiers.


for myfile in files:
    
        
    File = SD(data_in+myfile, SDC.READ) #   Lire depuis le hdf.
    l3 = File.select('l3m_data') #  Et met le contenu dans File.
    l3d = l3.get() #    Fonction get() pour avoir vraiment le tableau pour lire le hdf.
    #print 'min/max :', l3d.min(),l3d.max() # On peut demander les valeurs min / max.


    ymaxZR = int(ymax)*43.2964
    yminZR = int(ymin)*43.2964
    xmaxZR = int(ymax)*43.2964
    xminZR = int(ymin)*43.2964

    varnum=3  # on a dl plusieurs variables (ligne 23)
    varg=['sst11mic_8d','poc_8d', 'nsst_8d','chl_8d'][varnum]
    title=[u'Temperature de surface en °C',u'Carbone organique particlaire (POC) en mg.m-3',u'Temperature de surfarce nocturne en °C',u'Chlorophylle en mg.m-3'][varnum]
    FillValue=[65535.0,-32737.0,-32737.0,-32737.0]
    slI=[(0.00071718,-2),(1,0),(0.00071718,-2),(1,0)][varnum] # cette fois varnum récupère pente et intercept. 
    slope=slI[0] # égal au premier de la paire
    intercept=slI[1] 

    ScaledDataMinimum= [-2,10,-2,0.01][varnum] # Nous sert dans la formule de convertion. Scaled = données mises à l'échelle.
    ScaledDataMaximum= [45,1000,45,20][varnum] # Donne les futurs min / max des unités de valeurs.

    vmin=ScaledDataMinimum
    vmax=ScaledDataMaximum

    l3d[ (l3d < vmin) & (l3d != FillValue) ] = vmin #
    l3d[ l3d > 10 ] = 10.0 #
    if l3d.any()<0.011:
        l3d[ l3d == FillValue ] = np.nan #0.011 0.00001 #

    ZIl3d=l3d[yminZR:ymaxZR,xminZR:xmaxZR] # Echantilloner la ZI. Distance lignes puis colonnes.
    ZIl3dR=(ZIl3d*slope)+intercept
    ZIl3dR=np.dot(ZIl3dR,1.0) #   CRUCIAL : transformation en objet numpy pour manipuler plus facilement

    print 'min/max :', l3d.min(),l3d.max()

    filen = data_out+myfile[0:38]+'_ZR'
    print filen
    
    np.array([ZIl3dR])
    numpy.save(filen, ZIl3dR)
    
    
    
                          


print 'Fin'