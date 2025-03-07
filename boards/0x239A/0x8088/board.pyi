from __future__ import annotations
import busio
import microcontroller
"""
board Adafruit Industries LLC Feather Bluefruit Sense
https://circuitpython.org/boards/feather_bluefruit_sense
"""
A0: microcontroller.Pin = ...
A1: microcontroller.Pin = ...
A2: microcontroller.Pin = ...
A3: microcontroller.Pin = ...
A4: microcontroller.Pin = ...
A5: microcontroller.Pin = ...
AREF: microcontroller.Pin = ...
VOLTAGE_MONITOR: microcontroller.Pin = ...
BATTERY: microcontroller.Pin = ...
SWITCH: microcontroller.Pin = ...
NFC1: microcontroller.Pin = ...
NFC2: microcontroller.Pin = ...
D2: microcontroller.Pin = ...
D3: microcontroller.Pin = ...
D5: microcontroller.Pin = ...
D6: microcontroller.Pin = ...
D9: microcontroller.Pin = ...
D10: microcontroller.Pin = ...
D11: microcontroller.Pin = ...
D12: microcontroller.Pin = ...
D13: microcontroller.Pin = ...
NEOPIXEL: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
L: microcontroller.Pin = ...
LED: microcontroller.Pin = ...
RED_LED: microcontroller.Pin = ...
BLUE_LED: microcontroller.Pin = ...
MICROPHONE_CLOCK: microcontroller.Pin = ...
MICROPHONE_DATA: microcontroller.Pin = ...
PROXIMITY_LIGHT_INTERRUPT: microcontroller.Pin = ...
ACCELEROMETER_GYRO_INTERRUPT: microcontroller.Pin = ...
def UART() -> busio.UART:
    """Returns the `busio.UART` object for the board's designated UART bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.UART`.
    """
    ...

def SPI() -> busio.SPI:
    """Returns the `busio.SPI` object for the board's designated SPI bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.SPI`.
    """
    ...


def I2C() -> busio.I2C:
    """Returns the `busio.I2C` object for the board's designated I2C bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.I2C`.
    """
    ...


