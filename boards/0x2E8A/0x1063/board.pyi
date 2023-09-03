from __future__ import annotations
import busio
import displayio
import microcontroller
import typing
"""
board Pajenicko s.r.o. PicoPad
https://circuitpython.org/boards/pajenicko_picopad
"""
GP0: microcontroller.Pin = ...
GP1: microcontroller.Pin = ...
GP2: microcontroller.Pin = ...
GP3: microcontroller.Pin = ...
GP4: microcontroller.Pin = ...
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
GP26: microcontroller.Pin = ...
GP27: microcontroller.Pin = ...
GP28: microcontroller.Pin = ...
D0: microcontroller.Pin = ...
D1: microcontroller.Pin = ...
D2: microcontroller.Pin = ...
D3: microcontroller.Pin = ...
D4: microcontroller.Pin = ...
D5: microcontroller.Pin = ...
A0: microcontroller.Pin = ...
A1: microcontroller.Pin = ...
A2: microcontroller.Pin = ...
LCD_RESET: microcontroller.Pin = ...
LCD_CS: microcontroller.Pin = ...
LCD_SCLK: microcontroller.Pin = ...
LCD_MOSI: microcontroller.Pin = ...
LCD_DC: microcontroller.Pin = ...
LCD_BL: microcontroller.Pin = ...
AUDIO: microcontroller.Pin = ...
LED: microcontroller.Pin = ...
SW_X: microcontroller.Pin = ...
SW_Y: microcontroller.Pin = ...
SW_A: microcontroller.Pin = ...
SW_B: microcontroller.Pin = ...
SW_DOWN: microcontroller.Pin = ...
SW_RIGHT: microcontroller.Pin = ...
SW_LEFT: microcontroller.Pin = ...
SW_UP: microcontroller.Pin = ...
SD_CS: microcontroller.Pin = ...
SD_SCK: microcontroller.Pin = ...
SD_MOSI: microcontroller.Pin = ...
SD_MISO: microcontroller.Pin = ...
BAT_SENSE: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
SDA_ALT: microcontroller.Pin = ...
SCL_ALT: microcontroller.Pin = ...
I2C_ALT: typing.Any = ...
SMPS_MODE: microcontroller.Pin = ...
LED: microcontroller.Pin = ...
VBUS_SENSE: microcontroller.Pin = ...
DISPLAY: displayio.Display = ...
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

