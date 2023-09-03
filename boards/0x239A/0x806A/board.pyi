from __future__ import annotations
import busio
import microcontroller
"""
board WeAct stm32f411ce blackpill
https://circuitpython.org/boards/stm32f411ce_blackpill
"""
B12: microcontroller.Pin = ...
B13: microcontroller.Pin = ...
B14: microcontroller.Pin = ...
B15: microcontroller.Pin = ...
A8: microcontroller.Pin = ...
A9: microcontroller.Pin = ...
A10: microcontroller.Pin = ...
A11: microcontroller.Pin = ...
A12: microcontroller.Pin = ...
A15: microcontroller.Pin = ...
B3: microcontroller.Pin = ...
B4: microcontroller.Pin = ...
B5: microcontroller.Pin = ...
B6: microcontroller.Pin = ...
B7: microcontroller.Pin = ...
B8: microcontroller.Pin = ...
B9: microcontroller.Pin = ...
B10: microcontroller.Pin = ...
B2: microcontroller.Pin = ...
B1: microcontroller.Pin = ...
B0: microcontroller.Pin = ...
A7: microcontroller.Pin = ...
A6: microcontroller.Pin = ...
A5: microcontroller.Pin = ...
A4: microcontroller.Pin = ...
A3: microcontroller.Pin = ...
A2: microcontroller.Pin = ...
A1: microcontroller.Pin = ...
A0: microcontroller.Pin = ...
C15: microcontroller.Pin = ...
C14: microcontroller.Pin = ...
C13: microcontroller.Pin = ...
LED: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
def I2C() -> busio.I2C:
    """Returns the `busio.I2C` object for the board's designated I2C bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.I2C`.
    """
    ...


