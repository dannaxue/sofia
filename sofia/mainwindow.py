#!/usr/bin/env python
import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog, QDialog, QInputDialog, QMessageBox
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
        
        # import image function
        importImage = QAction(QIcon(self.path0 + '/icons/img.png'), 'Import', self)
        importImage.setShortcut('Ctrl+I')
        importImage.setStatusTip('Import an image for analysis')
        importImage.triggered.connect(self.imageUploadEvent)
        
        # quit function
        quitter = QAction(QIcon(self.path0 + '/icons/cancel.png'), 'Quit', self)
        quitter.setShortcut('Ctrl+Q')
        quitter.setStatusTip('Quit')
        quitter.triggered.connect(self.close)
        
        # open file function
        openFile = QAction(QIcon(self.path0 + '/icons/openfile.png'), 'File', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)
        
        # save file function
        saveFile = QAction(QIcon(self.path0 + '/icons/saver.png'), '&Save File', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)

        # make a menubar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&Options')
        
        # add actions to menubar
        fileMenu.addAction(openFile)   
        fileMenu.addAction(quitter)
        fileMenu.addAction(saveFile)
 
        importMenu = menubar.addMenu('Import')
        importMenu.addAction(importImage)
        
        # make toolbar
        self.toolbar = self.addToolBar('Toolbar')
        
        # add functions to toolbar
        self.toolbar.addAction(saveFile)
        self.toolbar.addAction(quitter)
        self.toolbar.addAction(importImage)
        self.toolbar.addAction(openFile)
        
        # make plot the central Widget
        self.setCentralWidget(self.plot)
        self.show()

    # To-do: Fix file function
    def file_save(self):
        name, _ = QFileDialog.getSaveFileName(self, 'Save File', options=QFileDialog.DontUseNativeDialog)
        file = open(name, 'w')
        text = file.read()
        file.write(text)
        file.close()
        
    # Gets image URL, passes to plots
    def imageUploadEvent(self, importImage):
        filename, ok = QInputDialog.getText(self, 'Image Upload', 'Enter image file URL:')
        
        self.plot.plot1.filename = filename
        self.plot.plot2.filename = filename
        
    # Makes Directory pop up, to help with searching for an image file
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