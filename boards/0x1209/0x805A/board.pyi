from __future__ import annotations
import busio
import microcontroller
"""
board ElectronicCats BastBLE
https://circuitpython.org/boards/bastble
"""
D2: microcontroller.Pin = ...
D3: microcontroller.Pin = ...
D4: microcontroller.Pin = ...
D5: microcontroller.Pin = ...
D6: microcontroller.Pin = ...
D7: microcontroller.Pin = ...
D8: microcontroller.Pin = ...
D9: microcontroller.Pin = ...
D10: microcontroller.Pin = ...
D11: microcontroller.Pin = ...
D12: microcontroller.Pin = ...
D13: microcontroller.Pin = ...
A0: microcontroller.Pin = ...
A1: microcontroller.Pin = ...
A2: microcontroller.Pin = ...
A3: microcontroller.Pin = ...
A4: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
A5: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
LED: microcontroller.Pin = ...
AREF: microcontroller.Pin = ...
VBAT: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
def UART() -> busio.UART:
    """Returns the `busio.UART` object for the board's designated UART bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.UART`.
    """
    ...

def SPI() -> busio.SPI:
    """Returns the `busio.SPI` object for the board's designated SPI bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.SPI`.
    """
    ...


def I2C() -> busio.I2C:
    """Returns the `busio.I2C` object for the board's designated I2C bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.I2C`.
    """
    ...


