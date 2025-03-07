from __future__ import annotations
import busio
import microcontroller
"""
board crcibernetica-ideaboard
https://circuitpython.org/boards/crcibernetica-ideaboard
"""
IO0: microcontroller.Pin = ...
IO1: microcontroller.Pin = ...
IO2: microcontroller.Pin = ...
NEOPIXEL: microcontroller.Pin = ...
IO3: microcontroller.Pin = ...
IO4: microcontroller.Pin = ...
IO5: microcontroller.Pin = ...
IO6: microcontroller.Pin = ...
IO7: microcontroller.Pin = ...
IO8: microcontroller.Pin = ...
IO9: microcontroller.Pin = ...
IO10: microcontroller.Pin = ...
IO11: microcontroller.Pin = ...
IO12: microcontroller.Pin = ...
IO13: microcontroller.Pin = ...
IO14: microcontroller.Pin = ...
IO15: microcontroller.Pin = ...
IO16: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
IO17: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
IO18: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
IO19: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
IO20: microcontroller.Pin = ...
IO21: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
IO22: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
IO23: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
IO25: microcontroller.Pin = ...
IO26: microcontroller.Pin = ...
IO27: microcontroller.Pin = ...
IO32: microcontroller.Pin = ...
IO33: microcontroller.Pin = ...
IO34: microcontroller.Pin = ...
IO35: microcontroller.Pin = ...
IO36: microcontroller.Pin = ...
IO39: microcontroller.Pin = ...
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


