# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:32:07 2015

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
        
        print "coordonnées validées, patientez..."
        i = 0
    else:
        print "recommencez"
        urcrnrlat =raw_input('ymax : ')
        llcrnrlat =raw_input('ymin : ')
        urcrnrlon =raw_input('xmax : ')
        llcrnrlon =raw_input('xmin : ')

ymax = urcrnrlat
ymin = llcrnrlat
xmax = urcrnrlon
xmin = llcrnrlon

    #------------ Choix de la zone d'intérêt
print ("Choix de la zone d'intérêt. Patientez...")

m = Basemap(projection='cyl',llcrnrlat=ymin, urcrnrlat=ymax, llcrnrlon=xmin, urcrnrlon=xmax,resolution='c')
m.drawlsmask(land_color='black',ocean_color='None',lakes=True)

plt.show()

#print "Entrez vos coordonnées:"
#urcrnrlat2 =raw_input('ymax : ')
#llcrnrlat2 =raw_input('ymin : ')
#urcrnrlon2 =raw_input('xmax : ')
#llcrnrlon2 =raw_input('xmin : ')
#
#j = 1
#m = Basemap(projection='cyl',resolution='c')
#m.drawlsmask(land_color='black',ocean_color='None',lakes=True)
#
#def draw_screen_poly( lats, lons, m):
#    x, y = m( lons, lats )
#    xy = zip(x,y)
#    poly = Polygon( xy, edgecolor='Red', fill=False, alpha=1.5 )
#    plt.gca().add_patch(poly)
#
#lats = [ ymin, ymax, ymax, ymin ]
#lons = [ xmin, xmin, xmax, xmax ]
#
#draw_screen_poly( lats, lons, m )
#
#while j > 0:
#        choix =raw_input('Valider o/n?: ')
#        
#        if choix =="o": 
#        
#            print "coordonnées validées, patientez..."
#            j = 0
#        else:
#            print "recommencez"
#            urcrnrlat2 =raw_input('ymax : ')
#            llcrnrlat2 =raw_input('ymin : ')
#            urcrnrlon2 =raw_input('xmax : ')
#            llcrnrlon2 =raw_input('xmin : ')
#
#ymax2 = urcrnrlat2
#ymin2 = llcrnrlat2
#xmax2 = urcrnrlon2
#xmin2 = llcrnrlon2

print "Choix de la zone d'intérêt..."
print "Combien de zones à délimiter?"
j =raw_input('nombre de ZI : ')
j = int(j)

#ok =raw_input('Valider o/n?: ')
#
#if ok !='o':
#    print "Correction..."
#    print "Combien de zones à délimiter?"
#    j =raw_input('nombre de ZI : ')

m = Basemap(projection='cyl',resolution='c')
m.drawlsmask(land_color='black',ocean_color='None',lakes=True)

while j > 0:
    print "Encore"
    print j
    print "ZI à délimiter."
    print "Entrez vos coordonnées:"
    urcrnrlat =raw_input('ymax : ')
    llcrnrlat =raw_input('ymin : ')
    urcrnrlon =raw_input('xmax : ')
    llcrnrlon =raw_input('xmin : ')
    choix =raw_input('Valider o/n?: ')
    
    if choix =="o": 
        
        print "coordonnées validées, patientez..."
        j = j - 1
        ymax2 = urcrnrlat
        ymin2 = llcrnrlat
        xmax2 = urcrnrlon
        xmin2 = llcrnrlon
        def draw_screen_poly2( lats2, lons2, m):
            x, y = m( lons2, lats2 )
            xy = zip(x,y)
            poly = Polygon( xy, edgecolor='Yellow', fill=False, alpha=1.5 )
            plt.gca().add_patch(poly)

        lats2 = [ ymin2, ymax2, ymax2, ymin2 ]
        lons2 = [ xmin2, xmin2, xmax2, xmax2 ]

        draw_screen_poly2( lats2, lons2, m )
    else:
        print "recommencez"
        
def draw_screen_poly( lats, lons, m):
    x, y = m( lons, lats )
    xy = zip(x,y)
    poly = Polygon( xy, edgecolor='Red', fill=False, alpha=1.5 )
    plt.gca().add_patch(poly)

