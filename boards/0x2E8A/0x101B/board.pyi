from __future__ import annotations
import busio
import displayio
import microcontroller
import typing
"""
board Pimoroni Badger 2040
https://circuitpython.org/boards/pimoroni_badger2040
"""
TX: microcontroller.Pin = ...
GP0: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
GP1: microcontroller.Pin = ...
INT: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
SW_DOWN: microcontroller.Pin = ...
SW_A: microcontroller.Pin = ...
SW_B: microcontroller.Pin = ...
SW_C: microcontroller.Pin = ...
SW_UP: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
INKY_CS: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
INKY_DC: microcontroller.Pin = ...
INKY_RST: microcontroller.Pin = ...
USER_SW: microcontroller.Pin = ...
VBUS_DETECT: microcontroller.Pin = ...
USER_LED: microcontroller.Pin = ...
INKY_BUSY: microcontroller.Pin = ...
VREF_POWER: microcontroller.Pin = ...
REF_1V2: microcontroller.Pin = ...
VBAT_SENSE: microcontroller.Pin = ...
DISPLAY: displayio.Display = ...
ENABLE_DIO: typing.Any = ...
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

