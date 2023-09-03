from __future__ import annotations
import busio
import displayio
import microcontroller
import typing
"""
board Adafruit Industries LLC Monster M4SK
https://circuitpython.org/boards/monster_m4sk
"""
MICROPHONE_CLOCK: microcontroller.Pin = ...
MICROPHONE_DATA: microcontroller.Pin = ...
RIGHT_TFT_CS: microcontroller.Pin = ...
RIGHT_TFT_DC: microcontroller.Pin = ...
LEFT_TFT_CS: microcontroller.Pin = ...
LEFT_TFT_DC: microcontroller.Pin = ...
STEMMA_I2C: typing.Any = ...
DISPLAY: displayio.Display = ...
RIGHT_DISPLAY: displayio.Display = ...
def I2C() -> busio.I2C:
    """Returns the `busio.I2C` object for the board's designated I2C bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.I2C`.
    """
    ...


