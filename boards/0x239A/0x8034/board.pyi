from __future__ import annotations
import busio
import displayio
import microcontroller
import typing
"""
board Adafruit Industries LLC PyBadge
https://circuitpython.org/boards/pybadge
"""
TFT_CS: microcontroller.Pin = ...
TFT_DC: microcontroller.Pin = ...
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


def UART() -> busio.UART:
    """Returns the `busio.UART` object for the board's designated UART bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.UART`.
    """
    ...

