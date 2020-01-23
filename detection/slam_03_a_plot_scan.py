# Plot a scan of the robot using matplotlib.
# 03_a_plot_scan
# Claus Brenner, 09 NOV 2012
from pylab import *
from matplotlib import *;
from lego_robot import *
import matplotlib.pyplot as plt

# Read the logfile which contains all scans.
logfile = LegoLogfile()
logfile.read("robot4_scan.txt")

# Plot one scan.
plt.plot(logfile.scan_data[8])
plt.show()
