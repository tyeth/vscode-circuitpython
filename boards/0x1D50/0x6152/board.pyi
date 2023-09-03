from __future__ import annotations
import busio
import microcontroller
"""
board nrf52.jpconstantineau.com BlueMicro833
https://circuitpython.org/boards/bluemicro833
"""
P0_02: microcontroller.Pin = ...
P0_03: microcontroller.Pin = ...
P0_04: microcontroller.Pin = ...
P0_05: microcontroller.Pin = ...
P0_06: microcontroller.Pin = ...
P0_07: microcontroller.Pin = ...
P0_08: microcontroller.Pin = ...
P0_09: microcontroller.Pin = ...
P0_10: microcontroller.Pin = ...
P0_11: microcontroller.Pin = ...
P0_12: microcontroller.Pin = ...
P0_13: microcontroller.Pin = ...
P0_14: microcontroller.Pin = ...
P0_15: microcontroller.Pin = ...
P0_16: microcontroller.Pin = ...
P0_17: microcontroller.Pin = ...
P0_19: microcontroller.Pin = ...
P0_20: microcontroller.Pin = ...
P0_21: microcontroller.Pin = ...
P0_22: microcontroller.Pin = ...
P0_23: microcontroller.Pin = ...
P0_24: microcontroller.Pin = ...
P0_25: microcontroller.Pin = ...
P0_26: microcontroller.Pin = ...
P0_27: microcontroller.Pin = ...
P0_28: microcontroller.Pin = ...
P0_29: microcontroller.Pin = ...
P0_30: microcontroller.Pin = ...
P0_31: microcontroller.Pin = ...
P1_00: microcontroller.Pin = ...
P1_01: microcontroller.Pin = ...
P1_02: microcontroller.Pin = ...
P1_03: microcontroller.Pin = ...
P1_04: microcontroller.Pin = ...
P1_05: microcontroller.Pin = ...
P1_06: microcontroller.Pin = ...
P1_07: microcontroller.Pin = ...
P1_08: microcontroller.Pin = ...
P1_09: microcontroller.Pin = ...
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
RX: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
LED1: microcontroller.Pin = ...
LED2: microcontroller.Pin = ...
RED_LED: microcontroller.Pin = ...
BLUE_LED: microcontroller.Pin = ...
VCC_ON: microcontroller.Pin = ...
NEOPIXEL: microcontroller.Pin = ...
def UART() -> busio.UART:
    """Returns the `busio.UART` object for the board's designated UART bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.UART`.
    """
    ...

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


