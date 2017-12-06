# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 15:17:04 2017

@author: user
"""

import zero_crossing_rate
import MFCC
import spectral_centroid
import spectral_contrast
import spectral_rollof
import spectral_bandwidth

import math
def euclideanDistance(instance1, instance2,n):
	distance = 0
	for x in range(n):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)


import operator 
def knn(trainingSet, testInstance, k, n):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(trainingSet[x], testInstance,n )
		distances.append([dist,x])
	distances.sort(key=operator.itemgetter(0))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][1])
	return neighbors


    
        
import sqlite3
vt = sqlite3.connect('DB/DB.db')
print ('Opened database successfully')
conn=vt.cursor()

conn.execute("SELECT * FROM Feature")

veriler = conn.fetchall()

trainData=[]

for x in veriler:
    trainData.append(x[2:])
    

testData= trainData[0]   
result=knn(trainData,testData,2,5)

for i in result:
    print(veriler[i][1],i)
    
    