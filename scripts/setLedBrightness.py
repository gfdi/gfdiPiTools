#!/usr/bin/env python
# setLedBrightness.py
#
# Set the brightness level of our LED.

import sys
from pyblinkm import BlinkM, Scripts
# Our in-house toolkit.
sys.path.append('../customLibraries')
import GFDITools

usageLine = "Usage:\n  ledControl.py <0-255>"
# Check arguments.
if 2 != len(sys.argv):
  print usageLine
  exit(1)

# Grab the first argument.  (Not argv[0], that's the command name.)
arg1 = int(sys.argv[1])

# range() is a little unintuitive, to me.  range(0, 256) excludes 256, meaning
# it includes numbers 0 - 255, inclusive.
if not arg1 in range(0, 256):
  print usageLine
  exit(1)

# Get the i2c bus number, then create a blinkm object with that bus number.
bus = GFDITools.guessBus()
blinkm = BlinkM(bus=bus)

# Issue the command to the I2C
blinkm.reset()
blinkm.go_to(arg1, arg1, arg1)

sys.exit(0)


# BlinkM makes some scripts available, which flash the lights in various
# patterns.  They're included here in commented form.  Copy lines as needed, or
# uncomment the whole block if you want to throw a rave.

'''
raw_input("Press Enter to continue...")
print "STARTUP\n"
blinkm.play_script(Scripts.STARTUP)

raw_input("Press Enter to continue...")
print 'RGB\n'
blinkm.play_script(Scripts.RGB)

raw_input("Press Enter to continue...")
print 'WHITE_FLASH\n'
blinkm.play_script(Scripts.WHITE_FLASH)

raw_input("Press Enter to continue...")
print 'GREEN_FLASH\n'
blinkm.play_script(Scripts.GREEN_FLASH)

raw_input("Press Enter to continue...")
print 'BLUE_FLASH\n'
blinkm.play_script(Scripts.BLUE_FLASH)

raw_input("Press Enter to continue...")
print 'CYAN_FLASH\n'
blinkm.play_script(Scripts.CYAN_FLASH)

raw_input("Press Enter to continue...")
print 'MAGENTA_FLASH\n'
blinkm.play_script(Scripts.MAGENTA_FLASH)

raw_input("Press Enter to continue...")
print 'YELLOW_FLASH\n'
blinkm.play_script(Scripts.YELLOW_FLASH)

raw_input("Press Enter to continue...")
print 'BLACK\n'
blinkm.play_script(Scripts.BLACK)

raw_input("Press Enter to continue...")
print 'HUE_CYCLE\n'
blinkm.play_script(Scripts.HUE_CYCLE)

raw_input("Press Enter to continue...")
print 'MOOD_LIGHT\n'
blinkm.play_script(Scripts.MOOD_LIGHT)

raw_input("Press Enter to continue...")
print 'VIRTUAL_CANDLE\n'
blinkm.play_script(Scripts.VIRTUAL_CANDLE)

raw_input("Press Enter to continue...")
print 'WATER_REFLECTIONS\n'
blinkm.play_script(Scripts.WATER_REFLECTIONS)

raw_input("Press Enter to continue...")
print 'OLD_NEON\n'
blinkm.play_script(Scripts.OLD_NEON)

raw_input("Press Enter to continue...")
print 'THE_SEASONS\n'
blinkm.play_script(Scripts.THE_SEASONS)

raw_input("Press Enter to continue...")
print 'THUNDERSTORM\n'
blinkm.play_script(Scripts.THUNDERSTORM)

raw_input("Press Enter to continue...")
print 'STOP_LIGHT\n'
blinkm.play_script(Scripts.STOP_LIGHT)

raw_input("Press Enter to continue...")
print 'MORSE_CODE\n'
blinkm.play_script(Scripts.MORSE_CODE)

'''
