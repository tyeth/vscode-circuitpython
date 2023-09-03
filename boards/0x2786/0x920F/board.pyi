from __future__ import annotations
import busio
import microcontroller
"""
board Switch Science, Inc. SSCI ISP1807 Micro Board
https://circuitpython.org/boards/ssci_isp1807_micro_board
"""
D0: microcontroller.Pin = ...
D1: microcontroller.Pin = ...
D2: microcontroller.Pin = ...
D3: microcontroller.Pin = ...
D4: microcontroller.Pin = ...
A4: microcontroller.Pin = ...
D5: microcontroller.Pin = ...
D6: microcontroller.Pin = ...
D7: microcontroller.Pin = ...
D8: microcontroller.Pin = ...
D9: microcontroller.Pin = ...
D10: microcontroller.Pin = ...
D14: microcontroller.Pin = ...
D15: microcontroller.Pin = ...
D16: microcontroller.Pin = ...
D17: microcontroller.Pin = ...
D18: microcontroller.Pin = ...
D19: microcontroller.Pin = ...
D20: microcontroller.Pin = ...
D21: microcontroller.Pin = ...
A0: microcontroller.Pin = ...
A1: microcontroller.Pin = ...
A2: microcontroller.Pin = ...
A3: microcontroller.Pin = ...
A5: microcontroller.Pin = ...
A6: microcontroller.Pin = ...
LED: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
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


