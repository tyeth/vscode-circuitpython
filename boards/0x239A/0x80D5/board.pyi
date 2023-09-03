from __future__ import annotations
import busio
import microcontroller
"""
board Radomir Dopieralski PewPew 10.2
https://circuitpython.org/boards/pewpew10
"""
_R1: microcontroller.Pin = ...
_R2: microcontroller.Pin = ...
_R3: microcontroller.Pin = ...
_R4: microcontroller.Pin = ...
_R5: microcontroller.Pin = ...
_R6: microcontroller.Pin = ...
_R7: microcontroller.Pin = ...
_R8: microcontroller.Pin = ...
_C8: microcontroller.Pin = ...
_C7: microcontroller.Pin = ...
_C6: microcontroller.Pin = ...
_C5: microcontroller.Pin = ...
_C4: microcontroller.Pin = ...
_C3: microcontroller.Pin = ...
_C2: microcontroller.Pin = ...
_C1: microcontroller.Pin = ...
_BUTTONS: microcontroller.Pin = ...
P1: microcontroller.Pin = ...
P2: microcontroller.Pin = ...
P3: microcontroller.Pin = ...
P4: microcontroller.Pin = ...
P5: microcontroller.Pin = ...
P6: microcontroller.Pin = ...
P7: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
DAC: microcontroller.Pin = ...
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

