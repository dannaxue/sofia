#!/usr/bin/env python

import sys
import numpy as np

#import os
from PyQt5.QtWidgets import QDialog, QMainWindow, QWidget, QVBoxLayout, QApplication, QPushButton

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib import cm
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

import random
# from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
#changes

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
        plt = PLOT_UI()
        self.setCentralWidget(plt)
        #mainLayout = QVBoxLayout()
        #plt.setLayout(mainLayout)        
        self.show()
        
class PLOT_UI(QWidget):
    
    def __init__(self):
        super(PLOT_UI, self).__init__()
        self.figure = Figure()
        self.initUI()

    def initUI(self):
        """User interface."""
        
        # Creates a Canvas and Navigation Toolbar
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        # Creates a button
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)
        
        # Sets up layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        self.toolbar.move('Bottom')
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)
    
    # Plots data
    def plot(self):
        data = [random.random() for i in range(10)]
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.plot(data, '*-')
        self.canvas.draw()

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