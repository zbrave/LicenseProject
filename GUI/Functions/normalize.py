# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 01:38:50 2017

@author: user
"""
def normalize():
        import sqlite3
        import numpy as np
        vt = sqlite3.connect('Functions\DB\DB.db')
        print ('Opened database successfully')
        conn=vt.cursor()
        
        conn.execute("Delete FROM NFeature")
        vt.commit()
        conn.execute("insert into NFeature select * from Feature")
        vt.commit()
        
        conn.execute("SELECT * FROM NFeature")
        
        
        veriler = conn.fetchall()
        
        trainData=np.zeros((veriler.__len__(),72))
        #npNames = np.zeros((veriler.__len__(), 1),dtype='S10')
        
        #names=[]
        j=0
        
        for x in veriler:
            #trainData.append(x[2:])
            trainData[j]=x[2:]
            #nameNpmy=x[1]
            #names.append(x[1])
            #npNames[j][0]=names[j].encode('utf-8')
            j=j+1
            #trainData.append(preprocessing.normalize(x[2:], norm='l2'))
        
        from sklearn import preprocessing
        
        for i in range(2,36):
            trainData[:96,i]=preprocessing.normalize(trainData[:96,i], norm='l2') 
        
        #X_normalized1 = preprocessing.normalize(trainData, norm='l1')
        
            
        
        i=1
        
        
        for x in range(96):
            b=np.array([[veriler[x][0]]])
            bak=trainData[x]
            bak=bak[np.newaxis]
            imp=np.concatenate((bak, b), axis=1)
            vt.executemany("UPDATE  NFeature set mZcr=?,vZcr=?,mCentroid=?,vCentroid=?,mContrast=?,vContrast=?,mBandwidth=?,vBandwidth=?,mRollof=?,vRollof=?,mMFFC1=?,vMFFC1=?,mMFFC2=?,vMFFC2=?,mMFFC3=?,vMFFC3=?,mMFFC4=?,vMFFC4=?,mMFFC5=?,vMFFC5=?,mMFFC6=?,vMFFC6=?,mMFFC7=?,vMFFC7=?,mMFFC8=?,vMFFC8=?,mMFFC9=?,vMFFC9=?,mMFFC10=?,vMFFC10=?,mMFFC11=?,vMFFC11=?,mMFFC12=?,vMFFC12=?,mMFFC13=?,vMFFC13=?,mCqt1=?,vCqt1=?,mCqt2=?,vCqt2=?,mCqt3=?,vCqt3=?,mCqt4=?,vCqt4=?,mCqt5=?,vCqt5=?,mCqt6=?,vCqt6=?,mCqt7=?,vCqt7=?,mCqt8=?,vCqt8=?,mCqt9=?,vCqt9=?,mCqt10=?,vCqt10=?,mCqt11=?,vCqt11=?,mCqt12=?,vCqt12=?,mTonnetz1=?,vTonnetz1=?,mTonnetz2=?,vTonnetz2=?,mTonnetz3=?,vTonnetz3=?,mTonnetz4=?,vTonnetz4=?,mTonnetz5=?,vTonnetz5=?,mTonnetz6=?,vTonnetz6=? WHERE ID=?", (imp))
           
            i=i+1
            vt.commit()
        
        conn.close()