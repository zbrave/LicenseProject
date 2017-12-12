# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 04:00:11 2017

@author: user
"""

import librosa
import librosa.util as util
import numpy as np
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
'''    
y, sr = librosa.load('audio/simpleLoop.wav')
zcr = zero_crossing_rate(y);
'''
