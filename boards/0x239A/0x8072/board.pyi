from __future__ import annotations
import busio
import displayio
import microcontroller
import typing
"""
board Adafruit Industries LLC CLUE nRF52840 Express
https://circuitpython.org/boards/clue_nrf52840_express
"""
P0: microcontroller.Pin = ...
D0: microcontroller.Pin = ...
A2: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
P1: microcontroller.Pin = ...
D1: microcontroller.Pin = ...
A3: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
P2: microcontroller.Pin = ...
D2: microcontroller.Pin = ...
A4: microcontroller.Pin = ...
P3: microcontroller.Pin = ...
D3: microcontroller.Pin = ...
A5: microcontroller.Pin = ...
P4: microcontroller.Pin = ...
D4: microcontroller.Pin = ...
A6: microcontroller.Pin = ...
P5: microcontroller.Pin = ...
D5: microcontroller.Pin = ...
BUTTON_A: microcontroller.Pin = ...
P6: microcontroller.Pin = ...
D6: microcontroller.Pin = ...
P7: microcontroller.Pin = ...
D7: microcontroller.Pin = ...
P8: microcontroller.Pin = ...
D8: microcontroller.Pin = ...
P9: microcontroller.Pin = ...
D9: microcontroller.Pin = ...
P10: microcontroller.Pin = ...
D10: microcontroller.Pin = ...
A7: microcontroller.Pin = ...
P11: microcontroller.Pin = ...
D11: microcontroller.Pin = ...
BUTTON_B: microcontroller.Pin = ...
P12: microcontroller.Pin = ...
D12: microcontroller.Pin = ...
A0: microcontroller.Pin = ...
P13: microcontroller.Pin = ...
D13: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
P14: microcontroller.Pin = ...
D14: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
P15: microcontroller.Pin = ...
D15: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
P16: microcontroller.Pin = ...
D16: microcontroller.Pin = ...
A1: microcontroller.Pin = ...
P17: microcontroller.Pin = ...
D17: microcontroller.Pin = ...
L: microcontroller.Pin = ...
LED: microcontroller.Pin = ...
P18: microcontroller.Pin = ...
D18: microcontroller.Pin = ...
NEOPIXEL: microcontroller.Pin = ...
P19: microcontroller.Pin = ...
D19: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
P20: microcontroller.Pin = ...
D20: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
MICROPHONE_CLOCK: microcontroller.Pin = ...
MICROPHONE_DATA: microcontroller.Pin = ...
SPEAKER: microcontroller.Pin = ...
PROXIMITY_LIGHT_INTERRUPT: microcontroller.Pin = ...
ACCELEROMETER_GYRO_INTERRUPT: microcontroller.Pin = ...
WHITE_LEDS: microcontroller.Pin = ...
TFT_RESET: microcontroller.Pin = ...
TFT_BACKLIGHT: microcontroller.Pin = ...
TFT_CS: microcontroller.Pin = ...
TFT_DC: microcontroller.Pin = ...
TFT_SCK: microcontroller.Pin = ...
TFT_MOSI: microcontroller.Pin = ...
STEMMA_I2C: typing.Any = ...
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


def UART() -> busio.UART:
    """Returns the `busio.UART` object for the board's designated UART bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.UART`.
    """
    ...

