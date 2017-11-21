# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 17:27:35 2017

@author: user
"""

import soundfile as sf
signal, fs = sf.read(r'C:\Users\merta\Desktop\Dersler\bitirme\simpleLoop.wav')

import numpy as np
import matplotlib.pyplot as plt

def spectral_centroid(x, samplerate=44100):
    magnitudes = np.abs(np.fft.rfft(x)) # magnitudes of positive frequencies
    #print(magnitudes)
    length = len(x)
    freqs = np.abs(np.fft.fftfreq(length, 1.0/samplerate)[:length//2+1]) # positive frequencies
    #C, S = np.cos(freqs), np.sin(freqs)
    #plt.plot(freqs, C)
    #plt.plot(freqs, S)
    #plt.show()
    #print(freqs)
    return np.sum(magnitudes*freqs) / np.sum(magnitudes) # return weighted mean

spectral_centroid1=spectral_centroid(signal)

#çözüm 2
from numpy import abs, sum, linspace
from numpy.fft import rfft

spectrum = abs(rfft(signal))
normalized_spectrum = spectrum / sum(spectrum)  # like a probability mass function
normalized_frequencies = linspace(0, 1, len(spectrum))
spectral_centroid2 = sum(normalized_frequencies * normalized_spectrum)
C, S = np.cos(normalized_frequencies), np.sin(normalized_frequencies)
plt.plot(normalized_frequencies, C)
plt.plot(normalized_frequencies, S)
plt.show() #merto kaçtım ben görüşürüz aaaaaaabi