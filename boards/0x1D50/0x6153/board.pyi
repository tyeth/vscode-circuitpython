from __future__ import annotations
import busio
import microcontroller
"""
board JPConstantineau PyKey60
https://circuitpython.org/boards/jpconstantineau_pykey60
"""
COL1: microcontroller.Pin = ...
COL2: microcontroller.Pin = ...
COL3: microcontroller.Pin = ...
COL4: microcontroller.Pin = ...
COL5: microcontroller.Pin = ...
COL6: microcontroller.Pin = ...
COL7: microcontroller.Pin = ...
COL8: microcontroller.Pin = ...
COL9: microcontroller.Pin = ...
COL10: microcontroller.Pin = ...
COL11: microcontroller.Pin = ...
COL12: microcontroller.Pin = ...
COL13: microcontroller.Pin = ...
COL14: microcontroller.Pin = ...
ROW1: microcontroller.Pin = ...
ROW2: microcontroller.Pin = ...
ROW3: microcontroller.Pin = ...
ROW4: microcontroller.Pin = ...
ROW5: microcontroller.Pin = ...
SPEAKER: microcontroller.Pin = ...
LED: microcontroller.Pin = ...
NEOPIXEL: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
def I2C() -> busio.I2C:
    """Returns the `busio.I2C` object for the board's designated I2C bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.I2C`.
    """
    ...


def SPI() -> busio.SPI:
    """Returns the `busio.SPI` object for the board's designated SPI bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.SPI`.
    """
    ...


