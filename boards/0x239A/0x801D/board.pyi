from __future__ import annotations
import busio
import microcontroller
"""
board Adafruit Industries LLC Gemma M0
https://circuitpython.org/boards/gemma_m0
"""
A1: microcontroller.Pin = ...
D2: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
A2: microcontroller.Pin = ...
D0: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
A0: microcontroller.Pin = ...
D1: microcontroller.Pin = ...
LED: microcontroller.Pin = ...
L: microcontroller.Pin = ...
D13: microcontroller.Pin = ...
APA102_MOSI: microcontroller.Pin = ...
DOTSTAR_DATA: microcontroller.Pin = ...
APA102_SCK: microcontroller.Pin = ...
DOTSTAR_CLOCK: microcontroller.Pin = ...
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

