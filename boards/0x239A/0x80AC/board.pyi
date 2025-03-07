from __future__ import annotations
import busio
import microcontroller
import typing
"""
board UnexpectedMaker FeatherS2
https://circuitpython.org/boards/unexpectedmaker_feathers2
"""
IO18: microcontroller.Pin = ...
A1: microcontroller.Pin = ...
D15: microcontroller.Pin = ...
DAC2: microcontroller.Pin = ...
IO17: microcontroller.Pin = ...
A0: microcontroller.Pin = ...
D14: microcontroller.Pin = ...
DAC1: microcontroller.Pin = ...
IO14: microcontroller.Pin = ...
A2: microcontroller.Pin = ...
D16: microcontroller.Pin = ...
IO12: microcontroller.Pin = ...
A3: microcontroller.Pin = ...
D17: microcontroller.Pin = ...
IO6: microcontroller.Pin = ...
A4: microcontroller.Pin = ...
D18: microcontroller.Pin = ...
IO5: microcontroller.Pin = ...
A5: microcontroller.Pin = ...
D19: microcontroller.Pin = ...
IO36: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
D25: microcontroller.Pin = ...
IO35: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
D24: microcontroller.Pin = ...
IO37: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
D23: microcontroller.Pin = ...
IO44: microcontroller.Pin = ...
D0: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
IO43: microcontroller.Pin = ...
D1: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
IO8: microcontroller.Pin = ...
D10: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
IO9: microcontroller.Pin = ...
D11: microcontroller.Pin = ...
IO0: microcontroller.Pin = ...
D4: microcontroller.Pin = ...
IO1: microcontroller.Pin = ...
D5: microcontroller.Pin = ...
A10: microcontroller.Pin = ...
IO3: microcontroller.Pin = ...
D6: microcontroller.Pin = ...
A9: microcontroller.Pin = ...
IO7: microcontroller.Pin = ...
D9: microcontroller.Pin = ...
A8: microcontroller.Pin = ...
IO33: microcontroller.Pin = ...
D20: microcontroller.Pin = ...
IO38: microcontroller.Pin = ...
D21: microcontroller.Pin = ...
IO10: microcontroller.Pin = ...
D12: microcontroller.Pin = ...
A7: microcontroller.Pin = ...
IO11: microcontroller.Pin = ...
D13: microcontroller.Pin = ...
A6: microcontroller.Pin = ...
LED: microcontroller.Pin = ...
APA102_MOSI: microcontroller.Pin = ...
APA102_SCK: microcontroller.Pin = ...
LDO2: microcontroller.Pin = ...
IO21: microcontroller.Pin = ...
IO4: microcontroller.Pin = ...
AMB: microcontroller.Pin = ...
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

