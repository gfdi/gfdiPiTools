#!/usr/bin/env python
# recordWeather.py
#
# Record the current weather conditions.

import sys
from optparse import OptionParser
sys.path.append('../customLibraries')
import WeatherStation

# Use OptionParser to grab command-line options.
parser = OptionParser()
parser.add_option('-f', '--file', dest='dataFile', help='Write weather data to CSVFILE.', metavar='CSVFILE')
(options, args) = parser.parse_args()

# Supply a default filename, if necessary.
if None == options.dataFile:
  dataFile = '../data/weatherData.csv'
else:
  dataFile = options.dataFile

# Create a WeatherStation object.
ws = WeatherStation.WeatherStation(dataFile=dataFile)

# Get down to business.
ws.fetchData()
ws.recordData()
ws.printData()
