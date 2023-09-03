from __future__ import annotations
import busio
import microcontroller
"""
board SparkFun Electronics SparkFun MicroMod nRF52840 Processor
https://circuitpython.org/boards/sparkfun_nrf52840_micromod
"""
LED: microcontroller.Pin = ...
P3V3_EN: microcontroller.Pin = ...
BATT_VIN3: microcontroller.Pin = ...
RESET: microcontroller.Pin = ...
BOOT: microcontroller.Pin = ...
UART_TX1: microcontroller.Pin = ...
UART_RX1: microcontroller.Pin = ...
UART_RTS1: microcontroller.Pin = ...
UART_CTS1: microcontroller.Pin = ...
TX: microcontroller.Pin = ...
RX: microcontroller.Pin = ...
UART_TX2: microcontroller.Pin = ...
UART_RX2: microcontroller.Pin = ...
I2C_SDA: microcontroller.Pin = ...
I2C_SCL: microcontroller.Pin = ...
SDA: microcontroller.Pin = ...
SCL: microcontroller.Pin = ...
I2C_INT: microcontroller.Pin = ...
I2C_SDA1: microcontroller.Pin = ...
I2C_SCL1: microcontroller.Pin = ...
SPI_CIPO: microcontroller.Pin = ...
SPI_MISO: microcontroller.Pin = ...
SPI_COPI: microcontroller.Pin = ...
SPI_MOSI: microcontroller.Pin = ...
SPI_SCK: microcontroller.Pin = ...
SPI_CS: microcontroller.Pin = ...
CIPO: microcontroller.Pin = ...
MISO: microcontroller.Pin = ...
COPI: microcontroller.Pin = ...
MOSI: microcontroller.Pin = ...
SCK: microcontroller.Pin = ...
CS: microcontroller.Pin = ...
LED_DAT: microcontroller.Pin = ...
LED_CLK: microcontroller.Pin = ...
SDIO_CLK: microcontroller.Pin = ...
SDIO_CMD: microcontroller.Pin = ...
SDIO_DATA0: microcontroller.Pin = ...
SDIO_DATA1: microcontroller.Pin = ...
SDIO_DATA2: microcontroller.Pin = ...
SDIO_DATA3: microcontroller.Pin = ...
SPI_CIPO1: microcontroller.Pin = ...
SPI_MISO1: microcontroller.Pin = ...
SPI_COPI1: microcontroller.Pin = ...
SPI_MOSI1: microcontroller.Pin = ...
SPI_SCK1: microcontroller.Pin = ...
SPI_CS1: microcontroller.Pin = ...
PDM_DATA: microcontroller.Pin = ...
PDM_CLK: microcontroller.Pin = ...
A0: microcontroller.Pin = ...
A1: microcontroller.Pin = ...
PWM0: microcontroller.Pin = ...
PWM1: microcontroller.Pin = ...
D0: microcontroller.Pin = ...
D1: microcontroller.Pin = ...
G0: microcontroller.Pin = ...
G1: microcontroller.Pin = ...
G2: microcontroller.Pin = ...
G3: microcontroller.Pin = ...
G4: microcontroller.Pin = ...
G5: microcontroller.Pin = ...
G6: microcontroller.Pin = ...
G7: microcontroller.Pin = ...
G8: microcontroller.Pin = ...
G9: microcontroller.Pin = ...
G10: microcontroller.Pin = ...
BUS0: microcontroller.Pin = ...
BUS1: microcontroller.Pin = ...
BUS2: microcontroller.Pin = ...
BUS3: microcontroller.Pin = ...
BUS4: microcontroller.Pin = ...
BUS5: microcontroller.Pin = ...
BUS6: microcontroller.Pin = ...
BUS7: microcontroller.Pin = ...
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

