from __future__ import annotations
import busio
import displayio
import typing
"""
board Adafruit Industries LLC PyPortal Titano
https://circuitpython.org/boards/pyportal_titano
"""
STEMMA_I2C: typing.Any = ...
DISPLAY: displayio.Display = ...
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


