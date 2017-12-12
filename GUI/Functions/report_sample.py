# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 17:15:08 2017

@author: merta
"""

import librosa.display

# Compare a long-window STFT chromagram to the CQT chromagram
def cqt(y,sr,filename):
#    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr,
#                                              n_chroma=12, n_fft=4096)
    chroma_cq = librosa.feature.chroma_cqt(y=y, sr=sr)
    
    import matplotlib.pyplot as plt
    plt.figure()
#    plt.subplot(2,1,1)
#    librosa.display.specshow(chroma_stft, y_axis='chroma')
#    plt.title('chroma_stft')
#    plt.colorbar()
    plt.subplot(2,1,2)
    librosa.display.specshow(chroma_cq, y_axis='chroma', x_axis='time')
    plt.title(filename)
    plt.colorbar()
    plt.tight_layout()
    return chroma_cq

#------------------------

import librosa
import numpy as np
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
    
#y, sr = librosa.load(librosa.util.example_audio_file(),
#                         offset=10, duration=15)
y1, sr1 = librosa.load(r'C:\Users\merta\Desktop\Dersler\bitirme\LicenseProject\Samples\Barış Manço - Kol Dugmeleri.mp3')
#chroma1 = cqt(y1,sr1,'Barış Manço - Kol Dugmeleri')
y2, sr2 = librosa.load(r'C:\Users\merta\Desktop\Dersler\bitirme\LicenseProject\Samples\Musa Eroğlu Mihriban.mp3')
#chroma2 = cqt(y2,sr2,'Musa Eroğlu Mihriban')
y3, sr3 = librosa.load(r'C:\Users\merta\Desktop\Dersler\bitirme\LicenseProject\Samples\Sevince - Erkin Koray.mp3')
#chroma3 = cqt(y3,sr3,'Sevince - Erkin Koray')
y4, sr4 = librosa.load(r'C:\Users\merta\Desktop\Dersler\bitirme\LicenseProject\Samples\Ahmet.mp3')

y5, sr5 = librosa.load(r'C:\Users\merta\Desktop\Dersler\bitirme\LicenseProject\Samples\Baha.mp3')
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

#-------------------------
spec_band1 = spectral_bandwidth(y1)
spec_band2 = spectral_bandwidth(y2)
spec_band3 = spectral_bandwidth(y3)

spec_cent1 = spectral_centroid(y1)
spec_cent2 = spectral_centroid(y2)
spec_cent3 = spectral_centroid(y3)

plt.figure()
plt.subplot(2, 1, 1)
plt.semilogy(spec_band1.T, label='Spectral bandwidth')
plt.ylabel('Hz')
plt.xticks([])
plt.xlim([0, spec_band1.shape[-1]])
plt.legend()
plt.title('Barış Manço - Kol Dugmeleri')
plt.tight_layout()

plt.figure()
plt.subplot(2, 1, 1)
plt.semilogy(spec_band2.T, label='Spectral bandwidth')
plt.ylabel('Hz')
plt.xticks([])
plt.xlim([0, spec_band2.shape[-1]])
plt.legend()
plt.title('Musa Eroğlu Mihriban')
plt.tight_layout()

plt.figure()
plt.subplot(2, 1, 1)
plt.semilogy(spec_band3.T, label='Spectral bandwidth')
plt.ylabel('Hz')
plt.xticks([])
plt.xlim([0, spec_band3.shape[-1]])
plt.legend()
plt.title('Sevince - Erkin Koray')
plt.tight_layout()

cent = librosa.feature.spectral_centroid(y=y1, sr=22050)
cent
# array([[ 4382.894,   626.588, ...,  5037.07 ,  5413.398]])

# From spectrogram input:

S, phase = librosa.magphase(librosa.stft(y=y1))
librosa.feature.spectral_centroid(S=S)
# array([[ 4382.894,   626.588, ...,  5037.07 ,  5413.398]])

# Using variable bin center frequencies:

if_gram, D = librosa.ifgram(y1)
librosa.feature.spectral_centroid(S=np.abs(D), freq=if_gram)
# array([[ 4420.719,   625.769, ...,  5011.86 ,  5221.492]])

# Plot the result

import matplotlib.pyplot as plt
plt.figure()
plt.subplot(2, 1, 1)
plt.semilogy(cent.T, label='Spectral centroid')
plt.ylabel('Hz')
plt.xticks([])
plt.xlim([0, cent.shape[-1]])
plt.legend()
plt.subplot(2, 1, 2)
librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max),
                         y_axis='log', x_axis='time')
plt.title('log Power spectrogram')
plt.tight_layout()

cent = librosa.feature.spectral_centroid(y=y2, sr=22050)
cent
# array([[ 4382.894,   626.588, ...,  5037.07 ,  5413.398]])

# From spectrogram input:

S, phase = librosa.magphase(librosa.stft(y=y2))
librosa.feature.spectral_centroid(S=S)
# array([[ 4382.894,   626.588, ...,  5037.07 ,  5413.398]])

# Using variable bin center frequencies:

if_gram, D = librosa.ifgram(y2)
librosa.feature.spectral_centroid(S=np.abs(D), freq=if_gram)
# array([[ 4420.719,   625.769, ...,  5011.86 ,  5221.492]])

# Plot the result

import matplotlib.pyplot as plt
plt.figure()
plt.subplot(2, 1, 1)
plt.semilogy(cent.T, label='Spectral centroid')
plt.ylabel('Hz')
plt.xticks([])
plt.xlim([0, cent.shape[-1]])
plt.legend()
plt.subplot(2, 1, 2)
librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max),
                         y_axis='log', x_axis='time')
plt.title('log Power spectrogram')
plt.tight_layout()

cent = librosa.feature.spectral_centroid(y=y3, sr=22050)
cent
# array([[ 4382.894,   626.588, ...,  5037.07 ,  5413.398]])

# From spectrogram input:

S, phase = librosa.magphase(librosa.stft(y=y3))
librosa.feature.spectral_centroid(S=S)
# array([[ 4382.894,   626.588, ...,  5037.07 ,  5413.398]])

# Using variable bin center frequencies:

if_gram, D = librosa.ifgram(y3)
librosa.feature.spectral_centroid(S=np.abs(D), freq=if_gram)
# array([[ 4420.719,   625.769, ...,  5011.86 ,  5221.492]])

# Plot the result

import matplotlib.pyplot as plt
plt.figure()
plt.subplot(2, 1, 1)
plt.semilogy(cent.T, label='Spectral centroid')
plt.ylabel('Hz')
plt.xticks([])
plt.xlim([0, cent.shape[-1]])
plt.legend()
plt.subplot(2, 1, 2)
librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max),
                         y_axis='log', x_axis='time')
plt.title('log Power spectrogram')
plt.tight_layout()


import numpy as np
import librosa
from librosa.core.spectrum import _spectrogram, power_to_db
from librosa.core.time_frequency import fft_frequencies

def spectral_contrast(y=None, sr=22050, S=None, n_fft=2048, hop_length=512,
                      freq=None, fmin=200.0, n_bands=6, quantile=0.02,
                      linear=False):


    S, n_fft = _spectrogram(y=y, S=S, n_fft=n_fft, hop_length=hop_length)

    # Compute the center frequencies of each bin
    if freq is None:
        freq = fft_frequencies(sr=sr, n_fft=n_fft)

    freq = np.atleast_1d(freq)

    if freq.ndim != 1 or len(freq) != S.shape[0]:
        raise ParameterError('freq.shape mismatch: expected '
                             '({:d},)'.format(S.shape[0]))

    if n_bands < 1 or not isinstance(n_bands, int):
        raise ParameterError('n_bands must be a positive integer')

    if not 0.0 < quantile < 1.0:
        raise ParameterError('quantile must lie in the range (0, 1)')

    if fmin <= 0:
        raise ParameterError('fmin must be a positive number')

    octa = np.zeros(n_bands + 2)
    octa[1:] = fmin * (2.0**np.arange(0, n_bands + 1))

    if np.any(octa[:-1] >= 0.5 * sr):
        raise ParameterError('Frequency band exceeds Nyquist. '
                             'Reduce either fmin or n_bands.')

    valley = np.zeros((n_bands + 1, S.shape[1]))
    peak = np.zeros_like(valley)

    for k, (f_low, f_high) in enumerate(zip(octa[:-1], octa[1:])):
        current_band = np.logical_and(freq >= f_low, freq <= f_high)

        idx = np.flatnonzero(current_band)

        if k > 0:
            current_band[idx[0] - 1] = True

        if k == n_bands:
            current_band[idx[-1] + 1:] = True

        sub_band = S[current_band]

        if k < n_bands:
            sub_band = sub_band[:-1]

        # Always take at least one bin from each side
        idx = np.rint(quantile * np.sum(current_band))
        idx = int(np.maximum(idx, 1))

        sortedr = np.sort(sub_band, axis=0)

        valley[k] = np.mean(sortedr[:idx], axis=0)
        peak[k] = np.mean(sortedr[-idx:], axis=0)

    if linear:
        return peak - valley
    else:
        return power_to_db(peak) - power_to_db(valley)

import numpy as np
from librosa.core.spectrum import _spectrogram
from librosa.core.time_frequency import fft_frequencies
import librosa

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

import librosa.util as util
import numpy as np
import librosa
import six




def zero_crossing_rate(y, frame_length=2048, hop_length=512, center=True,
                       **kwargs):
    global CROSSING
    util.valid_audio(y)

    if center:
        y = np.pad(y, int(frame_length // 2), mode='edge')

    y_framed = util.frame(y, frame_length, hop_length)

    kwargs['axis'] = 0
    kwargs.setdefault('pad', False)

    crossings = zero_crossings(y_framed, **kwargs)
    CROSSING = crossings
    print(crossings)

    return np.mean(crossings, axis=0, keepdims=True)


def zero_crossings(y, threshold=1e-10, ref_magnitude=None, pad=True,
                   zero_pos=True, axis=-1):
    '''Find the zero-crossings of a signal `y`: indices `i` such that
    `sign(y[i]) != sign(y[j])`.

    '''

    # Clip within the threshold
    if threshold is None:
        threshold = 0.0

    if six.callable(ref_magnitude):
        threshold = threshold * ref_magnitude(np.abs(y))

    elif ref_magnitude is not None:
        threshold = threshold * ref_magnitude

    if threshold > 0:
        y = y.copy()
        y[np.abs(y) <= threshold] = 0

    # Extract the sign bit
    if zero_pos:
        y_sign = np.signbit(y)
    else:
        y_sign = np.sign(y)

    # Find the change-points by slicing
    slice_pre = [slice(None)] * y.ndim
    slice_pre[axis] = slice(1, None)

    slice_post = [slice(None)] * y.ndim
    slice_post[axis] = slice(-1)

    # Since we've offset the input by one, pad back onto the front
    padding = [(0, 0)] * y.ndim
    padding[axis] = (1, 0)

    return np.pad((y_sign[slice_post] != y_sign[slice_pre]),
                  padding,
                  mode='constant',
                  constant_values=pad)

y, sr = librosa.load('audio/simpleLoop.wav')
zcr = zero_crossing_rate(y);

a = np.array([[np.mean(spec_band1), np.mean(spec_band2), np.mean(spec_band3)],[np.mean(spec_cent1), np.mean(spec_cent2), np.mean(spec_cent3)],[np.mean(spec_cont1), np.mean(spec_cont2), np.mean(spec_cont3)],[np.mean(spec_zcr1), np.mean(spec_zcr2), np.mean(spec_zcr3)],[,0,1]])

