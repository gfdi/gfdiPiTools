gfdiPiTools
==========

These are scripts and modules for controlling a Raspberry Pi and various
peripheral hardware.


moveMotor.py
------------

This script controls the motor which raises and lowers the camera on our
optical altimetry prototype.

*moveMotor.py &lt;num&gt;*

*num* must be a number, but the range allowed depends on the current position
of the camera.  Once the command completes, it should tell you the current
position of the camera.


setLedBrightness.py
-------------------

*setLedBrightness.py &lt;num&gt;*

This script could be easily extended to manipulate the RGB values of our
"white" LED, allowing easily enough control and almost enough brightness for a
dance party.  We're just interested in the brightness level, though, so it sets
the same value, specified on the command line, for red, green, and blue.

Only values from 0-255 are valid for *num*.

Dependencies include the pyblinkm library and our in-house library, GFDITools.


checkWeather.py
---------------

*checkWeather.py*

This just prints current weather conditions, gathered from environmental
sensors.


recordWeather.py

*recordWeather.py [(-f | --file) &lt;CSVFILE&gt;]*

This script is just like checkWeather.py, except it records the conditions in a
CSV file.  If CSVFILE is not specified, it will write to a default location.
