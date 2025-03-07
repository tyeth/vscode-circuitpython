from __future__ import annotations
import busio
import microcontroller
"""
board @sarfata shIRtty
https://circuitpython.org/boards/shirtty
"""
D0: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
D1: microcontroller.Pin = ...
IR_RX: microcontroller.Pin = ...
D2: microcontroller.Pin = ...
A2: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
D3: microcontroller.Pin = ...
A3: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
D4: microcontroller.Pin = ...
A4: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
D5: microcontroller.Pin = ...
D6: microcontroller.Pin = ...
D7: microcontroller.Pin = ...
D8: microcontroller.Pin = ...
IR_TX: microcontroller.Pin = ...
def I2C() -> busio.I2C:
    """Returns the `busio.I2C` object for the board's designated I2C bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.I2C`.
    """
    ...


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


