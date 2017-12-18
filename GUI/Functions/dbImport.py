# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 00:24:03 2017

@author: user
"""
def dbImport(name,path):
    import sqlite3
    conn = sqlite3.connect('Functions\DB\DB.db') #r'C:\Users\merta\Desktop\Dersler\bitirme\LicenseProject\GUI\Functions\DB\DB.db'
    print ('Opened database successfully')
    
    #our feture functions.
    import Functions.zero_crossing_rate as zero_crossing_rate
    import Functions.MFCC as MFCC
    import Functions.spectral_centroid as spectral_centroid
    import Functions.spectral_contrast as spectral_contrast
    import Functions.spectral_rollof as spectral_rollof
    import Functions.spectral_bandwidth as spectral_bandwidth
    import Functions.chroma_cqt as chroma_cqt
    import Functions.tonnetz as tonnetz
    
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
    
    cqt_array = chroma_cqt.chroma_cqt(y=y, sr=sr)
    vcqt1=statistics.pvariance(cqt_array[0])
    mcqt1=np.mean(cqt_array[0])
    
    vcqt2=statistics.pvariance(cqt_array[1])
    mcqt2=np.mean(cqt_array[1])
    
    vcqt3=statistics.pvariance(cqt_array[2])
    mcqt3=np.mean(cqt_array[2])
        
    vcqt4=statistics.pvariance(cqt_array[3])
    mcqt4=np.mean(cqt_array[3])
        
    vcqt5=statistics.pvariance(cqt_array[4])
    mcqt5=np.mean(cqt_array[4])
        
    vcqt6=statistics.pvariance(cqt_array[5])
    mcqt6=np.mean(cqt_array[5])
        
    vcqt7=statistics.pvariance(cqt_array[6])
    mcqt7=np.mean(cqt_array[6])
        
    vcqt8=statistics.pvariance(cqt_array[7])
    mcqt8=np.mean(cqt_array[7])
        
    vcqt9=statistics.pvariance(cqt_array[8])
    mcqt9=np.mean(cqt_array[8])
        
    vcqt10=statistics.pvariance(cqt_array[9])
    mcqt10=np.mean(cqt_array[9])
    
        
    vcqt11=statistics.pvariance(cqt_array[10])
    mcqt11=np.mean(cqt_array[10])
    
        
    vcqt12=statistics.pvariance(cqt_array[11])
    mcqt12=np.mean(cqt_array[11])
    
    
    yT = librosa.effects.harmonic(y)
    tonnetz_array =tonnetz.tonnetz(y=yT, sr=sr)
    vtonnetz1 = statistics.pvariance(tonnetz_array[0])
    mtonnetz1 = np.mean(tonnetz_array[0])
    
    vtonnetz2 = statistics.pvariance(tonnetz_array[1])
    mtonnetz2 = np.mean(tonnetz_array[1])
    
       
    vtonnetz3 = statistics.pvariance(tonnetz_array[2])
    mtonnetz3 = np.mean(tonnetz_array[2])
    
       
    vtonnetz4 = statistics.pvariance(tonnetz_array[3])
    mtonnetz4 = np.mean(tonnetz_array[3])
       
    vtonnetz5 = statistics.pvariance(tonnetz_array[4])
    mtonnetz5 = np.mean(tonnetz_array[4])
       
    vtonnetz6 = statistics.pvariance(tonnetz_array[5])
    mtonnetz6 = np.mean(tonnetz_array[5])
       
    
    
    
    
    #conn.execute("INSERT INTO Feature(NAME,mZcr,vZcr,mCentroid,vCentroid,mContrast,vContrast,mBandwidth,vBandwidth,mRollof,vRollof,mMFFC1,vMFFC1,mMFFC2,vMFFC2,mMFFC3,vMFFC3,mMFFC4,vMFFC4,mMFFC5,vMFFC5,mMFFC6,vMFFC6,mMFFC7,vMFFC7,mMFFC8,vMFFC8,mMFFC9,vMFFC9,mMFFC10,vMFFC10,mMFFC11,vMFFC11,mMFFC12,vMFFC12,mMFFC13,vMFFC13,)  VALUES ('"+name+"', "+zcr+", "+vzcr+", "+centroid+", "+vcentroid+", "+contrast+", "+vcontrast+", "+rollof+", "+vrollof+", "+bandwidth+", "+vbandwidth+", "+mfcc1+", "+vmfcc1+", "+mfcc2+", "+vmfcc2+", "+mfcc3+", "+vmfcc3+" "+mfcc4+", "+vmfcc4+", "+mfcc5+", "+vmfcc5+", "+mfcc6+", "+vmfcc6+", "+mfcc7+", "+vmfcc7+", "+mfcc8+", "+vmfcc8+", "+mfcc9+", "+vmfcc9+", "+mfcc10+", "+vmfcc10+", "+mfcc11+", "+vmfcc11+", "+mfcc12+", "+vmfcc12+", "+mfcc13+", "+vmfcc13+" )")
    List=[name,zcr,vzcr,centroid,vcentroid,contrast,vcontrast,rollof,vrollof,bandwidth,vbandwidth,mfcc1,vmfcc1,mfcc2,vmfcc2,mfcc3,vmfcc3,mfcc4,vmfcc4,mfcc5,vmfcc5,mfcc6,vmfcc6,mfcc7,vmfcc7,mfcc8,vmfcc8,mfcc9,vmfcc9,mfcc10,vmfcc10,mfcc11,vmfcc11,mfcc12,vmfcc12,mfcc13,vmfcc13,mcqt1,vcqt1,mcqt2,vcqt2,mcqt3,vcqt3,mcqt4,vcqt4,mcqt5,vcqt5,mcqt6,vcqt6,mcqt7,vcqt7,mcqt8,vcqt8,mcqt9,vcqt9,mcqt10,vcqt10,mcqt11,vcqt11,mcqt12,vcqt12,mtonnetz1,vtonnetz1,mtonnetz2,vtonnetz2,mtonnetz3,vtonnetz3,mtonnetz4,vtonnetz4,mtonnetz5,vtonnetz5,mtonnetz6,vtonnetz6]
    
    conn.execute("INSERT INTO Feature(NAME,mZcr,vZcr,mCentroid,vCentroid,mContrast,vContrast,mBandwidth,vBandwidth,mRollof,vRollof,mMFFC1,vMFFC1,mMFFC2,vMFFC2,mMFFC3,vMFFC3,mMFFC4,vMFFC4,mMFFC5,vMFFC5,mMFFC6,vMFFC6,mMFFC7,vMFFC7,mMFFC8,vMFFC8,mMFFC9,vMFFC9,mMFFC10,vMFFC10,mMFFC11,vMFFC11,mMFFC12,vMFFC12,mMFFC13,vMFFC13,mCqt1,vCqt1,mCqt2,vCqt2,mCqt3,vCqt3,mCqt4,vCqt4,mCqt5,vCqt5,mCqt6,vCqt6,mCqt7,vCqt7,mCqt8,vCqt8,mCqt9,vCqt9,mCqt10,vCqt10,mCqt11,vCqt11,mCqt12,vCqt12,mTonnetz1,vTonnetz1,mTonnetz2,vTonnetz2,mTonnetz3,vTonnetz3,mTonnetz4,vTonnetz4,mTonnetz5,vTonnetz5,mTonnetz6,vTonnetz6)  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", List)
    
    conn.commit()
    
    
    conn.close()
