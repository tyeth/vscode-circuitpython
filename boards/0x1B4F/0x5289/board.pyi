from __future__ import annotations
import busio
import microcontroller
import typing
"""
board SparkFun Electronics SFE_nRF52840_Mini
https://circuitpython.org/boards/sparkfun_nrf52840_mini
"""
D0: microcontroller.Pin = ...
D1: microcontroller.Pin = ...
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
D14: microcontroller.Pin = ...
D15: microcontroller.Pin = ...
D16: microcontroller.Pin = ...
D17: microcontroller.Pin = ...
A0: microcontroller.Pin = ...
A1: microcontroller.Pin = ...
A2: microcontroller.Pin = ...
A3: microcontroller.Pin = ...
A4: microcontroller.Pin = ...
A5: microcontroller.Pin = ...
A6: microcontroller.Pin = ...
A7: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
LED1: microcontroller.Pin = ...
BUTTON1: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
QWIIC: typing.Any = ...
STEMMA_I2C: typing.Any = ...
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


