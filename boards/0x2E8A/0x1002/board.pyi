from __future__ import annotations
import busio
import microcontroller
import typing
"""
board Pimoroni Pimoroni Pico LiPo (4MB)
https://circuitpython.org/boards/pimoroni_picolipo_4mb
"""
GP0: microcontroller.Pin = ...
GP1: microcontroller.Pin = ...
GP2: microcontroller.Pin = ...
GP3: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
GP4: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
GP5: microcontroller.Pin = ...
GP6: microcontroller.Pin = ...
GP7: microcontroller.Pin = ...
GP8: microcontroller.Pin = ...
GP9: microcontroller.Pin = ...
GP10: microcontroller.Pin = ...
GP11: microcontroller.Pin = ...
GP12: microcontroller.Pin = ...
GP13: microcontroller.Pin = ...
GP14: microcontroller.Pin = ...
GP15: microcontroller.Pin = ...
GP16: microcontroller.Pin = ...
GP17: microcontroller.Pin = ...
GP18: microcontroller.Pin = ...
GP19: microcontroller.Pin = ...
GP20: microcontroller.Pin = ...
GP21: microcontroller.Pin = ...
GP22: microcontroller.Pin = ...
USER_SW: microcontroller.Pin = ...
VBUS_DETECT: microcontroller.Pin = ...
LED: microcontroller.Pin = ...
GP25: microcontroller.Pin = ...
GP26_A0: microcontroller.Pin = ...
GP26: microcontroller.Pin = ...
A0: microcontroller.Pin = ...
GP27_A1: microcontroller.Pin = ...
GP27: microcontroller.Pin = ...
A1: microcontroller.Pin = ...
GP28_A2: microcontroller.Pin = ...
GP28: microcontroller.Pin = ...
A2: microcontroller.Pin = ...
A3: microcontroller.Pin = ...
BAT_SENSE: microcontroller.Pin = ...
STEMMA_I2C: typing.Any = ...
def I2C() -> busio.I2C:
    """Returns the `busio.I2C` object for the board's designated I2C bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.I2C`.
    """
    ...


