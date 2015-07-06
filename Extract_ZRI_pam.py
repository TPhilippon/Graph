# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:32:07 2015
@author: Terence, Pierre-Alain, UMR
"""
import os,sys
from pyhdf.SD import SD, SDC   
from mpl_toolkits.basemap import Basemap
from pylab import mpl as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
# =========================== Definition Varaibles =======================
varnum = 3
variable = ['nsst_8d', 'pic_8d', 'sst11mic_8d', 'chl_8d'][varnum]
bzi=1000 # marge autour des ZI pour la zoom
#data_out ='Y:\\home\\pressions\\SATELITIME\\sdatats\\Graph_data\\'   #Win
#data_indd ='Y:\\SATELITIME\\ddata\\'+str(variable)+'\\hdf'
data_out1 ='/home/pressions/SATELITIME/sdatats/Graph_data/ZR/' 
data_out2 ='/home/pressions/SATELITIME/sdatats/Graph_data/ZI/'  #Unix
data_in ='/home/pressions/SATELITIME/ddata/'+str(variable)+'/hdf/'
imfile = '/home/pressions/SATELITIME/ddata/chl2009.hdf' 
yzrmin,yzrmax,xzrmin,xzrmax=1600,2400,3000,3400


ezr=[yzrmin,yzrmax,xzrmin,xzrmax]
ezr=[000,6000,00,2600] # xmin,xmax,ymin,ymax,
#corr=np.array([4320,4320,8640,8640])
#ezr=corr-ezr

norm=mpl.colors.LogNorm(vmin=0.01, vmax=20)
colors = [(0.33,0.33,0.33)] + [(plt.cm.jet(i)) for i in xrange(1,256)]
new_map = mpl.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256) # Colormap

# ========================================================================
print "Choix de la zone régionale, patienez..."

fzr = SD(imfile, SDC.READ) #   Lire depuis le hdf.
dzr = fzr.select('l3m_data') #  Et met le contenu dans File.
dzr = dzr.get() #    Fonction get() pour avoir vraiment le tableau pour lire le hdf.
dzr = np.dot(dzr,1.0)
zr=dzr[ezr[2]:ezr[3],ezr[0]:ezr[1]]
plt.imshow(zr,norm=norm,extent=ezr,origin='upper', cmap=new_map,interpolation='none',aspect='equal') #extent=ezr
plt.show()
    #------------ Choix de la zone d'intérêt
czi =5#int(raw_input('Combien de ZI à délimiter?: '))
ezi=np.zeros((czi,),dtype=('i4,i4,i4,i4')) # ymin,ymax,xmin,xmax
for nzi in range(0,czi):
	print "ZI numero :",nzi
	extent='1840,1845,3228,3240' #raw_input('pour la zi: ymin,ymax,xmin,xmax : ') 2850,1800
	extent=(map(int,extent.split(',')))
	ezi[nzi]=tuple(extent) # stockage des coordonnées
	zzi=dzr[extent[0]-bzi:extent[1]+bzi,extent[2]-bzi:extent[3]+bzi] # data de zi avec un bord en plus
	plt.imshow(zzi,norm=norm, origin='lower',extent=[extent[0]-bzi,extent[1]+bzi,extent[2]-bzi,extent[3]+bzi],cmap=new_map,aspect='auto',interpolation='none')
	plt.show()
        # ==== trouver lesbornes de l'ensemble des ZI pour un zoom =====

        print "Coordonnées validées."
        j = j - 1
        
        
        print "recommencez."
        
print "Chargement..."

latminr = (float(latmin)-border)
latmaxr = (float(latmax)+border)
longminr = (float(longmin)-border)
longmaxr = (float(longmax)+border)

lats = [ latminr, latmaxr, latmaxr, latminr ]
lons = [ longminr, longminr, longmaxr, longmaxr ]

print 'x,y',x,y
#im=Image.open(img)
im2 = plt.imshow(im,extent=(x,x+179.9792,y+90,y-90), interpolation='none')
    
plt.show()

#sys.exit()

#--------------------- Lecture hdf et Extraction (save) ---------------------



print data_in
    #nsst_8d  
    #pic_8d
    #sst11mic_8d
    #chl_8d

files = os.listdir(data_in) #Liste les fichiers.
files.sort() #Trie les fichiers.
print len(files) #len = longueur de la liste de fichiers.


for myfile in files:
    
    print myfile
    i =1
    File = SD(data_in+myfile, SDC.READ) #   Lire depuis le hdf.
    l3 = File.select('l3m_data') #  Et met le contenu dans File.
    l3d = l3.get() #    Fonction get() pour avoir vraiment le tableau pour lire le hdf.
    #print 'min/max :', l3d.min(),l3d.max() # On peut demander les valeurs min / max.
    l3d = np.dot(l3d,1.0)

#    xminZR,xmaxZR=np.sort([abs(float(xmin)*43.2964),abs(float(xmax)*43.2964)])
#    yminZR,ymaxZR=np.sort([abs(float(ymin)*43.2964),abs(float(ymax)*43.2964)])
    
    xminZR,xmaxZR=np.sort([abs(float(xmin+179.9792)/0.0416666),abs(float(xmax+179.9792)/0.0416666)])
    yminZR,ymaxZR=np.sort([abs(float(-ymin+90)/0.0416666),abs(float(-ymax+90)/0.0416666)])

#    xminZR,xmaxZR=np.sort([abs(float(xmin)/0.08333333),abs(float(xmax)/0.08333333)])
#    yminZR,ymaxZR=np.sort([abs(float(ymin)/0.08333333),abs(float(ymax)/0.08333333)])
    
    print "xminZR,xmaxZR",xminZR,xmaxZR
    print "yminZR,ymaxZR",yminZR,ymaxZR
    varg=['sst11mic_8d','poc_8d', 'nsst_8d','chl_8d'][varnum]
    title=[u'Temperature de surface en °C',u'Carbone organique particlaire (POC) en mg.m-3',u'Temperature de surfarce nocturne en °C',u'Chlorophylle en mg.m-3'][varnum]
    FillValue=[65535.0,-32767.0,-32767.0,-32767.0]
    slI=[(0.00071718,-2),(1,0),(0.00071718,-2),(1,0)][varnum] #varnum récupère pente et intercept. 
    slope=slI[0] # égal au premier de la paire
    intercept=slI[1] 

    ScaledDataMinimum= [-2,10,-2,0.01][varnum] # Sert dans la formule de convertion. Scaled = données mises à l'échelle.
    ScaledDataMaximum= [45,1000,45,20][varnum] # Donne les futurs min / max des unités de valeurs.

    vmin=ScaledDataMinimum
    vmax=ScaledDataMaximum

    ZRl3d=l3d[yminZR:ymaxZR,xminZR:xmaxZR] # Echantilloner. Distance lignes puis colonnes.
    ZRl3dR=(ZRl3d*slope)+intercept
    
    print "ZRl3d",ZRl3d
    print "ZRl3dR",ZRl3dR

    ZRl3dR[ ZRl3dR == FillValue[varnum] ] = np.nan 

    filen = data_out1+myfile[0:38]+'_ZR'
    print filen

    w = ZRl3dR.shape
    print(w)
    numpy.save(filen, ZRl3dR)
    
    ZIs=[]
    while i <= p:
        
        xminZI,xmaxZI=np.sort([abs(round((float(d['xmin'+str(i)])+179.9792)/0.0416666)),abs(round((float(d['xmax'+str(i)])+179.9792)/0.0416666))])
        yminZI,ymaxZI=np.sort([abs(round((float(90-d['ymin'+str(i)]))/0.0416666)),abs(round((float(90-d['ymax'+str(i)]))/0.0416666))])

#        xminZI,xmaxZI=np.sort([abs(round((float(d['xmin'+str(i)])+180)/0.0833333)),abs(round((float(d['xmax'+str(i)])+180)/0.0833333))])
#        yminZI,ymaxZI=np.sort([abs(round((float(90-d['ymin'+str(i)]))/0.0833333)),abs(round((float(90-d['ymax'+str(i)]))/0.0833333))])
#        ymaxZI = abs(int(d['ymax'+str(i)])*43.2964)
#        yminZI = abs(int(d['ymin'+str(i)])*43.2964)
#        xmaxZI = abs(int(d['xmax'+str(i)])*43.2964)
#        xminZI = abs(int(d['xmin'+str(i)])*43.2964)

        print xminZI, xmaxZI
        print yminZI, ymaxZI

        ZIl3d=l3d[yminZI:ymaxZI,xminZI:xmaxZI] # Echantilloner la ZI. Distance lignes puis colonnes.
        ZIl3dR=(ZIl3d*slope)+intercept
        #ZIl3dR=np.dot(ZIl3dR,1.0) #   
        ZIl3dR[ ZIl3dR == FillValue[varnum] ] = np.nan #0.011 0.00001 #
        print "nombre de pixels : ", ZIl3d.size, np.prod(ZIl3d.shape)
        
        
        #ZIl3dR = np.array([ZIl3dR])
#        l[s] = ZIl3dR  
#        s=s+1   
        
        #numpy.save(filen+str(i), ZIl3dR)
        ZIs=ZIs+[(yminZI,ymaxZI,xminZI,xmaxZI,d['ymin'+str(i)],d['ymax'+str(i)],d['xmin'+str(i)],d['xmax'+str(i)]),ZIl3dR]
        i=i+1                
        raw_input()
#numpy.savez(filen, l)
    filen = data_out2+myfile[0:38]+'_ZI'  #'A'+str(a)+str(format(day,'03'))+str(a)+str(format(day2,'03'))+'.'+varg+
    print filen
    numpy.save(filen, ZIs)


print 'Fin'


