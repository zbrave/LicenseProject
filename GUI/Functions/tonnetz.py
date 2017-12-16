# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 02:01:10 2017

@author: user
"""

from Functions.chroma_cqt import chroma_cqt 
import librosa
import numpy as np
import librosa.util as util

def tonnetz(y=None, sr=22050, chroma=None):


    if y is None and chroma is None:
        raise ParameterError('Either the audio samples or the chromagram must be '
                             'passed as an argument.')

    if chroma is None:
        chroma = chroma_cqt(y=y, sr=sr)

    # Generate Transformation matrix
    dim_map = np.linspace(0, 12, num=chroma.shape[0], endpoint=False)

    scale = np.asarray([7. / 6, 7. / 6,
                        3. / 2, 3. / 2,
                        2. / 3, 2. / 3])

    V = np.multiply.outer(scale, dim_map)

    # Even rows compute sin()
    V[::2] -= 0.5

    R = np.array([1, 1,         # Fifths
                  1, 1,         # Minor
                  0.5, 0.5])    # Major

    phi = R[:, np.newaxis] * np.cos(np.pi * V)

    # Do the transform to tonnetz
    return phi.dot(util.normalize(chroma, norm=1, axis=0))


'''
y, sr = librosa.load('audio/simpleLoop.wav')
y = librosa.effects.harmonic(y)
tonnetz = tonnetz(y=y, sr=sr)
tonnetz


import matplotlib.pyplot as plt
plt.subplot(2, 1, 1)
librosa.display.specshow(tonnetz, y_axis='tonnetz')
plt.colorbar()
plt.title('Tonal Centroids (Tonnetz)')
plt.subplot(2, 1, 2)
librosa.display.specshow(librosa.feature.chroma_cqt(y, sr=sr),y_axis='chroma', x_axis='time')
plt.colorbar()
plt.title('Chroma')
plt.tight_layout()
'''