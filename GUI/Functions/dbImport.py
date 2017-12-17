# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 00:24:03 2017

@author: user
"""
def dbImport(name,path):
    import sqlite3
    conn = sqlite3.connect(r'C:\Users\merta\Desktop\Dersler\bitirme\LicenseProject\GUI\Functions\DB\DB.db')
    print ('Opened database successfully')
    
    #our feture functions.
    import Functions.zero_crossing_rate as zero_crossing_rate
    import Functions.MFCC as MFCC
    import Functions.spectral_centroid as spectral_centroid
    import Functions.spectral_contrast as spectral_contrast
    import Functions.spectral_rollof as spectral_rollof
    import Functions.spectral_bandwidth as spectral_bandwidth
     
    
    import librosa
    import statistics
    import numpy as np
    y, sr = librosa.load(path)#adres secimi yap.
    zcr = zero_crossing_rate.zero_crossing_rate(y)
    vzcr=statistics.pvariance(zcr[0])
    zcr=np.mean(zcr)
    
    centroid=spectral_centroid.spectral_centroid(y=y, sr=sr)
    vcentroid=statistics.pvariance(centroid[0])
    centroid=np.mean(centroid)
    
    S = np.abs(librosa.stft(y))
    contrast = spectral_contrast.spectral_contrast(S=S, sr=sr)
    vcontrast=statistics.pvariance(contrast[0])
    contrast = np.mean(contrast)
    
    
    rollof = spectral_rollof.spectral_rolloff(y=y, sr=sr)
    vrollof=statistics.pvariance(rollof[0])
    rollof=np.mean(rollof)
    
    bandwidth = spectral_bandwidth.spectral_bandwidth(y=y, sr=sr)
    vbandwidth=statistics.pvariance(bandwidth[0])
    bandwidth=np.mean(bandwidth)
    
    
    mfcc_array=MFCC.mfcc(y=y, sr=sr,n_mfcc=13)
    vmfcc1=statistics.pvariance(mfcc_array[0])
    mfcc1=np.mean(mfcc_array[0])
    
    vmfcc2=statistics.pvariance(mfcc_array[1])
    mfcc2=np.mean(mfcc_array[1])
    
    vmfcc3=statistics.pvariance(mfcc_array[2])
    mfcc3=np.mean(mfcc_array[2])
    
    vmfcc4=statistics.pvariance(mfcc_array[3])
    mfcc4=np.mean(mfcc_array[3])
    
    vmfcc5=statistics.pvariance(mfcc_array[4])
    mfcc5=np.mean(mfcc_array[4])
    
    vmfcc6=statistics.pvariance(mfcc_array[5])
    mfcc6=np.mean(mfcc_array[5])
    
    vmfcc7=statistics.pvariance(mfcc_array[6])
    mfcc7=np.mean(mfcc_array[6])
    
    vmfcc8=statistics.pvariance(mfcc_array[7])
    mfcc8=np.mean(mfcc_array[7])
    
    vmfcc9=statistics.pvariance(mfcc_array[8])
    mfcc9=np.mean(mfcc_array[8])
    
    vmfcc10=statistics.pvariance(mfcc_array[9])
    mfcc10=np.mean(mfcc_array[9])
    
    vmfcc11=statistics.pvariance(mfcc_array[10])
    mfcc11=np.mean(mfcc_array[10])
    
    vmfcc12=statistics.pvariance(mfcc_array[11])
    mfcc12=np.mean(mfcc_array[11])
    
    vmfcc13=statistics.pvariance(mfcc_array[12])
    mfcc13=np.mean(mfcc_array[12])
    
    
    #conn.execute("INSERT INTO Feature(NAME,mZcr,vZcr,mCentroid,vCentroid,mContrast,vContrast,mBandwidth,vBandwidth,mRollof,vRollof,mMFFC1,vMFFC1,mMFFC2,vMFFC2,mMFFC3,vMFFC3,mMFFC4,vMFFC4,mMFFC5,vMFFC5,mMFFC6,vMFFC6,mMFFC7,vMFFC7,mMFFC8,vMFFC8,mMFFC9,vMFFC9,mMFFC10,vMFFC10,mMFFC11,vMFFC11,mMFFC12,vMFFC12,mMFFC13,vMFFC13,)  VALUES ('"+name+"', "+zcr+", "+vzcr+", "+centroid+", "+vcentroid+", "+contrast+", "+vcontrast+", "+rollof+", "+vrollof+", "+bandwidth+", "+vbandwidth+", "+mfcc1+", "+vmfcc1+", "+mfcc2+", "+vmfcc2+", "+mfcc3+", "+vmfcc3+" "+mfcc4+", "+vmfcc4+", "+mfcc5+", "+vmfcc5+", "+mfcc6+", "+vmfcc6+", "+mfcc7+", "+vmfcc7+", "+mfcc8+", "+vmfcc8+", "+mfcc9+", "+vmfcc9+", "+mfcc10+", "+vmfcc10+", "+mfcc11+", "+vmfcc11+", "+mfcc12+", "+vmfcc12+", "+mfcc13+", "+vmfcc13+" )")
    List=[name,zcr,vzcr,centroid,vcentroid,contrast,vcontrast,rollof,vrollof,bandwidth,vbandwidth,mfcc1,vmfcc1,mfcc2,vmfcc2,mfcc3,vmfcc3,mfcc4,vmfcc4,mfcc5,vmfcc5,mfcc6,vmfcc6,mfcc7,vmfcc7,mfcc8,vmfcc8,mfcc9,vmfcc9,mfcc10,vmfcc10,mfcc11,vmfcc11,mfcc12,vmfcc12,mfcc13,vmfcc13]
    conn.execute("INSERT INTO Feature(NAME,mZcr,vZcr,mCentroid,vCentroid,mContrast,vContrast,mBandwidth,vBandwidth,mRollof,vRollof,mMFFC1,vMFFC1,mMFFC2,vMFFC2,mMFFC3,vMFFC3,mMFFC4,vMFFC4,mMFFC5,vMFFC5,mMFFC6,vMFFC6,mMFFC7,vMFFC7,mMFFC8,vMFFC8,mMFFC9,vMFFC9,mMFFC10,vMFFC10,mMFFC11,vMFFC11,mMFFC12,vMFFC12,mMFFC13,vMFFC13)  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", List)
    
    conn.commit()
    
    
    conn.close()
