#!/usr/bin/env python
# checkWeather.py
#
# Print current weather conditions.

import sys
sys.path.append('../customLibraries')
import WeatherStation

# Check arguments.
if 1 != len(sys.argv):
  print "Usage:\n  checkWeather.py"
  exit(1)

# Create a WeatherStation object.
ws = WeatherStation.WeatherStation("/home/pi/data/weatherData.csv")

# Get down to business.
ws.fetchData()
ws.printData()
