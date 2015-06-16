

import os
import sys
from pyhdf.SD import SD, SDC   
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon


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
    choix =raw_input('Valider oui ou non: ')
    choix =raw_input('Valider o/n?: ')
    
    if choix =="o": 
        
        print "coordonnées validées"
        print "coordonnées validées, patientez..."
        i = 0
    else:
        print "recommencez"

ymax = urcrnrlat
ymin = llcrnrlat
xmax = urcrnrlon
xmin = llcrnrlon

    #------------ Choix de la zone d'intérêt
print ("Choix de la zone d'intérêt. Patientez...")

m = Basemap(projection='cyl',llcrnrlat=ymin, urcrnrlat=ymax, llcrnrlon=xmin, urcrnrlon=xmax,resolution='c')
m.drawlsmask(land_color='black',ocean_color='None',lakes=True)

plt.show()

print "Entrez vos coordonnées:"
urcrnrlat2 =raw_input('ymax2 : ')
llcrnrlat2 =raw_input('ymin2 : ')
urcrnrlon2 =raw_input('xmax2 : ')
llcrnrlon2 =raw_input('xmin2 : ')

j = 1
while j > 0:
        choix =raw_input('Valider o/n?: ')
    
        if choix =="o": 
        
            print "coordonnées validées, patientez..."
            j = 0
        else:
            print "recommencez"
            urcrnrlat2 =raw_input('ymax2 : ')
            llcrnrlat2 =raw_input('ymin2 : ')
            urcrnrlon2 =raw_input('xmax2 : ')
            llcrnrlon2 =raw_input('xmin2 : ')

ymax2 = urcrnrlat2
ymin2 = llcrnrlat2
xmax2 = urcrnrlon2
xmin2 = llcrnrlon2

    #------------ Affichage ZR et ZI sur la Basemap
m = Basemap(projection='cyl',resolution='c')
m.drawlsmask(land_color='black',ocean_color='None',lakes=True)

def draw_screen_poly( lats, lons, m):
    x, y = m( lons, lats )
    xy = zip(x,y)
    poly = Polygon( xy, facecolor='red', alpha=0.4 )
    plt.gca().add_patch(poly)

lats = [ ymin, ymax, ymax, ymin ]
lons = [ xmin, xmin, xmax, xmax ]

draw_screen_poly( lats, lons, m )

def draw_screen_poly2( lats2, lons2, m):
    x, y = m( lons2, lats2 )
    xy = zip(x,y)
    poly = Polygon( xy, facecolor='yellow', alpha=0.4 )
    plt.gca().add_patch(poly)

lats2 = [ ymin2, ymax2, ymax2, ymin2 ]
lons2 = [ xmin2, xmin2, xmax2, xmax2 ]

draw_screen_poly2( lats2, lons2, m )

plt.show()

    #------------ Lecture hdf et Extraction

#myfile = 'A20021852002192.L3m_8D_CHL_chlor_a_4km.bz2.hdf'
#
#varnum=3  # choix de la variable
#varg=['sst11mic_8d','poc_8d', 'nsst_8d','chl_8d'][varnum]
#
#FillValue=[65535.0,-32737.0,-32737.0,-32737.0]
#slI=[(0.00071718,-2),(1,0),(0.00071718,-2),(1,0)][varnum] # cette fois varnum récupère pente et intercept. 
#slope=slI[0] # égal au premier de la paire
#intercept=slI[1] 
#
#path = varg+'/hdf/'
#files = os.listdir(path) #Liste ldes fichiers.
#files.sort() #Trie les fichiers.
#print len(files) #len = longueur de la liste de fichiers.
#
#File_Name = myfile
#File = SD(varg+'/hdf/'+File_Name, SDC.READ) #   Lire depuis le hdf.
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
#ZIl3d=l3d[yminZI:ymaxZI,xminZI:xmaxZI] # Echantilloner la ZI. Distance lignes puis colonnes.
#ZIl3d=np.dot(l3d,1.0) #   CRUCIAL : transformation en objet numpy pour manipuler plus facilement.




























