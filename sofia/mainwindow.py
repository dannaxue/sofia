#!/usr/bin/env python
import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QPushButton, QFileDialog, QInputDialog
from PyQt5.QtGui import QIcon
from sofia.plots import PLOT_UI

class GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Sofia'
        self.left = 10
        self.top = 20
        self.width = 500
        self.height = 500
        self.path0, file0 = os.path.split(__file__)
        
        # Style
        
        with open(self.path0 + '/stylesheet.css', "r") as fh:
            self.setStyleSheet(fh.read())
        
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
        
        quitter = QAction(QIcon(self.path0 + '/icons/doggo.png'), 'Quit', self)
        quitter.setShortcut('Ctrl+Q')
        quitter.setStatusTip('Import an image for analysis')
        quitter.triggered.connect(self.close)
        
        openFile = QAction(QIcon('open.png'), 'Open File', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Options')
        fileMenu.addAction(openFile)   
        fileMenu.addAction(quitter)
        self.toolbar = self.addToolBar('Toolbar')
        self.toolbar.addAction(importImage)
        self.setCentralWidget(self.plot)
        self.show()
        
    def imageUploadEvent(self, importImage):

        filename, ok = QInputDialog.getText(self, 'Image Upload', 'Enter image file name:')
        self.plot.plot1.filename = filename
        self.plot.plot2.filename = filename
        
    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

def main():
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    screen_resolution = app.desktop().screenGeometry()
    width = screen_resolution.width()
    gui.setGeometry(width * 0.025, 0, width * 0.95, width * 0.45)
    sys.exit(app.exec_())