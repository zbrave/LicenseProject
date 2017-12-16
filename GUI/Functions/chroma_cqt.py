# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 01:49:42 2017

@author: user
"""
import numpy as np
import librosa
import librosa.filters as filters
import librosa.util as util
from librosa.core.constantq import cqt, hybrid_cqt
def chroma_cqt(y=None, sr=22050, C=None, hop_length=512, fmin=None,
               norm=np.inf, threshold=0.0, tuning=None, n_chroma=12,
               n_octaves=7, window=None, bins_per_octave=None, cqt_mode='full'):

    cqt_func = {'full': cqt, 'hybrid': hybrid_cqt}

    if bins_per_octave is None:
        bins_per_octave = n_chroma

    # Build the CQT if we don't have one already
    if C is None:
        C = np.abs(cqt_func[cqt_mode](y, sr=sr,
                                      hop_length=hop_length,
                                      fmin=fmin,
                                      n_bins=n_octaves * bins_per_octave,
                                      bins_per_octave=bins_per_octave,
                                      tuning=tuning))

    # Map to chroma
    cq_to_chr = filters.cq_to_chroma(C.shape[0],
                                     bins_per_octave=bins_per_octave,
                                     n_chroma=n_chroma,
                                     fmin=fmin,
                                     window=window)
    chroma = cq_to_chr.dot(C)

    if threshold is not None:
        chroma[chroma < threshold] = 0.0

    # Normalize
    if norm is not None:
        chroma = util.normalize(chroma, norm=norm, axis=0)

    return chroma




'''
y, sr = librosa.load('audio/simpleLoop.wav')

chroma_cq = chroma_cqt(y=y, sr=sr)

import matplotlib.pyplot as plt
import librosa.display
plt.figure()
plt.subplot(2,1,2)
librosa.display.specshow(chroma_cq, y_axis='chroma', x_axis='time')
plt.title('chroma_cqt')
plt.colorbar()
plt.tight_layout()
'''