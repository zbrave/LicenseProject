import os
import vlc
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib.collections import PolyCollection
import librosa
import matplotlib
import Functions.knn as knn
import Functions.getFeatures as Features
import numpy as np
from librosa import display
from librosa import core
from librosa import util
from librosa.util.exceptions import ParameterError
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QVBoxLayout, QSizePolicy, QTableWidgetItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import pyqtSlot

class Ui_MainWindow(object):
    files = []
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(493, 658)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.songListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.songListWidget.setObjectName("songListWidget")
        self.horizontalLayout_1.addWidget(self.songListWidget)
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setObjectName("loadButton")
        self.horizontalLayout_1.addWidget(self.loadButton)
        self.verticalLayout.addLayout(self.horizontalLayout_1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.playSongButton = QtWidgets.QPushButton(self.centralwidget)
        self.playSongButton.setObjectName("playSongButton")
        self.horizontalLayout_2.addWidget(self.playSongButton)
        self.pauseSongButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseSongButton.setObjectName("pauseSongButton")
        self.horizontalLayout_2.addWidget(self.pauseSongButton)
        self.stopSongButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopSongButton.setObjectName("stopSongButton")
        self.horizontalLayout_2.addWidget(self.stopSongButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
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
#        self.tabLayout1.addWidget(self.tabLayout1Label, 0, 0, 1, 1)
#        self.tablLayout1TableWidget = QtWidgets.QTableWidget(self.tab)
#        self.tablLayout1TableWidget.setGridStyle(QtCore.Qt.SolidLine)
#        self.tablLayout1TableWidget.setObjectName("tablLayout1TableWidget")
#        self.tablLayout1TableWidget.setColumnCount(0)
#        self.tablLayout1TableWidget.setRowCount(0)
#        self.tabLayout1.addWidget(self.tablLayout1TableWidget, 1, 0, 1, 1)
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
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 493, 21))
        self.menubar.setObjectName("menubar")
        self.fileOpMenu = QtWidgets.QMenu(self.menubar)
        self.fileOpMenu.setObjectName("fileOpMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Data_Import = QtWidgets.QAction(MainWindow)
        self.actionNew_Data_Import.setObjectName("actionNew_Data_Import")
        self.fileOpMenu.addAction(self.actionNew_Data_Import)
        self.menubar.addAction(self.fileOpMenu.menuAction())
        
        self.stopSongButton.clicked.connect(self.stopSong)
        self.pauseSongButton.clicked.connect(self.pauseSong)
        self.playSongButton.clicked.connect(self.playSong)
        self.loadButton.clicked.connect(self.openFileNamesDialog)
        self.actionNew_Data_Import.triggered.connect(self.newDataImp)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadButton.setText(_translate("MainWindow", "Load File(s)..."))
        self.playSongButton.setText(_translate("MainWindow", "Play"))
        self.pauseSongButton.setText(_translate("MainWindow", "Pause"))
        self.stopSongButton.setText(_translate("MainWindow", "Stop"))
        self.fileOpMenu.setTitle(_translate("MainWindow", "File operations"))
        self.actionNew_Data_Import.setText(_translate("MainWindow", "New Data Import .."))
        
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
        return files, names
    
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
            
            result, veriler = self.connectDB()
            self.showFeatureOnNewTab(result, veriler)
#            # Adds new tab
#            self.tab_3 = QtWidgets.QWidget()
#            self.tab_3.setObjectName("tab_3")
#            self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
#            self.tabWidget.addTab(self.tab_3, "")
            
    def connectDB(self):
        import sqlite3
        vt = sqlite3.connect(r'C:\Users\merta\Desktop\Dersler\bitirme\LicenseProject\GUI\Functions\DB\DB.db')
        print ('Opened database successfully')
        conn=vt.cursor()
        
        conn.execute("SELECT * FROM Feature")
        
        veriler = conn.fetchall()
        
        trainData=[]
        
        for x in veriler:
            trainData.append(x[2:])
            
        testData=Features.features(self.files[self.songListWidget.currentRow()])
        #testData= trainData[0]
        
        result=knn.knn(trainData,testData,2,36)
        names=[]
        for i in result:
            print(veriler[i][1],i)
            names.append(veriler[i][1])        
        conn.close() 
        return result,veriler

        
    def showFeatureOnNewTab(self, result, veriler):
       # Adds new tab
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.tabWidget.addTab(self.tab, self.files[self.songListWidget.currentRow()].split('/')[-1:][0])
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
        for x in result:
            for j in range(36):
                item = QTableWidgetItem(str(veriler[x][j+1]))
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

    def __init__(self, parent=None, width=5, height=4, dpi=100, index=2):
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
        y, sr = librosa.load(index, duration=10)
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
