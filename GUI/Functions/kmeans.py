# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 17:46:50 2017

@author: user
"""


from scipy.spatial.distance import cdist
import numpy as np

import math
def euclideanDistance(instance1, instance2,n):
	distance = 0
	for x in range(n):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

    
def cDist(Data,center,k,size):
    distances= np.random.rand(size,k)
    i=0
    j=0
    for x in Data:
        for y in center:
            distances[i][j]= euclideanDistance(x, y,72)
            j=j+1
        i=i+1
        j=0
    return distances


def kMeans(k=None,method=None,Data=None,size=None,L=None):
    #center=[]
    global center
    
    #print('kmeans')       
    center=np.random.rand(k,72)#rastgele k tane random değerler oluşturuluyor.
    for i in range(k):
            #rastgele Datanın içinden k tane değer alınıyor bunlar başlagıç center'ı oluyor.
            indexplus=np.random.randint(low=0, high=size-1)
            center[i]=Data[indexplus]
            #center[i]=Data[indexplus]
   
        
    global distances,label
    tmp=center-1#döngüye başlangıçta girmesi için centerdan farklı bir değer veriyoruz    
    while (tmp!=center).all(): #bir önceki merkezle aynı olmadığı sürece devam
        #print("------------------DÖNDÜYE GİRDİ-----------------")
        tmp=center.copy() #bir önceki merkezi tutuyoruz kontrol için
        distances=cDist(Data, center,k,size)#mesafe matrisi tutuluyor
        
        
        L=np.argmin(distances,axis=1)#merkezlere mesafelerin en düşük değerinin indisi geliyor yani labellarımız.
        #print(L)
        
        for i in range(k):
            #aynı label değerlerinin ortalamasını alıyoruz ve çıkan ortalama değerler yeni center'ımız oluyor.
            #global tmp_array
            tmp_array=np.mean( Data[np.nonzero(L==i)],axis=0)
            #print(tmp_array)
            if math.isnan(tmp_array[0]) == False:
                for j in range(72):
                    center[i][j]=tmp_array[j]
            
    label=L.copy()#en sonunda döngüden çıktıktan sonra çizdirmek için local olan L yi global olan label a kopyalıyoruz.
    return label#buradaki dönen center'ı sadece mini bölümü için 100 elemana uygulanan kmeans++ ın center'ını almak için kullandım.
    
'''
import sqlite3

vt = sqlite3.connect('DB/DB.db')
print ('Opened database successfully')
conn=vt.cursor()

conn.execute("SELECT * FROM Feature")

veriler = conn.fetchall()
t=veriler.__len__()
trainData=np.random.rand(t,72)

for i in range(t):
   trainData[i]=veriler[i][2:]
    
label=np.full([t,],-1)

veriler[4]
Ltemp=kMeans(k=2,method='kmeans',Data=trainData,size=t,L=label) 
#testData= trainData[0]   
#result=knn(trainData,testData,2,5)

#for i in result:
#    print(veriler[i][1],i)

conn.close()
'''

