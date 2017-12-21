# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import os
import vlc
import time
import traceback, sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib.collections import PolyCollection
import librosa
import matplotlib
import Functions.knn as knn
import Functions.getFeatures as Features
import Functions.dbImport as dbImport
import numpy as np
from librosa import display
from librosa import core
from librosa import util
from librosa.util.exceptions import ParameterError
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

'''
K değişkeni parametrik
Thread
DockWidget(Grafik,Veritabanı,)
'''
            
class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        `tuple` (exctype, value, traceback.format_exc() )

    result
        `object` data returned from processing, anything

    progress
        `int` indicating % progress

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal()


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and 
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done

class Ui_MainWindow(object):
    files = []
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(864, 900)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setChecked(True)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_8.addWidget(self.checkBox_8, 0, 0, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setChecked(True)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_8.addWidget(self.checkBox_7, 7, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_8.addWidget(self.checkBox, 5, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_8.addWidget(self.checkBox_2, 8, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_8.addWidget(self.checkBox_4, 10, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_8.addWidget(self.checkBox_3, 9, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_8.addWidget(self.checkBox_5, 11, 0, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setChecked(True)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_8.addWidget(self.checkBox_6, 12, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.gridLayout_8.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_3)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.gridLayout_8.addLayout(self.horizontalLayout_5, 6, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_8, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gill Sans Ultra Bold")
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.gridLayout_7.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 864, 21))
        self.menubar.setObjectName("menubar")
        self.fileOpMenu = QtWidgets.QMenu(self.menubar)
        self.fileOpMenu.setObjectName("fileOpMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gill Sans Ultra Bold")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(-1)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.tablLayout1TableWidget = QtWidgets.QTableWidget(self.dockWidgetContents)
        self.tablLayout1TableWidget.setShowGrid(True)
        self.tablLayout1TableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tablLayout1TableWidget.setRowCount(0)
        self.tablLayout1TableWidget.setColumnCount(40)
        self.tablLayout1TableWidget.setObjectName("tablLayout1TableWidget")
        self.tablLayout1TableWidget.horizontalHeader().setDefaultSectionSize(60)
        self.verticalLayout_3.addWidget(self.tablLayout1TableWidget)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget)
        self.dockWidget_2 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_2.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gill Sans Ultra Bold")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.songListWidget = QtWidgets.QListWidget(self.dockWidgetContents_2)
        self.songListWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.songListWidget.setStyleSheet("border-bottom-color: rgb(85, 85, 127);\n"
"font: 75 8pt \"Microsoft PhagsPa\";\n"
"text-decoration: underline;\n"
"color: rgb(170, 0, 0);\n"
"selection-color: rgb(255, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0.216, y1:0.875, x2:1, y2:0, stop:0 rgba(241, 255, 0, 111), stop:1 rgba(255, 255, 255, 255));\n"
"selection-background-color: rgb(85, 0, 255);\n"
"gridline-color: rgb(85, 170, 0);\n"
"selection-color: rgb(255, 170, 127);")
        self.songListWidget.setMovement(QtWidgets.QListView.Static)
        self.songListWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.songListWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.songListWidget.setGridSize(QtCore.QSize(0, 20))
        self.songListWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.songListWidget.setModelColumn(0)
        self.songListWidget.setObjectName("songListWidget")
        self.verticalLayout_4.addWidget(self.songListWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playSongButton = QtWidgets.QPushButton(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(24)
        sizePolicy.setVerticalStretch(24)
        sizePolicy.setHeightForWidth(self.playSongButton.sizePolicy().hasHeightForWidth())
        self.playSongButton.setSizePolicy(sizePolicy)
        self.playSongButton.setMinimumSize(QtCore.QSize(24, 24))
        self.playSongButton.setMaximumSize(QtCore.QSize(24, 24))
        self.playSongButton.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/icons/Play-icon.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"")
        self.playSongButton.setText("")
        self.playSongButton.setCheckable(False)
        self.playSongButton.setObjectName("playSongButton")
        self.horizontalLayout.addWidget(self.playSongButton)
        self.pauseSongButton = QtWidgets.QPushButton(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pauseSongButton.sizePolicy().hasHeightForWidth())
        self.pauseSongButton.setSizePolicy(sizePolicy)
        self.pauseSongButton.setMinimumSize(QtCore.QSize(24, 24))
        self.pauseSongButton.setMaximumSize(QtCore.QSize(24, 24))
        self.pauseSongButton.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/icons/Stop-icon.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"")
        self.pauseSongButton.setText("")
        self.pauseSongButton.setObjectName("pauseSongButton")
        self.horizontalLayout.addWidget(self.pauseSongButton)
        self.stopSongButton = QtWidgets.QPushButton(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopSongButton.sizePolicy().hasHeightForWidth())
        self.stopSongButton.setSizePolicy(sizePolicy)
        self.stopSongButton.setMinimumSize(QtCore.QSize(24, 24))
        self.stopSongButton.setMaximumSize(QtCore.QSize(24, 24))
        self.stopSongButton.setStyleSheet("background-color: transparent;\n"
"border-image: url(:/icons/Pause-icon.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"")
        self.stopSongButton.setText("")
        self.stopSongButton.setObjectName("stopSongButton")
        self.horizontalLayout.addWidget(self.stopSongButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.radioButton = QtWidgets.QRadioButton(self.dockWidgetContents_2)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_6.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.dockWidgetContents_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_6.addWidget(self.radioButton_2)
        self.gridLayout_9.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.dockWidgetContents_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_7.addWidget(self.lineEdit_5)
        self.gridLayout_9.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_9, 2, 0, 1, 1)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_2)
        self.dockWidget_3 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents_3)
        self.tabWidget.setObjectName("tabWidget")
#        self.tab = QtWidgets.QWidget()
#        self.tab.setObjectName("tab")
#        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
#        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
#        self.gridLayout_3.setObjectName("gridLayout_3")
#        self.tabLayout1 = QtWidgets.QGridLayout()
#        self.tabLayout1.setObjectName("tabLayout1")
#        self.tabLayout1Label = QtWidgets.QLabel(self.tab)
#        self.tabLayout1Label.setAlignment(QtCore.Qt.AlignCenter)
#        self.tabLayout1Label.setObjectName("tabLayout1Label")
#        self.tabLayout1.addWidget(self.tabLayout1Label, 1, 0, 1, 1)
#        self.gridLayout_3.addLayout(self.tabLayout1, 0, 0, 1, 1)
#        self.tabWidget.addTab(self.tab, "")
#        self.tab_2 = QtWidgets.QWidget()
#        self.tab_2.setObjectName("tab_2")
#        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
#        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
#        self.gridLayout_4.setObjectName("gridLayout_4")
#        self.tabLayout2 = QtWidgets.QGridLayout()
#        self.tabLayout2.setObjectName("tabLayout2")
#        self.gridLayout_4.addLayout(self.tabLayout2, 0, 0, 1, 1)
#        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_3)
        self.actionNew_Data_Import = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Music-Library-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Data_Import.setIcon(icon)
        self.actionNew_Data_Import.setObjectName("actionNew_Data_Import")
        self.actionPrepared_Data_Import_csv = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/add-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrepared_Data_Import_csv.setIcon(icon1)
        self.actionPrepared_Data_Import_csv.setObjectName("actionPrepared_Data_Import_csv")
        self.fileOpMenu.addAction(self.actionNew_Data_Import)
        self.fileOpMenu.addAction(self.actionPrepared_Data_Import_csv)
        self.menubar.addAction(self.fileOpMenu.menuAction())

        self.songListWidget.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.stopSongButton.clicked.connect(self.stopSong)
        self.pauseSongButton.clicked.connect(self.pauseSong)
        self.playSongButton.clicked.connect(self.playSong)
#        self.loadButton.clicked.connect(self.openFileNamesDialog)
        self.actionNew_Data_Import.triggered.connect(self.newDataImp)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Thread operations
        self.threadpool = QThreadPool()
        # On Launch Run this func.
        self.loadMusicOnLaunch()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    def progress_fn(self):
        self.statusbar.showMessage('Database operations going on ...')

    def execute_this_fn(self, progress_callback):
        progress_callback.emit()
        result, veriler = self.connectDB()
        return result, veriler

    def thread_complete(self):
        self.statusbar.showMessage('Database operations completed.')
        
    def threadop(self):
        # Pass the function to execute
        worker = Worker(self.execute_this_fn) # Any other args, kwargs are passed to the run function
        worker.signals.result.connect(self.showFeatureOnNewTab)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.threadpool.start(worker)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_8.setText(_translate("MainWindow", "Tonnetz"))
        self.checkBox_7.setText(_translate("MainWindow", "MFCC"))
        self.checkBox.setText(_translate("MainWindow", "Chroma CQT"))
        self.checkBox_2.setText(_translate("MainWindow", "Spectral Rollof"))
        self.checkBox_4.setText(_translate("MainWindow", "Spectral Contrast"))
        self.checkBox_3.setText(_translate("MainWindow", "Spectral Bandwith"))
        self.checkBox_5.setText(_translate("MainWindow", "Spectral Centroid"))
        self.checkBox_6.setText(_translate("MainWindow", "Zero Crossing"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "Recommendations"))
        self.fileOpMenu.setTitle(_translate("MainWindow", "File operations"))
        self.label.setText(_translate("MainWindow", "Features"))
        self.tablLayout1TableWidget.setSortingEnabled(False)
        self.label_2.setText(_translate("MainWindow", "Playlist"))
        self.songListWidget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        __sortingEnabled = self.songListWidget.isSortingEnabled()
        self.songListWidget.setSortingEnabled(False)
        self.songListWidget.setSortingEnabled(__sortingEnabled)
        self.radioButton.setText(_translate("MainWindow", "kNN"))
        self.radioButton_2.setText(_translate("MainWindow", "Kmeans"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
#        self.tabLayout1Label.setText(_translate("MainWindow", "TextLabel"))
#        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
#        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.actionNew_Data_Import.setText(_translate("MainWindow", "New Data Import (mp3) "))
        self.actionPrepared_Data_Import_csv.setText(_translate("MainWindow", "Prepared Data Import (csv) "))

    def loadMusicOnLaunch(self):
        import glob
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = dir_path + '\Musics\*.mp3'
        self.files = glob.glob(dir_path)
        for file in self.files:
            x = file.split('\\')
            self.songListWidget.addItems(x[-1:])
        
    def newDataImp(self):
        fileNames , _ = QtWidgets.QFileDialog.getOpenFileNames(None, 'Open File', os.getenv('HOME'), "Musics (*.mp3 *.wav)")
        files = []
        names = []
        if fileNames:
#            Just keep file names not path
            for i in range(0,len(fileNames)):
                files.append(fileNames[i])
                x = fileNames[i].split('/')
                names.append(x[-1:][0])
        #return files, names
        for i in range(len(names)):
            dbImport.dbImport(names[i],files[i])
        
    def openFileNamesDialog(self): 
        fileNames , _ = QtWidgets.QFileDialog.getOpenFileNames(None, 'Open File', os.getenv('HOME'), "Musics (*.mp3 *.wav)")
        if fileNames:
#            Just keep file names not path
            for i in range(0,len(fileNames)):
                self.files.append(fileNames[i])
                x = fileNames[i].split('/')
                self.songListWidget.addItems(x[-1:])
            print(self.files)
            
    def playSong(self):
        if self.songListWidget.currentItem():
            media = instance.media_new(self.files[self.songListWidget.currentRow()])
            player.set_media(media)
            player.play()
            if self.threadpool.activeThreadCount() == 0:
                self.threadop()
                
    def addnewTab(self):
            # Adds new tab
            self.tab_3 = QtWidgets.QWidget()
            self.tab_3.setObjectName("tab_3")
            self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
            self.tabWidget.addTab(self.tab_3, "")
        
    def connectDB(self):
        import sqlite3
        vt = sqlite3.connect('Functions\DB\DB.db') #r'C:\Users\merta\Desktop\Dersler\bitirme\LicenseProject\GUI\Functions\DB\DB.db'
        self.statusbar.showMessage('Opened database successfully')
        conn=vt.cursor()
        self.statusbar.showMessage('Executing tables ...')
        conn.execute("SELECT * FROM Feature")
        
        veriler = conn.fetchall()
        
        trainData=[]
        
        for x in veriler:
            trainData.append(x[2:])
        self.statusbar.showMessage('Extracting features ...')   
        testData=Features.features(self.files[self.songListWidget.currentRow()])
        #testData= trainData[0]
        
        result=knn.knn(trainData,testData,2,72)
        names=[]
        for i in result:
            print(veriler[i][1],i)
            names.append(veriler[i][1])        
        conn.close()
        return result,veriler

        
    def showFeatureOnNewTab(self, result):
       # Adds new tab
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        ''' Şarkı seçildikten sonra seçilen değişirse
        Yeni tab adı o an seçili olanı alıyor. '''
        self.tabWidget.addTab(self.tab, self.files[self.songListWidget.currentRow()].split('\\')[-1:][0])
        self.tabLayout1 = QtWidgets.QGridLayout()
        self.tabLayout1.setObjectName("tabLayout1")
        self.tablLayout1TableWidget = QtWidgets.QTableWidget(self.tab)
        self.tablLayout1TableWidget.setObjectName("tablLayout1TableWidget")
        self.tabLayout1.addWidget(self.tablLayout1TableWidget)
        self.tablLayout1TableWidget.setRowCount(4)
        self.tablLayout1TableWidget.setColumnCount(36)
        headers = ['Song','mZCR','vZCR','mCent','vCent','mCont','vCont','mBand','vBand','mRoll','vRoll','mMFCC1','vMFCC1','mMFCC2','vMFCC2','mMFCC3','vMFCC3','mMFCC4','vMFCC4','mMFCC5','vMFCC5','mMFCC6','vMFCC6','mMFCC7','vMFCC7','mMFCC8','vMFCC8','mMFCC9','vMFCC9','mMFCC10','vMFCC10','mMFCC11','vMFCC11','mMFCC12','vMFCC12','mMFCC13','vMFCC13']
        self.tablLayout1TableWidget.setHorizontalHeaderLabels(headers)
        i=0
        '''
        for x in names:
            self.tablLayout1TableWidget.setItem(i,0, QTableWidgetItem(x))
            i=i+1
        '''
        i=0
        for x in result[0]:
            for j in range(36):
                item = QTableWidgetItem(str(result[1][x][j+1]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tablLayout1TableWidget.setItem(i,j, item)
            i += 1
            
            
        '''
        self.tablLayout1TableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        self.tablLayout1TableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tablLayout1TableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.tablLayout1TableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.tablLayout1TableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
        self.tablLayout1TableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
        self.tablLayout1TableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
        self.tablLayout1TableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
        '''
        self.gridLayout.addLayout(self.tabLayout1, 0, 0, 1, 1)
        sc = MyStaticMplCanvas(self.centralwidget, width=2, height=1, dpi=100, index=self.files[self.songListWidget.currentRow()])
        self.tabLayout1.addWidget(sc)
#       self.tabWidget.setCurrentIndex(len(sel))
        self.tabWidget.setCurrentWidget(self.tab)

        
    def pauseSong(self):
        if self.songListWidget.currentItem():
            player.pause()
            
    def stopSong(self):
        if self.songListWidget.currentItem():
            player.stop()
            
class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100, index=0):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.compute_initial_figure(index)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self, index):
        pass
    
class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""

    def compute_initial_figure(self, index):
        y, sr = librosa.load(index)
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


import Icons.icons            
#VLC Player conf.          
instance = vlc.Instance()
player = instance.media_player_new()
global files
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())