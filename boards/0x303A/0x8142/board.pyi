from __future__ import annotations
import busio
import microcontroller
import typing
"""
board Turkish Technology Team Foundation Deneyap Mini
https://circuitpython.org/boards/deneyap_mini
"""
RX: microcontroller.Pin = ...
D0: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
D1: microcontroller.Pin = ...
D2: microcontroller.Pin = ...
PWM0: microcontroller.Pin = ...
D3: microcontroller.Pin = ...
PWM1: microcontroller.Pin = ...
MO: microcontroller.Pin = ...
D4: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
MI: microcontroller.Pin = ...
D5: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
MC: microcontroller.Pin = ...
D6: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
SC: microcontroller.Pin = ...
D7: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
SD: microcontroller.Pin = ...
D8: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
D9: microcontroller.Pin = ...
D10: microcontroller.Pin = ...
SS: microcontroller.Pin = ...
DA1: microcontroller.Pin = ...
D11: microcontroller.Pin = ...
DAC1: microcontroller.Pin = ...
DA0: microcontroller.Pin = ...
D12: microcontroller.Pin = ...
DAC0: microcontroller.Pin = ...
BT: microcontroller.Pin = ...
D13: microcontroller.Pin = ...
GPKEY: microcontroller.Pin = ...
D14: microcontroller.Pin = ...
LEDB: microcontroller.Pin = ...
D15: microcontroller.Pin = ...
LEDG: microcontroller.Pin = ...
D16: microcontroller.Pin = ...
LEDR: microcontroller.Pin = ...
A0: microcontroller.Pin = ...
T0: microcontroller.Pin = ...
A1: microcontroller.Pin = ...
T1: microcontroller.Pin = ...
A2: microcontroller.Pin = ...
T2: microcontroller.Pin = ...
A3: microcontroller.Pin = ...
T3: microcontroller.Pin = ...
A4: microcontroller.Pin = ...
T4: microcontroller.Pin = ...
A5: microcontroller.Pin = ...
T5: microcontroller.Pin = ...
A6: microcontroller.Pin = ...
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

