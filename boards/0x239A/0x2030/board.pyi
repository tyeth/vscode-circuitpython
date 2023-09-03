from __future__ import annotations
import busio
import microcontroller
"""
board Czech maker Maker badge
https://circuitpython.org/boards/maker_badge
"""
D0: microcontroller.Pin = ...
D1: microcontroller.Pin = ...
CAP5: microcontroller.Pin = ...
D2: microcontroller.Pin = ...
CAP4: microcontroller.Pin = ...
D3: microcontroller.Pin = ...
CAP3: microcontroller.Pin = ...
D4: microcontroller.Pin = ...
CAP2: microcontroller.Pin = ...
D5: microcontroller.Pin = ...
CAP1: microcontroller.Pin = ...
D6: microcontroller.Pin = ...
VOLTAGE_MONITOR: microcontroller.Pin = ...
BATTERY: microcontroller.Pin = ...
D7: microcontroller.Pin = ...
D8: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
D9: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
D10: microcontroller.Pin = ...
D11: microcontroller.Pin = ...
D12: microcontroller.Pin = ...
D13: microcontroller.Pin = ...
D14: microcontroller.Pin = ...
A4: microcontroller.Pin = ...
D15: microcontroller.Pin = ...
A3: microcontroller.Pin = ...
D16: microcontroller.Pin = ...
A2: microcontroller.Pin = ...
D17: microcontroller.Pin = ...
A1: microcontroller.Pin = ...
D18: microcontroller.Pin = ...
NEOPIXEL: microcontroller.Pin = ...
D21: microcontroller.Pin = ...
NEOPIXEL_POWER: microcontroller.Pin = ...
NEOPIXEL_POWER_INVERTED: microcontroller.Pin = ...
D26: microcontroller.Pin = ...
D33: microcontroller.Pin = ...
D34: microcontroller.Pin = ...
D35: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
D36: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
D37: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
D38: microcontroller.Pin = ...
D39: microcontroller.Pin = ...
D40: microcontroller.Pin = ...
D41: microcontroller.Pin = ...
D42: microcontroller.Pin = ...
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


