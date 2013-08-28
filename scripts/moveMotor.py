#!/usr/bin/env python
# moveMotor.py
#
# Adjust the height of our camera by moving a motor a specified number of
# steps.

import serial
import sys
from time import sleep

# Check arguments.
if 2 != len(sys.argv):
  print "Usage:\n  moveMotorOnce.py <number>"
  exit(1)

# Grab the first argument.  (Not argv[0], that's the command name.)
arg1 = str(sys.argv[1])


# Create object representing serial connection to Arduino.
ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

# Reinitialize the connection, just in case there's something in the buffer.
ser.close()
ser.open()


try:
  # Issue the command to the Arduino.
  ser.write(arg1)

  # Wait for, then grab, the response from the Arduino.
  response = ''
  while response == '':
    response = ser.read(1024)
    sleep(.1)

  # Report the response.
  print response

  # Clean up and get out.
  ser.close()
  sys.exit(0)

except (KeyboardInterrupt, SystemExit):
  # By handling these exceptions, we get to slip in clean-up operations before
  # the program exits.
  ser.close()

