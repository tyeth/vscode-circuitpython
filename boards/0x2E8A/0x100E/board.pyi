from __future__ import annotations
import busio
import displayio
import microcontroller
"""
board Raspberry Pi Zero
https://circuitpython.org/boards/raspberrypi_zero
"""
D0: microcontroller.Pin = ...
D1: microcontroller.Pin = ...
D2: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
D3: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
D4: microcontroller.Pin = ...
D5: microcontroller.Pin = ...
D6: microcontroller.Pin = ...
D7: microcontroller.Pin = ...
CE1: microcontroller.Pin = ...
D8: microcontroller.Pin = ...
CE0: microcontroller.Pin = ...
D9: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
D10: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
D11: microcontroller.Pin = ...
SCLK: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
D12: microcontroller.Pin = ...
D13: microcontroller.Pin = ...
D14: microcontroller.Pin = ...
TXD: microcontroller.Pin = ...
D15: microcontroller.Pin = ...
RXD: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
D16: microcontroller.Pin = ...
D17: microcontroller.Pin = ...
D18: microcontroller.Pin = ...
D19: microcontroller.Pin = ...
MISO_1: microcontroller.Pin = ...
D20: microcontroller.Pin = ...
MOSI_1: microcontroller.Pin = ...
D21: microcontroller.Pin = ...
SCLK_1: microcontroller.Pin = ...
SCK_1: microcontroller.Pin = ...
D22: microcontroller.Pin = ...
D23: microcontroller.Pin = ...
D24: microcontroller.Pin = ...
D25: microcontroller.Pin = ...
D26: microcontroller.Pin = ...
D27: microcontroller.Pin = ...
DISPLAY: displayio.Display = ...
def I2C() -> busio.I2C:
    """Returns the `busio.I2C` object for the board's designated I2C bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.I2C`.
    """
    ...


