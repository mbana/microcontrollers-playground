# `microcontrollers-playground`

Currently just experimenting with these boards:

1. Challenger RP2040 WiFi/BLE MkII (Chip Antenna), iLabs, SKU: 105302:<https://thepihut.com/products/challenger-rp2040-wifi-ble-mkii-chip-antenna?srsltid=AfmBOopzcAZWlSnGHHmkhl2usFXs4mfhcFF3hcKnOi-f4k2X5Vgm6ejP>.

## `challenger_rp2040_wifi_ble`

```
Adafruit CircuitPython 9.2.4 on 2025-01-29; Challenger RP2040 WiFi/BLE with rp2040
Board ID:challenger_rp2040_wifi_ble
UID:DF61A86357872029
```

## `Firmware`

Get the firmware from <https://circuitpython.org/board/challenger_rp2040_wifi_ble/>, or if you prefer a direct link see the below:

1. <https://downloads.circuitpython.org/bin/challenger_rp2040_wifi_ble/en_GB/adafruit-circuitpython-challenger_rp2040_wifi_ble-en_GB-9.2.4.uf2>
2. <>

Then flash it to the `` drive.

##

```
circup install asyncio
circup update --all
```

Copy the code found in `code.py` into `code.py` in the mounted drive.

## Debugging

```
$ picocom /dev/ttyACM0 -b 115200
```

You might need to run as `sudo` or add yourself to the appriopriate group - `plugdev` or `dialout` for it to work without `sudo`.

## References

**TODO(MBama)**

## `LICENSE`

See [`./LICENSE`](./LICENSE).
