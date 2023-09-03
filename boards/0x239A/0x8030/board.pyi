from __future__ import annotations
import busio
import microcontroller
import typing
"""
board Adafruit Industries LLC Trellis M4 Express
https://circuitpython.org/boards/trellis_m4_express
"""
APA102_MOSI: microcontroller.Pin = ...
DOTSTAR_DATA: microcontroller.Pin = ...
APA102_SCK: microcontroller.Pin = ...
DOTSTAR_CLOCK: microcontroller.Pin = ...
STEMMA_I2C: typing.Any = ...
def I2C() -> busio.I2C:
    """Returns the `busio.I2C` object for the board's designated I2C bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.I2C`.
    """
    ...


