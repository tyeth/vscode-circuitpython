from __future__ import annotations
import busio
import microcontroller
import typing
"""
board adafruit_qtpy_esp32c3
https://circuitpython.org/boards/adafruit_qtpy_esp32c3
"""
BUTTON: microcontroller.Pin = ...
BOOT0: microcontroller.Pin = ...
D0: microcontroller.Pin = ...
A0: microcontroller.Pin = ...
D18: microcontroller.Pin = ...
A1: microcontroller.Pin = ...
D17: microcontroller.Pin = ...
A2: microcontroller.Pin = ...
D9: microcontroller.Pin = ...
A3: microcontroller.Pin = ...
D8: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
D7: microcontroller.Pin = ...
A4: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
D6: microcontroller.Pin = ...
A5: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
D5: microcontroller.Pin = ...
A6: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
D16: microcontroller.Pin = ...
A7: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
D35: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
D36: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
D37: microcontroller.Pin = ...
NEOPIXEL: microcontroller.Pin = ...
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

