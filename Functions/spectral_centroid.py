# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 17:27:35 2017

@author: user
"""





import numpy as np
import librosa.util as util
from librosa.core.spectrum import _spectrogram
from librosa.core.time_frequency import fft_frequencies
import matplotlib.pyplot as plt
import librosa.display

 
# -- Spectral features -- #
def spectral_centroid(y=None, sr=22050, S=None, n_fft=2048, hop_length=512,
                      freq=None):


    S, n_fft = _spectrogram(y=y, S=S, n_fft=n_fft, hop_length=hop_length)

    if not np.isrealobj(S):
        raise ParameterError('Spectral centroid is only defined '
                             'with real-valued input')
    elif np.any(S < 0):
        raise ParameterError('Spectral centroid is only defined '
                             'with non-negative energies')

    # Compute the center frequencies of each bin
    if freq is None:
        freq = fft_frequencies(sr=sr, n_fft=n_fft)

    if freq.ndim == 1:
        freq = freq.reshape((-1, 1))

    # Column-normalize S
    return np.sum(freq * util.normalize(S, norm=1, axis=0),
                  axis=0, keepdims=True)

'''
y, sr = librosa.load('audio/simpleLoop.wav')
cent=spectral_centroid(y=y, sr=sr)


plt.figure()
plt.subplot(2, 1, 1)
plt.semilogy(cent.T, label='Spectral centroid')
plt.ylabel('Hz')
plt.xticks([])
plt.xlim([0, cent.shape[-1]])
plt.legend()
plt.subplot(2, 1, 2)
librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), y_axis='log', x_axis='time')
plt.title('log Power spectrogram')
plt.tight_layout()
'''