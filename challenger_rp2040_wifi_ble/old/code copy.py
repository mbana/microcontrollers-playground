import _asyncio as asyncio
import board
import digitalio
from digitalio import DigitalInOut, Direction
from rainbowio import colorwheel
import neopixel

print("starting")

async def blink_led():
    with neopixel.NeoPixel(board.NEOPIXEL, 1) as pixel:
        pixel.brightness = 0.3
        while True:
            for color_value in range(255):
                pixel[0] = colorwheel(color_value)
                await asyncio.sleep(1)

async def blink_neopixel():
    with DigitalInOut(board.LED) as led:
        led.direction = Direction.OUTPUT
        while True:
            led.value = True
            await asyncio.sleep(1)
            led.value = False
            await asyncio.sleep(1)

async def main():
    led1_task = asyncio.create_task(blink_led())
    # led2_task = asyncio.create_task(blink_neopixel())

    await asyncio.gather(led1_task)
    print("done")

asyncio.run(main())

# import asyncio
# import board
# import digitalio

# import time
# import board
# from rainbowio import colorwheel
# import neopixel

# import time
# import board
# from digitalio import DigitalInOut, Direction

# # LED setup for onboard LED
# led = DigitalInOut(board.LED)
# led.direction = Direction.OUTPUT

# pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
# pixel.brightness = 0.16

# def rainbow(delay):
#     for color_value in range(255):
#         pixel[0] = colorwheel(color_value)
#         time.sleep(delay)
#         # led.value = False

# while True:
#     led.value = True
#     rainbow(0.02)

# led.value = False
# print("led off")

# import time
# import board
# import neopixel

# pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

# pixel.brightness = 0.3

# while True:
#     pixel.fill((255, 0, 0))
#     time.sleep(0.5)
#     pixel.fill((0, 255, 0))
#     time.sleep(0.5)
#     pixel.fill((0, 0, 255))
#     time.sleep(0.5)

# import time
# import board
# from digitalio import DigitalInOut, Direction

# # LED setup for onboard LED
# led = DigitalInOut(board.LED)
# led.direction = Direction.OUTPUT

# while True:
#     led.value = True
#     print("led on")
#     time.sleep(1)

#     led.value = False
#     print("led off")
#     time.sleep(1)

# print("finished")

# import socketpool
# import wifi

# from adafruit_httpserver import Server, Request, Response

# AP_SSID = "123"
# AP_PASSWORD = "123"

# print("Creating access point...")
# wifi.radio.start_ap(ssid=AP_SSID, password=AP_PASSWORD)
# print(f"Created access point {AP_SSID}")

# pool = socketpool.SocketPool(wifi.radio)
# server = Server(pool, "/static", debug=True)

# @server.route("/")
# def base(request: Request):
#     """
#     Serve a default static plain text message.
#     """
#     return Response(request, "Hello from the CircuitPython HTTP Server!")

# server.serve_forever(str(wifi.radio.ipv4_address_ap))

# import time
# import board
# import busio
# from digitalio import DigitalInOut
# from digitalio import Direction
# from adafruit_espatcontrol import adafruit_espatcontrol

# # # Get wifi details and more from a secrets.py file
# # try:
# #   from secrets import secrets
# # except ImportError:
# #   print("WiFi secrets are kept in secrets.py, please add them there!")
# #   raise
# # # Debug Level
# # # Change the Debug Flag if you have issues with AT commands
# # debugflag = True
# debugflag = True

# if board.board_id == "challenger_rp2040_wifi_ble":
#   RX = board.ESP_RX
#   TX = board.ESP_TX
#   resetpin = DigitalInOut(board.WIFI_RESET)
#   rtspin = False
#   uart = busio.UART(TX, RX, baudrate=11520, receiver_buffer_size=2048)
#   esp_boot = DigitalInOut(board.WIFI_MODE)
#   esp_boot.direction = Direction.OUTPUT
#   esp_boot.value = True
# else:
#   RX = board.ESP_TX
#   TX = board.ESP_RX
#   resetpin = DigitalInOut(board.ESP_WIFI_EN)
#   rtspin = DigitalInOut(board.ESP_CTS)
#   uart = busio.UART(TX, RX, timeout=0.1)
#   esp_boot = DigitalInOut(board.ESP_BOOT_MODE)
#   esp_boot.direction = Direction.OUTPUT
#   esp_boot.value = True

