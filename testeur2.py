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


#
#        day= 1
#        day2= 0
#        b= 8 
#        day2= day+7
#        if day2 > 365:
#            day2 = 365
#        if a % 4 == 0 and day2 == 365:
#            day2 = 366
        
data_out ='/home/pressions/SATELITIME/sdatats/Graph_data/'
data_in ='/home/pressions/SATELITIME/ddata/'+'chl_8d'+'/hdf/'
    #nsst_8d
    #pic_8d
    #sst11mic_8d
    #chl_8d

files = os.listdir(data_in) #Liste les fichiers.
files.sort() #Trie les fichiers.
print len(files) #len = longueur de la liste de fichiers.
p = 2
stop = 3
start = 1

d2 = {}
        
for myfile in files:
    day= 185
    day2= 0
    b= 8 
for a in range (2002,2016):

    print a
    while day2 < 365:
        day2= day+7
        if day2 > 365:
            day2 = 365
        if a % 4 == 0 and day2 == 365:
            day2 = 366
        
        i=1
        File = SD(data_in+myfile, SDC.READ) #   Lire depuis le hdf.
        l3 = File.select('l3m_data') #  Et met le contenu dans File.
        l3d = l3.get() #    Fonction get() pour avoir vraiment le tableau pour lire le hdf.
        print 'min/max :', l3d.min(),l3d.max() # On peut demander les valeurs min / max.
        
        if start < stop:
            while i <= p:
    
                ymaxZI = int(30)*43.2964
                yminZI = int(-7)*43.2964
                xmaxZI = int(-33)*43.2964
                xminZI = int(-100)*43.2964
    
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

                ZIl3d=l3d[yminZI:ymaxZI,xminZI:xmaxZI] # Echantilloner la ZI. Distance lignes puis colonnes.
                ZIl3dR=(ZIl3d*slope)+intercept
                ZIl3dR=np.dot(l3d,1.0) #   CRUCIAL : transformation en objet numpy pour manipuler plus facilement

                print 'min/max :', l3d.min(),l3d.max()
    
                filen = data_out+'A'+str(a)+str(format(day,'03'))+str(a)+str(format(day2,'03'))+'.'+varg+'_ZI'
                print filen+str(i)
                
                np.array([ZIl3dR])
                numpy.save(filen+str(i), ZIl3dR)
                
                f = filen+str(i)+'.npy'
                data = numpy.load(f)
                data_mean = numpy.mean(data)
                
                d2['ZI'+str(i)] = data_mean
                
                
                i=i+1
                start = start+1  #DELME
                
                day= day+8
        if a == 2015 and day2 == 32:
            day2 = 365
    day= 1
    day2= 0
                
plt.plot(int(d2['ZI1']),'o')
plt.plot(int(d2['ZI2']),'o')

plt.xlabel('x')
plt.ylabel('y')
plt.title('filen')

plt.show()
                

print 'Fin'
