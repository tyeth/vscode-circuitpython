from __future__ import annotations
import busio
import microcontroller
"""
board Cytron Maker Zero SAMD21
https://circuitpython.org/boards/cytron_maker_zero_samd21
"""
A0: microcontroller.Pin = ...
A1: microcontroller.Pin = ...
A2: microcontroller.Pin = ...
A3: microcontroller.Pin = ...
A4: microcontroller.Pin = ...
A5: microcontroller.Pin = ...
D0: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
D1: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
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
LED: microcontroller.Pin = ...
D38: microcontroller.Pin = ...
ATN: microcontroller.Pin = ...
D20: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
D21: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
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

