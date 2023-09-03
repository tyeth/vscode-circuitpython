from __future__ import annotations
import busio
import microcontroller
"""
board NXP iMX RT 1050 EVKB
https://circuitpython.org/boards/imxrt1050_evkb
"""
LCD_BACKLIGHT: microcontroller.Pin = ...
LCD_RST: microcontroller.Pin = ...
LCD_ENABLE: microcontroller.Pin = ...
LCD_VSYNC: microcontroller.Pin = ...
LCD_HSYNC: microcontroller.Pin = ...
LCD_CLK: microcontroller.Pin = ...
LCD_D0: microcontroller.Pin = ...
LCD_D1: microcontroller.Pin = ...
LCD_D2: microcontroller.Pin = ...
LCD_D3: microcontroller.Pin = ...
LCD_D4: microcontroller.Pin = ...
LCD_D5: microcontroller.Pin = ...
LCD_D6: microcontroller.Pin = ...
LCD_D7: microcontroller.Pin = ...
LCD_D8: microcontroller.Pin = ...
LCD_D9: microcontroller.Pin = ...
LCD_D10: microcontroller.Pin = ...
LCD_D11: microcontroller.Pin = ...
LCD_D12: microcontroller.Pin = ...
LCD_D13: microcontroller.Pin = ...
LCD_D14: microcontroller.Pin = ...
LCD_D15: microcontroller.Pin = ...
LCD_TOUCH_INT: microcontroller.Pin = ...
AUDIO_INT: microcontroller.Pin = ...
AUDIO_MCLK: microcontroller.Pin = ...
AUDIO_RX_SYNC: microcontroller.Pin = ...
AUDIO_RX_BCLK: microcontroller.Pin = ...
AUDIO_RXD: microcontroller.Pin = ...
AUDIO_TXD: microcontroller.Pin = ...
AUDIO_TX_BCLK: microcontroller.Pin = ...
AUDIO_TX_SYNC: microcontroller.Pin = ...
SPDIF_IN: microcontroller.Pin = ...
SPDIF_OUT: microcontroller.Pin = ...
ETHERNET_MDIO: microcontroller.Pin = ...
ETHERNET_MDC: microcontroller.Pin = ...
ETHERNET_RXD0: microcontroller.Pin = ...
ETHERNET_RXD1: microcontroller.Pin = ...
ETHERNET_CRS_DV: microcontroller.Pin = ...
ETHERNET_TXD0: microcontroller.Pin = ...
ETHERNET_TXD1: microcontroller.Pin = ...
ETHERNET_TXEN: microcontroller.Pin = ...
ETHERNET_INT: microcontroller.Pin = ...
ETHERNET_RST: microcontroller.Pin = ...
ETHERNET_CLK: microcontroller.Pin = ...
ETHERNET_RXER: microcontroller.Pin = ...
FREELINK_TX: microcontroller.Pin = ...
FREELINK_RX: microcontroller.Pin = ...
CAN_TX: microcontroller.Pin = ...
CAN_RX: microcontroller.Pin = ...
CAN_STBY: microcontroller.Pin = ...
USB_HOST_DP: microcontroller.Pin = ...
USB_HOST_DM: microcontroller.Pin = ...
USB_HOST_DP: microcontroller.Pin = ...
USB_HOST_DM: microcontroller.Pin = ...
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

