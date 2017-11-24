# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import os
import vlc
import matplotlib.pyplot as plt
import librosa
import matplotlib
from numpy import arange, sin, pi
matplotlib.use("Qt5Agg")
from librosa import display
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QVBoxLayout, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import pyqtSlot
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(432, 478)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 341, 227))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.songListWidget = QtWidgets.QListWidget(self.widget)
        self.songListWidget.setObjectName("songListWidget")
        self.horizontalLayout_2.addWidget(self.songListWidget)
        self.loadButton = QtWidgets.QPushButton(self.widget)
        self.loadButton.setObjectName("loadButton")
        self.loadButton.clicked.connect(self.openFileNamesDialog)
        self.horizontalLayout_2.addWidget(self.loadButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.playSongButton = QtWidgets.QPushButton(self.widget)
        self.playSongButton.setObjectName("playSongButton")
        self.playSongButton.clicked.connect(self.playSong)
        self.horizontalLayout_3.addWidget(self.playSongButton)
        self.pauseSongButton = QtWidgets.QPushButton(self.widget)
        self.pauseSongButton.setObjectName("pauseSongButton")
        self.pauseSongButton.clicked.connect(self.pauseSong)
        self.horizontalLayout_3.addWidget(self.pauseSongButton)
        self.stopSongButton = QtWidgets.QPushButton(self.widget)
        self.stopSongButton.setObjectName("stopSongButton")
        self.stopSongButton.clicked.connect(self.stopSong)
        self.horizontalLayout_3.addWidget(self.stopSongButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 432, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadButton.setText(_translate("MainWindow", "Load File(s)..."))
        self.playSongButton.setText(_translate("MainWindow", "Play"))
        self.pauseSongButton.setText(_translate("MainWindow", "Pause"))
        self.stopSongButton.setText(_translate("MainWindow", "Stop"))
        
    def openFileNamesDialog(self): 
        fileNames , _ = QtWidgets.QFileDialog.getOpenFileNames(None, 'Open File', os.getenv('HOME'))
        if fileNames:
            print(fileNames)    
            self.files = fileNames
#            Just keep file names not path
            for i in range(0,len(fileNames)):
                x = fileNames[i].split('/')
                print(x)
                self.songListWidget.addItems(x[-1:])
            
    def playSong(self):
        if self.songListWidget.currentItem():
            media = instance.media_new(self.songListWidget.currentItem().text())
            player.set_media(media)
            player.play()
            sc = MyStaticMplCanvas(self.widget, width=5, height=4, dpi=100)
            self.verticalLayout.addWidget(sc)
#            y, sr = librosa.load(librosa.util.example_audio_file(), duration=10)
#            x = plt.figure()
#            plt.subplot(3, 1, 1)
#            librosa.display.waveplot(y, sr=sr)
#            plt.title('Monophonic')
            self.verticalLayout.addWidget(sc)
            
    def pauseSong(self):
        if self.songListWidget.currentItem():
            player.pause()
            
    def stopSong(self):
        if self.songListWidget.currentItem():
            player.stop()
            
class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)

        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass
    
class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""
    def compute_initial_figure(self):
        y, sr = librosa.load(librosa.util.example_audio_file(), duration=10)
        x = plt.figure()
        plt.subplot(3, 1, 1)
        librosa.display.waveplot(y, sr=sr)
        plt.title('Monophonic')
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        
            
#VLC Player conf.          
instance = vlc.Instance()
player = instance.media_player_new()
global files
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())