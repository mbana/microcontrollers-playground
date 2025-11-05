## `challenger_rp2040_wifi_ble`

```sh
Adafruit CircuitPython 9.2.4 on 2025-01-29; Challenger RP2040 WiFi/BLE with rp2040
Board ID:challenger_rp2040_wifi_ble
UID:DF61A86357872029
```

### `Firmware`

Get the firmware from <https://circuitpython.org/board/challenger_rp2040_wifi_ble/>, or if you prefer a direct link see <https://downloads.circuitpython.org/bin/challenger_rp2040_wifi_ble/en_GB/adafruit-circuitpython-challenger_rp2040_wifi_ble-en_GB-9.2.4.uf2>.

Then flash it to the drive.

###

```sh
circup install asyncio
circup update --all
```

Copy the code found in `code.py` into `code.py` in the mounted drive.

### Debugging

```sh
$ picocom /dev/ttyACM0 -b 115200
```

You might need to run as `sudo` or add yourself to the appriopriate group - `plugdev` or `dialout` for it to work without `sudo`.

## References
