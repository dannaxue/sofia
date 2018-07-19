from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from astropy.wcs import WCS
from astropy.utils.data import download_file
from astropy.io import fits

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