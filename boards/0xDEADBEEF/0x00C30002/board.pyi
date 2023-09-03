from __future__ import annotations
import busio
import microcontroller
"""
board luatos_core_esp32c3_ch343
https://circuitpython.org/boards/luatos_core_esp32c3_ch343
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
BOOT0: microcontroller.Pin = ...
BUTTON: microcontroller.Pin = ...
IO10: microcontroller.Pin = ...
IO12: microcontroller.Pin = ...
LED: microcontroller.Pin = ...
IO13: microcontroller.Pin = ...
LED2: microcontroller.Pin = ...
IO18: microcontroller.Pin = ...
IO19: microcontroller.Pin = ...
def UART() -> busio.UART:
    """Returns the `busio.UART` object for the board's designated UART bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.UART`.
    """
    ...

