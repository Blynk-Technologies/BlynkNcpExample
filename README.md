
# Blynk.NCP

[![Issues](https://img.shields.io/github/issues/blynkkk/BlynkNcpExample.svg)](https://github.com/blynkkk/BlynkNcpExample/issues)
[![downloads](https://img.shields.io/github/downloads/blynkkk/BlynkNcpDriver/total)](https://github.com/blynkkk/BlynkNcpDriver/releases/latest)
[![PlatformIO CI](https://img.shields.io/github/actions/workflow/status/blynkkk/BlynkNcpExample/build.yml)](https://github.com/blynkkk/BlynkNcpExample/actions/workflows/build.yml)
[![License](https://img.shields.io/github/license/blynkkk/BlynkNcpExample?color=blue)](LICENSE)
[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/badges/StandWithUkraine.svg)](https://stand-with-ukraine.pp.ua)

**Blynk.NCP** is a solution that off-loads connectivity to a **Network Co-Processor (NCP)**, while your application logic resides on the **Primary MCU**. This implies a [dual-Microcontroller Unit (MCU)](https://docs.google.com/presentation/d/1aP2sQWB0J9EWj8Y1h5qeyfm2aFwaNSUKnCE-k7zxVnk/present) architecture.

## When to use Blynk.NCP?

Using Blynk.NCP is recommended if one of these is true:

- You have one of the [supported dual-MCU](#supported-boards) boards and want connect it to Blynk
- You're building a new IoT product with specific requirements for the Primary MCU, so you're adding a separate connectivity module
- You are using Blynk for retrofitting your existing products
- You have included an **AT command**-based module, but you struggle to make it work right or to achieve your product goals
- You are looking for **ridiculously low** risks, integration efforts, and time to market, along with **improved reliability** of your products

## Features

- **Blynk.Inject**: connect your devices easily using [<img src="https://cdn.rawgit.com/simple-icons/simple-icons/develop/icons/googleplay.svg" width="16" height="16" /> Android App](https://play.google.com/store/apps/details?id=cloud.blynk),
[<img src="https://cdn.rawgit.com/simple-icons/simple-icons/develop/icons/apple.svg" width="16" height="16" /> iOS App](https://apps.apple.com/us/app/blynk-iot/id1559317868) or [🌐 Web Dashboard](https://blynk.cloud)
  - `BLE`-assisted device provisioning for the best end-user experience
  - `WiFiAP`-based provisioning for devices without BLE support
  - **Network Manager**: WiFi (up to 16 saved networks), Ethernet, Cellular (depending on the hardware)
  - Advanced network connection troubleshooting
- Secure **Blynk.Cloud** connection that provides simple API for:
  - Data transfer with Virtual Pins, reporting Events, and accessing Metadata
  - `Time`, `Timezone` and `Location`, with an ability to track local time when the device is offline, including DST transitions
- **Blynk.Air** - automatic Over The Air firmware updates using Web Dashboard
  - Both NCP and the Primary MCU firmware updates
  - Direct firmware upgrade using iOS/Android App, before device activation

Additional services that can be provided by the Blynk.NCP:

- `⏳ soon` Persistent automation scenarios - work even if the device is offline
- `⏳ soon` Non-volatile storage for [Preferences](https://github.com/vshymanskyy/Preferences) library
- `✅ ready` NCP-assisted [fail-safe OTA updates](https://github.com/blynkkk/BlynkNcpDriver/blob/main/docs/Firmware%20Upgrade.md#ncp-assisted-fail-safe-ota-updates)
- `✅ ready` Connectivity-related **device state indication** - requires a monochrome/RGB/addressable LED attached to the NCP
- `✅ ready` **User button** (also used for configuration reset) - requires a momentary push button attached to the NCP
- `✅ ready` **Factory testing** and provisioning
- `🤔 later` File System storage
- `🤔 later` Generic UDP/TCP/TLS socket API

## Supported boards

This example project is compatible with a set of ready-to-use Dual-MCU boards:

Board                            |                 | 🔄 MCU / NCP   | 🌐            | ⚙️      | 🗃️
:--                              | ---             | :---           | :---         | :---    | :---
[UNO R4 WiFi][1]                 | `unoR4wifi`     | `⏳ / ✅`      | WiFi 2.4     | BLE     | 4.25 MB
[Portenta C33][2]                | `portentaC33`   | `⏳ / ✅`      | WiFi 2.4     | BLE     | 512 KB
[Nano RP2040 Connect][3]         | `rp2040connect` | `✅ / ❌`      | WiFi 2.4     | BLE     | 384 KB
[Nano 33 IoT][4]                 | `nano33iot`     | `✅ / ❌`      | WiFi 2.4     | BLE     | 384 KB
[MKR WiFi 1010][5]               | `mkrwifi1010`   | `✅ / ❌`      | WiFi 2.4     | BLE     | 384 KB
[T-PicoC3][6]                    | `t_pico_c3`     | `✅ / ✅`      | WiFi 2.4     | BLE     | 512 KB
[RPi Pico][7] + [ESP8266][8]     | `pico_esp8266`  | `✅ / ✅`      | WiFi 2.4     | WiFiAP  | 1000 KB
[Wio Terminal][9]                | `⏳`            | `✅ / ❔`      | WiFi 2.4/5   | BLE     | ❔

🔄 Over-the-Air Updates, 🌐 Connectivity, ⚙️ Provisioning, 🗃️ File System

## Custom boards

You can also [add one of the supported connectivity modules](docs/BuildYourOwn.md) to your own board.

## Getting started

This project uses **PlatformIO**. We recommend using [**VSCode**][pio_vscode] or [**PIO CLI**][pio_cli].  
See the [**troubleshooting**](#troubleshooting) section if you have issues with the following steps.

1. Clone this repository using `git`, or download it as a [`ZIP` file](https://github.com/blynkkk/BlynkNcpExample/archive/refs/heads/main.zip).

2. Flash the Blynk.NCP firmware (***replace `nano33iot` with your board type***):

```sh
pio run -e nano33iot -t upload_ncp
```

> __Warning__: This overwrites both the Main MCU and the connectivity module firmware.  
> You can [restore the stock firmware][restore] easily.

3. Open `src/main.cpp` and fill in [information from your Blynk Template](https://bit.ly/BlynkInject):

```cpp
#define BLYNK_TEMPLATE_ID           "TMPxxxxxx"
#define BLYNK_TEMPLATE_NAME         "MyDevice"
```

4. Build and flash the example project, run the serial monitor:

```sh
pio run -e nano33iot -t upload
pio device monitor
```

## Use the Blynk iOS/Android app to configure your new device

Ensure that the Blynk App is installed on your smartphone and scan this QR code:

<img alt="Add New Device QR" src="./docs/Images/AddNewDeviceQR.png" width="250" />

Alternatively: Open the `Blynk App` -> click `Add New Device` -> select `Find Devices Nearby`

## Disclaimer

> The community edition of Blynk.NCP is available for personal use and evaluation.  
> If you're interested in using Blynk.NCP for commercial applications, feel free to [contact Blynk][blynk_sales]. Thank you!

## Troubleshooting

If something doesn't work, try some of these solutions:
- If your board is based on a Raspberry Pi RP2040 chip, it may fail to work on Windows. Please apply [this fix][fix_windows_rp2040]
- Upgrade PlatformIO to the latest version. Run: `pio upgrade`
- Upgrade packages to the latest version. Run: `pio pkg update`


[blynk_sales]: https://blynk.io/en/contact-us-business
[pio_vscode]: https://docs.platformio.org/en/stable/integration/ide/vscode.html#ide-vscode
[pio_cli]: https://docs.platformio.org/en/stable/core/index.html
[restore]: ./docs/RestoreFirmware.md
[arduino_ide]: https://github.com/blynkkk/blynk-library/blob/master/examples/Blynk.Edgent/Edgent_NCP/Edgent_NCP.ino
[fix_windows_rp2040]: https://arduino-pico.readthedocs.io/en/latest/platformio.html#important-steps-for-windows-users-before-installing

[1]: https://store-usa.arduino.cc/products/uno-r4-wifi
[2]: https://store-usa.arduino.cc/products/portenta-c33
[3]: https://store-usa.arduino.cc/products/arduino-nano-rp2040-connect
[4]: https://store-usa.arduino.cc/products/arduino-nano-33-iot
[5]: https://store-usa.arduino.cc/products/arduino-mkr-wifi-1010
[6]: https://www.lilygo.cc/products/lilygo%C2%AE-t-picoc3-esp32-c3-rp2040-1-14-inch-lcd-st7789v
[7]: https://www.raspberrypi.com/products/raspberry-pi-pico
[8]: https://www.waveshare.com/pico-esp8266.htm
[9]: https://www.seeedstudio.com/Wio-Terminal-p-4509.html

