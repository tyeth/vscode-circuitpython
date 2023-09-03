from __future__ import annotations
import busio
import microcontroller
"""
board Smart Bee Designs Bee-Motion-S3
https://circuitpython.org/boards/smartbeedesigns_bee_motion_s3
"""
IO5: microcontroller.Pin = ...
A5: microcontroller.Pin = ...
D5: microcontroller.Pin = ...
IO6: microcontroller.Pin = ...
A6: microcontroller.Pin = ...
D6: microcontroller.Pin = ...
IO7: microcontroller.Pin = ...
A7: microcontroller.Pin = ...
D7: microcontroller.Pin = ...
IO8: microcontroller.Pin = ...
A8: microcontroller.Pin = ...
D8: microcontroller.Pin = ...
IO9: microcontroller.Pin = ...
A9: microcontroller.Pin = ...
D9: microcontroller.Pin = ...
IO10: microcontroller.Pin = ...
A10: microcontroller.Pin = ...
D10: microcontroller.Pin = ...
IO11: microcontroller.Pin = ...
A11: microcontroller.Pin = ...
D11: microcontroller.Pin = ...
IO12: microcontroller.Pin = ...
A12: microcontroller.Pin = ...
D12: microcontroller.Pin = ...
IO12: microcontroller.Pin = ...
A12: microcontroller.Pin = ...
D12: microcontroller.Pin = ...
IO13: microcontroller.Pin = ...
A13: microcontroller.Pin = ...
D13: microcontroller.Pin = ...
IO14: microcontroller.Pin = ...
A14: microcontroller.Pin = ...
D14: microcontroller.Pin = ...
IO15: microcontroller.Pin = ...
A15: microcontroller.Pin = ...
D15: microcontroller.Pin = ...
IO16: microcontroller.Pin = ...
D16: microcontroller.Pin = ...
IO17: microcontroller.Pin = ...
D17: microcontroller.Pin = ...
IO35: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
D35: microcontroller.Pin = ...
IO36: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
D36: microcontroller.Pin = ...
IO37: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
D37: microcontroller.Pin = ...
IO48: microcontroller.Pin = ...
NEOPIXEL: microcontroller.Pin = ...
NEOPIXEL_POWER: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
D43: microcontroller.Pin = ...
IO43: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
IO44: microcontroller.Pin = ...
D44: microcontroller.Pin = ...
BOOT_BTN: microcontroller.Pin = ...
BATTERY: microcontroller.Pin = ...
VBAT: microcontroller.Pin = ...
VBAT_SENSE: microcontroller.Pin = ...
VOLTAGE_MONITOR: microcontroller.Pin = ...
VBUS_SENSE: microcontroller.Pin = ...
LIGHT: microcontroller.Pin = ...
LIGHT_SENSOR: microcontroller.Pin = ...
PIR: microcontroller.Pin = ...
PIR_SENSOR: microcontroller.Pin = ...
LDO2: microcontroller.Pin = ...
def I2C() -> busio.I2C:
    """Returns the `busio.I2C` object for the board's designated I2C bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.I2C`.
    """
    ...


def UART() -> busio.UART:
    """Returns the `busio.UART` object for the board's designated UART bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.UART`.
    """
    ...

