from __future__ import annotations
import busio
import microcontroller
"""
board lolin_c3_mini
https://circuitpython.org/boards/lolin_c3_mini
"""
IO0: microcontroller.Pin = ...
A0: microcontroller.Pin = ...
D0: microcontroller.Pin = ...
IO1: microcontroller.Pin = ...
A1: microcontroller.Pin = ...
D1: microcontroller.Pin = ...
IO2: microcontroller.Pin = ...
A2: microcontroller.Pin = ...
D2: microcontroller.Pin = ...
IO3: microcontroller.Pin = ...
A3: microcontroller.Pin = ...
D3: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
IO4: microcontroller.Pin = ...
A4: microcontroller.Pin = ...
D4: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
IO5: microcontroller.Pin = ...
A5: microcontroller.Pin = ...
D5: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
IO6: microcontroller.Pin = ...
D6: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
IO7: microcontroller.Pin = ...
D7: microcontroller.Pin = ...
LED: microcontroller.Pin = ...
NEOPIXEL: microcontroller.Pin = ...
IO8: microcontroller.Pin = ...
D8: microcontroller.Pin = ...
IO9: microcontroller.Pin = ...
BOOT0: microcontroller.Pin = ...
BUTTON: microcontroller.Pin = ...
IO10: microcontroller.Pin = ...
D10: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
IO20: microcontroller.Pin = ...
A7: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
IO21: microcontroller.Pin = ...
A6: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
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

