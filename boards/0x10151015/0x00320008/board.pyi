from __future__ import annotations
import busio
import displayio
import microcontroller
import typing
"""
board m5stack_core2
https://circuitpython.org/boards/m5stack_core2
"""
MOSI: microcontroller.Pin = ...
D23: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
D38: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
D18: microcontroller.Pin = ...
D3: microcontroller.Pin = ...
PORTC_RX: microcontroller.Pin = ...
RX2: microcontroller.Pin = ...
D13: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
D21: microcontroller.Pin = ...
PORTA_SDA: microcontroller.Pin = ...
D32: microcontroller.Pin = ...
D27: microcontroller.Pin = ...
A27: microcontroller.Pin = ...
I2S_SDO: microcontroller.Pin = ...
D2: microcontroller.Pin = ...
A35: microcontroller.Pin = ...
D35: microcontroller.Pin = ...
PORTB_IN: microcontroller.Pin = ...
A36: microcontroller.Pin = ...
D36: microcontroller.Pin = ...
A25: microcontroller.Pin = ...
D25: microcontroller.Pin = ...
PORTB_OUT: microcontroller.Pin = ...
A26: microcontroller.Pin = ...
D26: microcontroller.Pin = ...
D1: microcontroller.Pin = ...
PORTC_TX: microcontroller.Pin = ...
TX2: microcontroller.Pin = ...
D14: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
D22: microcontroller.Pin = ...
PORTA_SCL: microcontroller.Pin = ...
D33: microcontroller.Pin = ...
D19: microcontroller.Pin = ...
I2S_LRC: microcontroller.Pin = ...
I2S_PDM_MIC_CLOCK: microcontroller.Pin = ...
D0: microcontroller.Pin = ...
I2S_PDM_MIC_DATA: microcontroller.Pin = ...
D34: microcontroller.Pin = ...
A34: microcontroller.Pin = ...
I2S_SCK: microcontroller.Pin = ...
TFT_CS: microcontroller.Pin = ...
TFT_DC: microcontroller.Pin = ...
SD_CS: microcontroller.Pin = ...
TOUCH_INT: microcontroller.Pin = ...
PORTA_I2C: typing.Any = ...
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

