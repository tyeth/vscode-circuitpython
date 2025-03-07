from __future__ import annotations
import busio
import microcontroller
"""
board Espressif ESP32-S3-DevKitM-1-N8
https://circuitpython.org/boards/espressif_esp32s3_devkitm_1_n8
"""
IO0: microcontroller.Pin = ...
IO1: microcontroller.Pin = ...
IO2: microcontroller.Pin = ...
IO3: microcontroller.Pin = ...
IO4: microcontroller.Pin = ...
IO5: microcontroller.Pin = ...
IO6: microcontroller.Pin = ...
IO7: microcontroller.Pin = ...
IO8: microcontroller.Pin = ...
IO9: microcontroller.Pin = ...
IO10: microcontroller.Pin = ...
IO11: microcontroller.Pin = ...
IO12: microcontroller.Pin = ...
IO13: microcontroller.Pin = ...
IO14: microcontroller.Pin = ...
IO15: microcontroller.Pin = ...
IO16: microcontroller.Pin = ...
IO17: microcontroller.Pin = ...
IO18: microcontroller.Pin = ...
IO19: microcontroller.Pin = ...
IO20: microcontroller.Pin = ...
IO21: microcontroller.Pin = ...
IO35: microcontroller.Pin = ...
IO36: microcontroller.Pin = ...
IO37: microcontroller.Pin = ...
IO38: microcontroller.Pin = ...
IO39: microcontroller.Pin = ...
IO40: microcontroller.Pin = ...
IO41: microcontroller.Pin = ...
IO42: microcontroller.Pin = ...
IO43: microcontroller.Pin = ...
IO44: microcontroller.Pin = ...
IO45: microcontroller.Pin = ...
IO46: microcontroller.Pin = ...
IO47: microcontroller.Pin = ...
IO48: microcontroller.Pin = ...
NEOPIXEL: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
def UART() -> busio.UART:
    """Returns the `busio.UART` object for the board's designated UART bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.UART`.
    """
    ...

