#!/usr/bin/env python
import os
import csv
import sys
import time
import datetime
import smbus
from smbus import SMBus

# We want a library in a non-standard location.  First, let's add that location
# to the path, so we can use it.
sys.path.append('../thirdPartyLibraries')
# Now let's import that library.
from Adafruit_BMP085 import BMP085

# Our custom in-house library, also in a non-standard location.
sys.path.append('../customLibraries')
import GFDITools


class WeatherStation:
  def __init__(self, dataFile='/dev/null'):
    self.dataFile = dataFile
    self.fetched = False

    # Initialise the BMP085 and use STANDARD mode (default value)
    # self.bmp = BMP085(0x77, debug=True)
    self.bmp = BMP085(0x77)
    
    # To specify a different operating mode, uncomment one of the following:
    # self.bmp = BMP085(0x77, 0)  # ULTRALOWPOWER Mode
    # self.bmp = BMP085(0x77, 1)  # STANDARD Mode
    # self.bmp = BMP085(0x77, 2)  # HIRES Mode
    # self.bmp = BMP085(0x77, 3)  # ULTRAHIRES Mode

    # Initilize HIH-6130.
    bus = GFDITools.guessBus()
    self.HIH6130 = SMBus(bus=bus)

    # Temporary storage array for HIH6130 data
    self.blockData = [0, 0, 0, 0]


  def fetchData(self):
    # Fetch temp & pressure data from BMP
    self.temp = self.bmp.readTemperature()
    self.pressure = self.bmp.readPressure() / 100.0
    # Altitude seems buggy, so we're skipping it for now.
    # altitude = self.bmp.readAltitude()

    # Tell HIH-6130 we want temperature and humidity data.
    self.HIH6130.write_quick(0x27)
    # Wait for it.
    time.sleep(0.050)
    # Read the data we requested.
    blockData = self.HIH6130.read_i2c_block_data(0x27, 0)
    # Process the data.
    self.status = (blockData[0] & 0xc0) >> 6
    self.humidity = (((blockData[0] & 0x3f) << 8) + blockData[1]) * 100.0 / 16383.0
    self.tempC = ((blockData[2] << 6) + ((blockData[3] & 0xfc) >> 2)) * 165.0 / 16383.0 - 40.0
    # tempF = tempC*9.0/5.0 + 32.0

    # Make a note that there is now data to be had.
    self.fetched = True


  def printData(self):
    # print data to screen
    # print "Data:       ", "%02x "*len(d)%tuple(d)
    # print "Status:     ", status
    if self.fetched:
      print "Humidity:   %.2f" % self.humidity, "%RH"
      print "Temperature:    %.2f C" % self.tempC
      print "Barometric Pressure:    %.2f hPa" % self.pressure
      print "Temperature:    %.2f C" % self.temp
    else:
      print "No data has been fetched."
      return -1


  def recordData(self):
    if self.fetched:
      if not os.path.exists(self.dataFile):
        with open(self.dataFile, 'w') as csvfile:
          datawriter = csv.writer(
            csvfile,
            quotechar=',',
            quoting=csv.QUOTE_MINIMAL
          )
          datawriter.writerow([
            'Date',
            'Temp(C)',
            'Pressure(hPa)',
            'Humidity(%RH)'
          ])

      with open(self.dataFile, 'a+') as csvfile:
        datawriter = csv.writer(csvfile, quotechar=',', quoting=csv.QUOTE_MINIMAL)
        datawriter.writerow([datetime.datetime.now(), self.tempC, self.pressure, self.humidity])
    else:
      print "No data has been fetched."
      return -1

