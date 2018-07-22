from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from astropy.wcs import WCS
from astropy.utils.data import download_file
from astropy.io import fits
from astroquery.skyview import SkyView
import numpy as np

class PLOT_UI(QWidget):
    
    def __init__(self):
        super(PLOT_UI, self).__init__()
        self.figure = Figure()
        self.initUI()

    def initUI(self):
        """User interface."""
        
        layout = QHBoxLayout()
        plot1 = IMAGE_PLOT()
        plot2 = CONTOUR_PLOT()
        layout.addWidget(plot1)
        layout.addWidget(plot2)
        self.setLayout(layout)

class IMAGE_PLOT(QWidget):

    
    def __init__(self):
        super(IMAGE_PLOT, self).__init__()
        self.figure = Figure()
        self.initUI()

    def initUI(self):
        """User interface."""
        
        # Creates a Canvas and Navigation Toolbar
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Creates a button1
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)
        
        # Sets up layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.button)
        self.setLayout(layout)
    
    # Plots data
    def plot(self):
        image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True)
        # memmap tells code not to remember these handles after.
        hdulist = fits.open(image_file, memmap=False)
        header = hdulist['PRIMARY'].header
        data = hdulist['PRIMARY'].data
        hdulist.close()
        wcs = WCS(header)
        ax = self.figure.add_axes([0.1, 0.1, 0.8, 0.8], projection = wcs)
        ax.set_xlabel('RA')
        ax.set_ylabel('Dec')
        ax.imshow(data, cmap = 'gist_heat', origin = 'lower')
        ra = ax.coords[0]
        ra.set_major_formatter('hh:mm:ss')
        dec = ax.coords[1]
        dec.set_major_formatter('dd:mm:ss');
        self.canvas.draw()
        
class CONTOUR_PLOT(QWidget):

    
    def __init__(self):
        super(CONTOUR_PLOT, self).__init__()
        self.figure = Figure()
        self.initUI()

    def initUI(self):
        """User interface."""
        
        # Creates a Canvas and Navigation Toolbar
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Creates a button1
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)
        
        # Sets up layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.button)
        self.setLayout(layout)
    
    # Plots data
    def plot(self):
        sv = SkyView()
        paths = sv.get_images(position='M 82', survey = ['WISE 12', 'GALEX Near UV'])
        wcs1 = WCS(paths[0][0].header)
        wcs2 = WCS(paths[1][0].header)
        ax = self.figure.add_axes([0.1, 0.1, 0.8, 0.8], projection = wcs1)
        ax.imshow(paths[0][0].data, origin = 'lower', cmap = 'gist_heat_r')
        ima2 = paths[1][0].data
        levels = np.nanmin(ima2) + [0.02, 0.09, 0.2]
        ax.contour(ima2, levels, transform = ax.get_transform(wcs2), colors='r')
        ax.set_xlabel('RA')
        ax.set_ylabel('Dec')
        self.canvas.draw()


#Start plotting data here, within the framework already given by PLOT_UI and CONTOUR_PLOT
# class PLOTTING():
    
    # def __init__(self):
        # super(PLOTTING, self).__init__()
        # self.initGraph()
    
    # def initGraph(self):
        # here I will set up the functions to initialize the actual image plotting/graphing
        # read in the filename, and get the variable for the filename/image address
        # everytime imageUpload is called
        
        # Steps:
        # 1. Clear plot
        # 2. Read in filename
        # 3. Get data, label axes, perform designated functions
        # 4. self.canvas.draw()
        # 5. Remember to do one for plot 1 and one for plot 2
        
        # Learn how to be able to access the graphs defined in earlier functions
    