#!/usr/bin/env python

import sys
#import os
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication

class GUI (QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = 'Sofia'
        self.left = 10
        self.top = 20
        self.width = 500
        self.height = 500
        
        self.initUI()
    
    def initUI(self):
        """User interface."""
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # Main widget
        wid = QWidget()
        self.setCentralWidget(wid)
        
        # Main Layout
        mainLayout = QVBoxLayout() 
        # QV = vertical box
        
        # Self plot panel
        self.panel = QWidget()
        layout = QVBoxLayout(self.panel)
        
        layout.addWidget(self.panel)
        
        #add panel to main layout
        mainLayout.addWidget(self.panel)
        wid.setLayout(mainLayout)
        self.show()
    
def main():
    app = QApplication(sys.argv)
    # gui = GUI()
    
    sys.exit(app.exec_())
    