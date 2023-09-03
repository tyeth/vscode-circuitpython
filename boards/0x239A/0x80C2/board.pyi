from __future__ import annotations
import busio
import microcontroller
"""
board bleeptrack PicoPlanet
https://circuitpython.org/boards/picoplanet
"""
A1: microcontroller.Pin = ...
A0: microcontroller.Pin = ...
A2: microcontroller.Pin = ...
D5: microcontroller.Pin = ...
GREEN_LED: microcontroller.Pin = ...
D6: microcontroller.Pin = ...
RED_LED: microcontroller.Pin = ...
LED: microcontroller.Pin = ...
D7: microcontroller.Pin = ...
BLUE_LED: microcontroller.Pin = ...
D1: microcontroller.Pin = ...
A3: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
D2: microcontroller.Pin = ...
A4: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
D3: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
D4: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
D8: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
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


