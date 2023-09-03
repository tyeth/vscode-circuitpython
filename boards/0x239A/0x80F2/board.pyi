from __future__ import annotations
import busio
import microcontroller
import typing
"""
board Adafruit Feather RP2040
https://circuitpython.org/boards/adafruit_feather_rp2040
"""
A0: microcontroller.Pin = ...
A1: microcontroller.Pin = ...
A2: microcontroller.Pin = ...
A3: microcontroller.Pin = ...
D24: microcontroller.Pin = ...
D25: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
D0: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
D1: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
D4: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
D5: microcontroller.Pin = ...
D6: microcontroller.Pin = ...
D9: microcontroller.Pin = ...
D10: microcontroller.Pin = ...
D11: microcontroller.Pin = ...
D12: microcontroller.Pin = ...
LED: microcontroller.Pin = ...
D13: microcontroller.Pin = ...
BUTTON: microcontroller.Pin = ...
BOOT: microcontroller.Pin = ...
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

