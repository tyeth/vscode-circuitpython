from __future__ import annotations
import busio
import microcontroller
import typing
"""
board Adafruit Industries LLC QT Py M0 Haxpress
https://circuitpython.org/boards/qtpy_m0_haxpress
"""
D0: microcontroller.Pin = ...
A0: microcontroller.Pin = ...
D1: microcontroller.Pin = ...
A1: microcontroller.Pin = ...
D2: microcontroller.Pin = ...
A2: microcontroller.Pin = ...
D3: microcontroller.Pin = ...
A3: microcontroller.Pin = ...
D4: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
D5: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
D6: microcontroller.Pin = ...
A6: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
D7: microcontroller.Pin = ...
A7: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
D8: microcontroller.Pin = ...
A8: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
D9: microcontroller.Pin = ...
A9: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
D10: microcontroller.Pin = ...
A10: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
NEOPIXEL: microcontroller.Pin = ...
NEOPIXEL_POWER: microcontroller.Pin = ...
STEMMA_I2C: typing.Any = ...
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

