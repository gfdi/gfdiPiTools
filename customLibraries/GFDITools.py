#!/usr/bin/env python

# Return the guessed number of the 
def guessBus():
  f = open('/proc/cpuinfo', 'r')

  for line in f:
    if line.startswith('Revision'):
      if int(line.rstrip()[-1], 16) in [2, 3]:
        # If there's a line starting with "Revision" and ending with '2' or
        # '3', consider this an older rev. 1 Pi, with i2c bus address 0.
        return 0
      else:
        # If it's anything else, consider it a newer rev. 2 Pi, with i2c bus
        # address 1.
        return 1
