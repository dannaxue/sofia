#!/usr/bin/env python
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QInputDialog, QToolButton
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
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        plot = PLOT_UI()
        #build toolbar
        importImage = QAction(QIcon('doggo.png'), 'Import', self)
        importImage.setShortcut('Ctrl+I')
        importImage.setStatusTip('Import an image for analysis')
        importImage.triggered.connect(self.imageUploadEvent)
        
        self.toolbar = self.addToolBar('Toolbar')
        self.toolbar.addAction(importImage)
        self.setCentralWidget(plot)
        self.show()
        
    def imageUploadEvent(self, importImage):
        filename, ok = QInputDialog.getText(self, 'Image Upload', 'Enter image file name:')

def main():
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    screen_resolution = app.desktop().screenGeometry()
    width = screen_resolution.width()
    gui.setGeometry(width * 0.025, 0, width * 0.95, width * 0.45)
    sys.exit(app.exec_())