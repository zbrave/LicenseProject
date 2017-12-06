# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:51:55 2017

@author: user
"""



#------------------------

import librosa
import numpy as np
from spectral_centroid import spectral_centroid #our spectral_centroid.py
from librosa.core.time_frequency import fft_frequencies
import librosa.util as util
from librosa.core.spectrum import _spectrogram

def spectral_bandwidth(y=None, sr=22050, S=None, n_fft=2048, hop_length=512,
                       freq=None, centroid=None, norm=True, p=2):


    S, n_fft = _spectrogram(y=y, S=S, n_fft=n_fft, hop_length=hop_length)

    if not np.isrealobj(S):
        raise ParameterError('Spectral bandwidth is only defined '
                             'with real-valued input')
    elif np.any(S < 0):
        raise ParameterError('Spectral bandwidth is only defined '
                             'with non-negative energies')

    if centroid is None:
        centroid = spectral_centroid(y=y, sr=sr, S=S,
                                     n_fft=n_fft,
                                     hop_length=hop_length,
                                     freq=freq)

    # Compute the center frequencies of each bin
    if freq is None:
        freq = fft_frequencies(sr=sr, n_fft=n_fft)

    if freq.ndim == 1:
        deviation = np.abs(np.subtract.outer(freq, centroid[0]))
    else:
        deviation = np.abs(freq - centroid[0])

    # Column-normalize S
    if norm:
        S = util.normalize(S, norm=1, axis=0)

    return np.sum(S * deviation**p, axis=0, keepdims=True)**(1./p)



'''
# From time-series input
y, sr = librosa.load('audio/simpleLoop.wav')
spec_bw = spectral_bandwidth(y=y, sr=sr)
spec_bw

import matplotlib.pyplot as plt
import librosa.display
plt.figure()
plt.subplot(2, 1, 1)
plt.semilogy(spec_bw.T, label='Spectral bandwidth')
plt.ylabel('Hz')
plt.xticks([])
plt.xlim([0, spec_bw.shape[-1]])
plt.legend()
plt.subplot(2, 1, 2)
librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max),y_axis='log', x_axis='time')
plt.title('log Power spectrogram')
plt.tight_layout()
'''
