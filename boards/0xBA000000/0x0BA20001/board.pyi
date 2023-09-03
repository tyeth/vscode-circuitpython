from __future__ import annotations
import displayio
import microcontroller
"""
board espruino_banglejs2
https://circuitpython.org/boards/espruino_banglejs2
"""
PRESSURE_SCL: microcontroller.Pin = ...
VOLTAGE_MONITOR: microcontroller.Pin = ...
MEMLCD_CS: microcontroller.Pin = ...
MEMLCD_EXTCOMIN: microcontroller.Pin = ...
MEMLCD_DISP: microcontroller.Pin = ...
BACKLIGHT: microcontroller.Pin = ...
BUTTON: microcontroller.Pin = ...
VIBRATE: microcontroller.Pin = ...
HRM_POWER: microcontroller.Pin = ...
HRM_INT: microcontroller.Pin = ...
CHARGE_PORT: microcontroller.Pin = ...
HRM_SDA: microcontroller.Pin = ...
CHARGE_COMPLETE: microcontroller.Pin = ...
MEMLCD_SCK: microcontroller.Pin = ...
MEMLCD_MOSI: microcontroller.Pin = ...
GPS_POWER: microcontroller.Pin = ...
GPS_TX: microcontroller.Pin = ...
GPS_RX: microcontroller.Pin = ...
HRM_SCL: microcontroller.Pin = ...
TOUCH_SDA: microcontroller.Pin = ...
TOUCH_SCL: microcontroller.Pin = ...
TOUCH_INT: microcontroller.Pin = ...
ACCEL_SDA: microcontroller.Pin = ...
ACCEL_SCL: microcontroller.Pin = ...
COMPASS_SDA: microcontroller.Pin = ...
COMPASS_SCL: microcontroller.Pin = ...
PRESSURE_SDA: microcontroller.Pin = ...
DISPLAY: displayio.Display = ...
