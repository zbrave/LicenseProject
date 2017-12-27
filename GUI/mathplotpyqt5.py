# embedding_in_qt5.py --- Simple Qt5 application embedding matplotlib canvases
#
# Copyright (C) 2005 Florent Rougon
#               2006 Darren Dale
#               2015 Jens H Nielsen
#
# This file is an example program for matplotlib. It may be used and
# modified with no restriction; raw copies as well as modified versions
# may be distributed without limitation.

from __future__ import unicode_literals
import sys
import os
import random
import matplotlib
import warnings

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import Formatter, ScalarFormatter
from matplotlib.ticker import LogLocator, FixedLocator, MaxNLocator
from matplotlib.ticker import SymmetricalLogLocator
import librosa
from librosa import display
from librosa import core
from librosa import util
from librosa.util.exceptions import ParameterError
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

progname = os.path.basename(sys.argv[0])
progversion = "0.1"


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=3, height=2, dpi=250):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""

    def compute_initial_figure(self):
        y, sr = librosa.load(librosa.util.example_audio_file(), duration=10)
        max_points=5e4
        x_axis='time'
        offset=0.0
        max_sr=1000
        util.valid_audio(y, mono=False)

        if not (isinstance(max_sr, int) and max_sr > 0):
            raise ParameterError('max_sr must be a non-negative integer')
    
        target_sr = sr
        hop_length = 1
    
        if max_points is not None:
            if max_points <= 0:
                raise ParameterError('max_points must be strictly positive')
    
            if max_points < y.shape[-1]:
                target_sr = min(max_sr, (sr * y.shape[-1]) // max_points)
    
            hop_length = sr // target_sr
    
            if y.ndim == 1:
                y = util.frame(y, hop_length).max(axis=0)
            else:
                y = np.vstack([util.frame(_, hop_length).max(axis=0) for _ in y])
    
        if y.ndim > 1:
            y_top = y[0]
            y_bottom = -y[1]
        else:
            y_top = y
            y_bottom = -y
    
        axes = plt.gca()
    
#        kwargs.setdefault('color', next(axes._get_lines.prop_cycler)['color'])
    
        locs = offset + core.frames_to_time(np.arange(len(y_top)),
                                            sr=sr,
                                            hop_length=hop_length)
        self.axes.fill_between(locs, y_bottom, y_top)
    
        axes.set_xlim([locs.min(), locs.max()])
        if x_axis == 'time':
            axes.xaxis.set_major_formatter(display.TimeFormatter(lag=False))
            axes.xaxis.set_label_text('Time')
        elif x_axis is None or x_axis in ['off', 'none']:
            axes.set_xticks([])
        else:
            raise ParameterError('Unknown x_axis value: {}'.format(x_axis))

class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def compute_initial_figure(self):
        y, sr = librosa.load(librosa.util.example_audio_file(), duration=10)
        max_points=5e4
        x_axis='time'
        offset=0.0
        max_sr=1000
        util.valid_audio(y, mono=False)

        if not (isinstance(max_sr, int) and max_sr > 0):
            raise ParameterError('max_sr must be a non-negative integer')
    
        target_sr = sr
        hop_length = 1
    
        if max_points is not None:
            if max_points <= 0:
                raise ParameterError('max_points must be strictly positive')
    
            if max_points < y.shape[-1]:
                target_sr = min(max_sr, (sr * y.shape[-1]) // max_points)
    
            hop_length = sr // target_sr
    
            if y.ndim == 1:
                y = util.frame(y, hop_length).max(axis=0)
            else:
                y = np.vstack([util.frame(_, hop_length).max(axis=0) for _ in y])
    
        if y.ndim > 1:
            y_top = y[0]
            y_bottom = -y[1]
        else:
            y_top = y
            y_bottom = -y
    
        axes = plt.gca()
    
#        kwargs.setdefault('color', next(axes._get_lines.prop_cycler)['color'])
    
        locs = offset + core.frames_to_time(np.arange(len(y_top)),
                                            sr=sr,
                                            hop_length=hop_length)
        self.axes.fill_between(locs, y_bottom, y_top)
    
        axes.set_xlim([locs.min(), locs.max()])
        if x_axis == 'time':
            axes.xaxis.set_major_formatter(display.TimeFormatter(lag=False))
            axes.xaxis.set_label_text('Time')
        elif x_axis is None or x_axis in ['off', 'none']:
            axes.set_xticks([])
        else:
            raise ParameterError('Unknown x_axis value: {}'.format(x_axis))

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        y, sr = librosa.load(librosa.util.example_audio_file(), duration=10)
        max_points=5e4
        x_axis='time'
        offset=0.0
        max_sr=1000
        util.valid_audio(y, mono=False)

        if not (isinstance(max_sr, int) and max_sr > 0):
            raise ParameterError('max_sr must be a non-negative integer')
    
        target_sr = sr
        hop_length = 1
    
        if max_points is not None:
            if max_points <= 0:
                raise ParameterError('max_points must be strictly positive')
    
            if max_points < y.shape[-1]:
                target_sr = min(max_sr, (sr * y.shape[-1]) // max_points)
    
            hop_length = sr // target_sr
    
            if y.ndim == 1:
                y = util.frame(y, hop_length).max(axis=0)
            else:
                y = np.vstack([util.frame(_, hop_length).max(axis=0) for _ in y])
    
        if y.ndim > 1:
            y_top = y[0]
            y_bottom = -y[1]
        else:
            y_top = y
            y_bottom = -y
    
        axes = plt.gca()
    
#        kwargs.setdefault('color', next(axes._get_lines.prop_cycler)['color'])
    
        locs = offset + core.frames_to_time(np.arange(len(y_top)),
                                            sr=sr,
                                            hop_length=hop_length)
        self.axes.fill_between(locs, y_bottom, y_top, where=50 >= y_bottom, facecolor='green', interpolate=True)
        self.axes.fill_between(locs, y_bottom, y_top, where=50 <= y_bottom, facecolor='red', interpolate=True)
    
        axes.set_xlim([locs.min(), locs.max()])
        if x_axis == 'time':
            axes.xaxis.set_major_formatter(display.TimeFormatter(lag=False))
            axes.xaxis.set_label_text('Time')
        elif x_axis is None or x_axis in ['off', 'none']:
            axes.set_xticks([])
        else:
            raise ParameterError('Unknown x_axis value: {}'.format(x_axis))
        
        self.draw()


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QtWidgets.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QtWidgets.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QtWidgets.QWidget(self)

        l = QtWidgets.QVBoxLayout(self.main_widget)
        sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        l.addWidget(sc)
        l.addWidget(dc)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 2000)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QtWidgets.QMessageBox.about(self, "About",
                                    """embedding_in_qt5.py example
Copyright 2005 Florent Rougon, 2006 Darren Dale, 2015 Jens H Nielsen

This program is a simple example of a Qt5 application embedding matplotlib
canvases.

It may be used and modified with no restriction; raw copies as well as
modified versions may be distributed without limitation.

This is modified from the embedding in qt4 example to show the difference
between qt4 and qt5"""
                                )


qApp = QtWidgets.QApplication(sys.argv)

aw = ApplicationWindow()
aw.setWindowTitle("%s" % progname)
aw.show()
sys.exit(qApp.exec_())
#qApp.exec_()