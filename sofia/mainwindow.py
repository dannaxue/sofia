#!/usr/bin/env python
import sys
# import numpy as np

#import os
from PyQt5.QtWidgets import QMainWindow, QApplication

#from matplotlib.backends.backend_qt5agg import FigureCanvas
#from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
#from matplotlib.figure import Figure
# from matplotlib import cm
# from matplotlib import pyplot as plt
#from astropy.wcs import WCS
#from astropy.utils.data import download_file
#from astropy.io import fits
# from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
#changes

#specify the library (sofia.plots)
from sofia.plots import GLUE

class GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Sofia'
        self.left = 10
        self.top = 20
        self.width = 500
        self.height = 500
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #wid = QWidget()
        plot = GLUE()
        self.setCentralWidget(plot)
        #mainLayout = QVBoxLayout()
        #plt.setLayout(mainLayout)       
        self.show()

def main():
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    #plt = PLOTTER()
    #plt.show()
    screen_resolution = app.desktop().screenGeometry()
    width = screen_resolution.width()
    gui.setGeometry(width * 0.025, 0, width * 0.95, width * 0.45)
    sys.exit(app.exec_())