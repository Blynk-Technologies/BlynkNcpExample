#pragma once

/* TFT_eSPI config */

#define USER_SETUP_LOADED 1

#define ST7789_DRIVER

#define TFT_WIDTH  135
#define TFT_HEIGHT 240

#define CGRAM_OFFSET      // Library will add offsets required

#define TFT_MISO    -1
#define TFT_MOSI     3
#define TFT_SCLK     2
#define TFT_CS       5  // Chip select control pin
#define TFT_DC       1  // Data Command control pin
#define TFT_RST      0  // Reset pin (could connect to RST pin)

#define LOAD_GLCD   // Font 1. Original Adafruit 8 pixel font needs ~1820 bytes in FLASH
#define LOAD_FONT2  // Font 2. Small 16 pixel high font, needs ~3534 bytes in FLASH, 96 characters
#define LOAD_FONT4  // Font 4. Medium 26 pixel high font, needs ~5848 bytes in FLASH, 96 characters
#define LOAD_FONT6  // Font 6. Large 48 pixel font, needs ~2666 bytes in FLASH, only characters 1234567890:-.apm
#define LOAD_FONT7  // Font 7. 7 segment 48 pixel font, needs ~2438 bytes in FLASH, only characters 1234567890:.
#define LOAD_FONT8  // Font 8. Large 75 pixel font needs ~3256 bytes in FLASH, only characters 1234567890:-.
#define LOAD_FONT8N // Font 8. Alternative to Font 8 above, slightly narrower, so 3 digits fit a 160 pixel TFT
#define LOAD_GFXFF  // FreeFonts. Include access to the 48 Adafruit_GFX free fonts FF1 to FF48 and custom fonts

#define SMOOTH_FONT  1

#define SPI_FREQUENCY        40000000
#define SPI_READ_FREQUENCY   20000000
#define SUPPORT_TRANSACTIONS


/* T-PICO pin definitions */

#define PIN_TFT_BL      4
#define PIN_PWR_ON     22
#define PIN_BUTTON1     6
#define PIN_BUTTON2     7
#define PIN_RED_LED    25
#define PIN_BAT_VOLT   26

#define ESP32C3_RX_PIN  9
#define ESP32C3_TX_PIN  8
