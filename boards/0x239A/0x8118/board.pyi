from __future__ import annotations
import busio
import displayio
import microcontroller
import typing
"""
board Adafruit Camera
https://circuitpython.org/boards/adafruit_esp32s3_camera
"""
MOSI: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
TFT_RESET: microcontroller.Pin = ...
TFT_CS: microcontroller.Pin = ...
TFT_DC: microcontroller.Pin = ...
CARD_CS: microcontroller.Pin = ...
IRQ: microcontroller.Pin = ...
NEOPIXEL: microcontroller.Pin = ...
SPEAKER: microcontroller.Pin = ...
BUTTON: microcontroller.Pin = ...
BATTERY_MONITOR: microcontroller.Pin = ...
A0: microcontroller.Pin = ...
A1: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
CAMERA_DATA: typing.Any = ...
CAMERA_VSYNC: microcontroller.Pin = ...
CAMERA_HREF: microcontroller.Pin = ...
CAMERA_DATA9: microcontroller.Pin = ...
CAMERA_XCLK: microcontroller.Pin = ...
CAMERA_DATA8: microcontroller.Pin = ...
CAMERA_DATA7: microcontroller.Pin = ...
CAMERA_PCLK: microcontroller.Pin = ...
CAMERA_DATA6: microcontroller.Pin = ...
CAMERA_DATA2: microcontroller.Pin = ...
CAMERA_DATA5: microcontroller.Pin = ...
CAMERA_DATA3: microcontroller.Pin = ...
CAMERA_DATA4: microcontroller.Pin = ...
DISPLAY: displayio.Display = ...
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


