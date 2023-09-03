from __future__ import annotations
import busio
import microcontroller
import typing
"""
board Adafruit Metro M7 iMX RT1011 SD
https://circuitpython.org/boards/adafruit_metro_m7_1011_sd
"""
STEMMA_I2C: typing.Any = ...
I2S_WORD_SELECT: microcontroller.Pin = ...
I2S_BIT_CLOCK: microcontroller.Pin = ...
I2S_DATA: microcontroller.Pin = ...
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

