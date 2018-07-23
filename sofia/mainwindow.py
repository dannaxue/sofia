#!/usr/bin/env python
import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QInputDialog
from PyQt5.QtGui import QIcon
from sofia.plots import PLOT_UI, IMAGE_PLOT, CONTOUR_PLOT

class GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Sofia'
        self.left = 10
        self.top = 20
        self.width = 500
        self.height = 500
        self.path0, file0 = os.path.split(__file__)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.plot = PLOT_UI()
        #build toolbar
        importImage = QAction(QIcon(self.path0 + '/icons/doggo.png'), 'Import', self)
        importImage.setShortcut('Ctrl+I')
        importImage.setStatusTip('Import an image for analysis')
        importImage.triggered.connect(self.imageUploadEvent)
        
        self.toolbar = self.addToolBar('Toolbar')
        self.toolbar.addAction(importImage)
        self.setCentralWidget(self.plot)
        self.show()
        
    def imageUploadEvent(self, importImage):
        filename, ok = QInputDialog.getText(self, 'Image Upload', 'Enter image file name:')
        self.plot.plot1.filename = filename
        self.plot.plot2.filename = filename

def main():
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    screen_resolution = app.desktop().screenGeometry()
    width = screen_resolution.width()
    gui.setGeometry(width * 0.025, 0, width * 0.95, width * 0.45)
    sys.exit(app.exec_())