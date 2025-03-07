from __future__ import annotations
import busio
import microcontroller
"""
board WarmBit WarmBit BluePixel nRF52840
https://circuitpython.org/boards/warmbit_bluepixel
"""
A0: microcontroller.Pin = ...
A1: microcontroller.Pin = ...
D0: microcontroller.Pin = ...
D1: microcontroller.Pin = ...
D2: microcontroller.Pin = ...
D5: microcontroller.Pin = ...
D7: microcontroller.Pin = ...
D9: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
MAXTEMP_SCL: microcontroller.Pin = ...
MAXTEMP_SDA: microcontroller.Pin = ...
ACC_SCL: microcontroller.Pin = ...
ACC_SDA: microcontroller.Pin = ...
ADDON_SCL: microcontroller.Pin = ...
ADDON_SDA: microcontroller.Pin = ...
L: microcontroller.Pin = ...
LED: microcontroller.Pin = ...
YELLOW_LED: microcontroller.Pin = ...
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


