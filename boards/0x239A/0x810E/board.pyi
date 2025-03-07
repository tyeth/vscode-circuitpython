from __future__ import annotations
import busio
import microcontroller
import typing
"""
board Adafruit Industries LLC nRF52840 LED Glasses Driver
https://circuitpython.org/boards/adafruit_led_glasses_nrf52840
"""
MICROPHONE_CLOCK: microcontroller.Pin = ...
MICROPHONE_DATA: microcontroller.Pin = ...
NEOPIXEL: microcontroller.Pin = ...
SWITCH: microcontroller.Pin = ...
LED: microcontroller.Pin = ...
ACCELEROMETER_INTERRUPT: microcontroller.Pin = ...
VOLTAGE_MONITOR: microcontroller.Pin = ...
BATTERY: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
STEMMA_I2C: typing.Any = ...
def I2C() -> busio.I2C:
    """Returns the `busio.I2C` object for the board's designated I2C bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.I2C`.
    """
    ...


