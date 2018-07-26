import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT 
# as NavigationToolbar
from matplotlib.figure import Figure
from sofia.plotter import plotImage, plotContour
from PyQt5.QtWidgets import QSplitter
from PyQt5.QtCore import Qt

class PLOT_UI(QWidget):
    
    def __init__(self):
        super().__init__()
        # get rid of the 
        self.figure = Figure()
        self.initUI()

    def initUI(self):
        """User interface."""
        
        layout = QHBoxLayout()
        self.plot1 = IMAGE_PLOT()
        self.plot2 = CONTOUR_PLOT()
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.plot1)
        splitter.addWidget(self.plot2)
        splitter.setStretchFactor(1, 1)
        layout.addWidget(splitter)
        self.setLayout(layout)

class IMAGE_PLOT(QWidget):

    
    def __init__(self):
        super().__init__()
        self.figure = Figure()
        self.initUI()

    def initUI(self):
        """User interface."""
        
        # Creates a Canvas and Navigation Toolbar
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Creates a button1
        # self.button = QPushButton('Plot')
        # self.button.clicked.connect(self.plot)
        
        # Sets up layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        # layout.addWidget(self.button)
        self.setLayout(layout)
    
    # Plots data
    def plot(self):
        plotImage(self)
        # image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True)
        # memmap tells code not to remember these handles after
        # define return object of class
        
class CONTOUR_PLOT(QWidget):
    
    def __init__(self):
        super().__init__()
        self.figure = Figure()
        self.initUI()

    def initUI(self):
        """User interface."""
        
        # Creates a Canvas and Navigation Toolbar
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        # Sets up layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        # layout.addWidget(self.button)
        self.setLayout(layout)
    
    # Plots data
    def plot(self):
        plotContour(self)
        
class NavigationToolbar(NavigationToolbar2QT):
    def __init__(self,canvas,parent):
        # Select only a few buttons
        self.iconDir = os.path.join(os.path.dirname(os.path.abspath(__file__)),"icons")
        self.toolitems = [
            ('Home','Go back to original limits','home','home'),
            ('Pan','Pan figure','move','pan'),
            ('Zoom','Zoom in','zoom_to_rect','zoom'),
            ('Save', 'Save the figure', 'filesave', 'save_figure'),
            # ('Plot', 'plot', 'plot', 'plot'),
        ]
        self.parent = parent
        super().__init__(canvas,parent)
        self.addAction(self._icon('plot.png'), 'Plot', self.parent.plot)