lats = [ ymin, ymax, ymax, ymin ]
lons = [ xmin, xmin, xmax, xmax ]

draw_screen_poly( lats, lons, m )

#        urcrnrlat =raw_input('ymax : ')
#        llcrnrlat =raw_input('ymin : ')
#        urcrnrlon =raw_input('xmax : ')
#        llcrnrlon =raw_input('xmin : ')


    #------------ Affichage ZR et ZI sur la Basemap
#m = Basemap(projection='cyl',resolution='c')
#m.drawlsmask(land_color='black',ocean_color='None',lakes=True)
#
#
#
#
#
#if continuer == 'o':
#    j = i
#    while j > 2:
#        def draw_screen_poly( lats, lons, m):
#            x, y = m( lons, lats )
#            xy = zip(x,y)
#            poly = Polygon( xy, edgecolor='Red', fill=False, alpha=1.5 )
#            plt.gca().add_patch(poly)
#
#        lats = [ llcrnrlat+i, urcrnrlat+i, urcrnrlat+i, llcrnrlat+i ]
#        lons = [ llcrnrlon+i, llcrnrlon+i, urcrnrlon+i, urcrnrlon+i ]
#
#        draw_screen_poly( lats, lons, m )
#        j = j-1
#else:
#    end()
    
plt.show()

    #------------ Lecture hdf et Extraction

#myfile = 'A20021852002192.L3m_8D_CHL_chlor_a_4km.bz2.hdf'
#
#path = '/home/pressions/SATELITIME/ddata/chl_8d/hdf/'
#files = os.listdir(path) #Liste ldes fichiers.
#files.sort() #Trie les fichiers.
#print len(files) #len = longueur de la liste de fichiers.
#
#File_Name = myfile
#File = SD(path+File_Name, SDC.READ) #   Lire depuis le hdf.
#l3 = File.select('l3m_data') #  Et met le contenu dans File.
#l3d = l3.get() #    Fonction get() pour avoir vraiment le tableau pour lire le hdf.
#    
#print 'min/max :', l3d.min(),l3d.max() # On peut demander les valeurs min / max.
#
#ymaxZI = ymax2*43.2964
#yminZI = ymin2*43.2964
#xmaxZI = xmax2*43.2964
#xminZI = xmin2*43.2964
#
#varnum=3  # on a dl plusieurs variables (ligne 23)
#varg=['sst11mic_8d','poc_8d', 'nsst_8d','chl_8d'][varnum]
#title=[u'Temperature de surface en °C',u'Carbone organique particlaire (POC) en mg.m-3',u'Temperature de surfarce nocturne en °C',u'Chlorophylle en mg.m-3'][varnum]
#FillValue=[65535.0,-32737.0,-32737.0,-32737.0]
#slI=[(0.00071718,-2),(1,0),(0.00071718,-2),(1,0)][varnum] # cette fois varnum récupère pente et intercept. 
#slope=slI[0] # égal au premier de la paire
#intercept=slI[1] 
#
#ScaledDataMinimum= [-2,10,-2,0.01][varnum] # Nous sert dans la formule de convertion. Scaled = données mises à l'échelle.
#ScaledDataMaximum= [45,1000,45,20][varnum] # Donne les futurs min / max des unités de valeurs.
#
#vmin=ScaledDataMinimum
#vmax=ScaledDataMaximum
#
#l3d[ (l3d < vmin) & (l3d != FillValue) ] = vmin #
#l3d[ l3d > 10 ] = 10.0 #
#if l3d.any()<0.011:
#    l3d[ l3d == FillValue ] = np.nan #0.011 0.00001 #
#
#ZIl3d=l3d[yminZI:ymaxZI,xminZI:xmaxZI] # Echantilloner la ZI. Distance lignes puis colonnes.
#ZIl3dR=(ZIl3d*slope)+intercept
#ZIl3dR=np.dot(l3d,1.0) #   CRUCIAL : transformation en objet numpy pour manipuler plus facilement
#
#print 'min/max :', l3d.min(),l3d.max()
#
#numpy.save('test', ZIl3d)

