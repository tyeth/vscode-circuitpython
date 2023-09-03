from __future__ import annotations
import busio
import typing
"""
board Oak Dev Tech Pixelwing ESP32S2
https://circuitpython.org/boards/odt_pixelwing_esp32_s2
"""
STEMMA_I2C: typing.Any = ...
def I2C() -> busio.I2C:
    """Returns the `busio.I2C` object for the board's designated I2C bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.I2C`.
    """
    ...


