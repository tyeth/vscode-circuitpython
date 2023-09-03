from __future__ import annotations
import busio
import microcontroller
"""
board PJRC/Sparkfun Teensy MicroMod
https://circuitpython.org/boards/sparkfun_teensy_micromod
"""
USB_HOST_POWER: microcontroller.Pin = ...
USB_HOST_DP: microcontroller.Pin = ...
USB_HOST_DM: microcontroller.Pin = ...
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

