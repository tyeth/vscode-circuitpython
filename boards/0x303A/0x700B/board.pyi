from __future__ import annotations
import busio
import displayio
import microcontroller
"""
board Espressif ESP32-S3-USB-OTG-N8
https://circuitpython.org/boards/espressif_esp32s3_usb_otg_n8
"""
USB_SEL: microcontroller.Pin = ...
LED_GREEN: microcontroller.Pin = ...
LED: microcontroller.Pin = ...
LED_YELLOW: microcontroller.Pin = ...
BUTTON_OK: microcontroller.Pin = ...
BUTTON_UP: microcontroller.Pin = ...
BUTTON_DW: microcontroller.Pin = ...
BUTTON_DOWN: microcontroller.Pin = ...
BUTTON_MENU: microcontroller.Pin = ...
LCD_RST: microcontroller.Pin = ...
LCD_EN: microcontroller.Pin = ...
LCD_DC: microcontroller.Pin = ...
LCD_SCLK: microcontroller.Pin = ...
LCD_SDA: microcontroller.Pin = ...
LCD_BL: microcontroller.Pin = ...
SD_SCK: microcontroller.Pin = ...
SD_D0: microcontroller.Pin = ...
SD_D1: microcontroller.Pin = ...
SD_D2: microcontroller.Pin = ...
SD_D3: microcontroller.Pin = ...
HOST_VOL: microcontroller.Pin = ...
BAT_VOL: microcontroller.Pin = ...
BATTERY: microcontroller.Pin = ...
VOLTAGE_MONITOR: microcontroller.Pin = ...
LIMIT_EN: microcontroller.Pin = ...
OVER_CURRENT: microcontroller.Pin = ...
DEV_VBUS_EN: microcontroller.Pin = ...
BOOST_EN: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
DISPLAY: displayio.Display = ...
def UART() -> busio.UART:
    """Returns the `busio.UART` object for the board's designated UART bus(es).
    The object created is a singleton, and uses the default parameter values for `busio.UART`.
    """
    ...

