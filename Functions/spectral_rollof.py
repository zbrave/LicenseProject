# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:31:57 2017

@author: user
"""

#----------------------------------
import librosa
import numpy as np
from librosa.core.spectrum import _spectrogram
from librosa.core.time_frequency import fft_frequencies

def spectral_rolloff(y=None, sr=22050, S=None, n_fft=2048, hop_length=512,
                     freq=None, roll_percent=0.85):

    if not 0.0 < roll_percent < 1.0:
        raise ParameterError('roll_percent must lie in the range (0, 1)')

    S, n_fft = _spectrogram(y=y, S=S, n_fft=n_fft, hop_length=hop_length)

    if not np.isrealobj(S):
        raise ParameterError('Spectral rolloff is only defined '
                             'with real-valued input')
    elif np.any(S < 0):
        raise ParameterError('Spectral rolloff is only defined '
                             'with non-negative energies')

    # Compute the center frequencies of each bin
    if freq is None:
        freq = fft_frequencies(sr=sr, n_fft=n_fft)

    # Make sure that frequency can be broadcast
    if freq.ndim == 1:
        freq = freq.reshape((-1, 1))

    total_energy = np.cumsum(S, axis=0)

    threshold = roll_percent * total_energy[-1]

    ind = np.where(total_energy < threshold, np.nan, 1)

    return np.nanmin(ind * freq, axis=0, keepdims=True)



'''
#From time-series input
y, sr = librosa.load('audio/simpleLoop.wav')
rolloff = spectral_rolloff(y=y, sr=sr)
rolloff
#from spectrogram input
S, phase = librosa.magphase(librosa.stft(y))
spectral_rolloff(S=S, sr=sr)

# With a higher roll percentage:
spectral_rolloff(y=y, sr=sr, roll_percent=0.95)

import matplotlib.pyplot as plt
import librosa.display
plt.figure()
plt.subplot(2, 1, 1)
plt.semilogy(rolloff.T, label='Roll-off frequency')
plt.ylabel('Hz')
plt.xticks([])
plt.xlim([0, rolloff.shape[-1]])
plt.legend()
plt.subplot(2, 1, 2)
librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max),y_axis='log', x_axis='time')
plt.title('log Power spectrogram')
plt.tight_layout()
'''