# print("ESP AT commands")
# # For Boards that do not have an rtspin like challenger_rp2040_wifi set rtspin to False.
# esp = adafruit_espatcontrol.ESP_ATcontrol(
#     uart, 115200, reset_pin=resetpin, rts_pin=rtspin, debug=debugflag
# )
# print("Resetting ESP module")
# esp.hard_reset()

# first_pass = True
# while True:
#     try:
#         if first_pass:
#             # Some ESP do not return OK on AP Scan.
#             # See https://github.com/adafruit/Adafruit_CircuitPython_ESP_ATcontrol/issues/48
#             # Comment out the next 3 lines if you get a No OK response to AT+CWLAP
#             print("Scanning for AP's")
#             for ap in esp.scan_APs():
#                 print(ap)
#             print("Checking connection...")
#             # secrets dictionary must contain 'ssid' and 'password' at a minimum
#             print("Connecting...")
#             esp.connect(secrets)
#             print("Connected to AT software version ", esp.version)
#             print("IP address ", esp.local_ip)
#             first_pass = False
#         print("Pinging 8.8.8.8...", end="")
#         print(esp.ping("8.8.8.8"))
#         time.sleep(10)
#     except (ValueError, RuntimeError, adafruit_espatcontrol.OKError) as e:
#         print("Failed to get data, retrying\n", e)
#         print("Resetting ESP module")
#         esp.hard_reset()
#         continue


# import board
# import busio
# import digitalio

# wifi=busio.UART(board.ESP_TX, board.ESP_RX, baudrate=115200, receiver_buffer_size=2048)
# wrst = digitalio.DigitalInOut(board.WIFI_RESET)
# wmde = digitalio.DigitalInOut(board.WIFI_MODE)
# wrst.direction = digitalio.Direction.OUTPUT
# wmde.direction = digitalio.Direction.OUTPUT
# wrst.value = 0
# wmde.value = 1
# wrst.value = 1

# if board.board_id == "challenger_rp2040_wifi_ble":
#   RX = board.ESP_RX
#   TX = board.ESP_TX
#   resetpin = digitalio.DigitalInOut(board.WIFI_RESET)
#   rtspin = False
#   uart = busio.UART(TX, RX, baudrate=11520, receiver_buffer_size=2048)
#   esp_boot = digitalio.DigitalInOut(board.WIFI_MODE)
#   esp_boot.direction = Direction.OUTPUT
#   esp_boot.value = True
# else:
#   RX = board.ESP_TX
#   TX = board.ESP_RX
#   resetpin = digitalio.DigitalInOut(board.ESP_WIFI_EN)
#   rtspin = digitalio.DigitalInOut(board.ESP_CTS)
#   uart = busio.UART(TX, RX, timeout=0.1)
#   esp_boot = digitalio.DigitalInOut(board.ESP_BOOT_MODE)
#   esp_boot.direction = Direction.OUTPUT
#   esp_boot.value = True

# # For Boards that do not have an rtspin like challenger_rp2040_wifi_ble set rtspin to False.
# from adafruit_espatcontrol import adafruit_espatcontrol

# esp = adafruit_espatcontrol.ESP_ATcontrol(uart, 115200, reset_pin=resetpin, rts_pin=rtspin, debug=debugflag)
# print("Resetting ESP module")
# esp.hard_reset()

# import asyncio
# import board
# import digitalio

# # import socketpool
# # import wifi
# # from adafruit_httpserver import Server, Request, Response

# # AP_SSID = "..."
# # AP_PASSWORD = "..."

# # print("Creating access point...")
# # wifi.radio.start_ap(ssid=AP_SSID, password=AP_PASSWORD)
# # print(f"Created access point {AP_SSID}")

# # pool = socketpool.SocketPool(wifi.radio)
# # server = Server(pool, "/static", debug=True)

# # @server.route("/")
# # def base(request: Request):
# #     return Response(request, "...")

# # server.serve_forever(str(wifi.radio.ipv4_address_ap))

# async def blink(pin, interval):  # Don't forget the async!
#   with digitalio.DigitalInOut(pin) as led:
#     led.switch_to_output(value=False)
#     # led.direction = digitalio.Direction.OUTPUT
#     while True:
#       led.value = True
#       await asyncio.sleep(interval)  # Don't forget the await!
#       led.value = False
#       await asyncio.sleep(interval)  # Don't forget the await!

# async def main():  # Don't forget the async!
#   print("starting server and blinking task")
#   led_task = asyncio.create_task(blink(board.LED, 0.25))
#   await asyncio.gather(led_task)  # Don't forget the await!
#   print("done")

# asyncio.run(main())
