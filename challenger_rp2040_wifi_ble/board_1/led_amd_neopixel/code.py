# import _asyncio as asyncio
import asyncio
import board
import neopixel
from digitalio import DigitalInOut, Direction
from rainbowio import colorwheel
import time

async def blink_neopixel():
    with neopixel.NeoPixel(board.NEOPIXEL, 1) as pixel:
        pixel.brightness = 0.16
        while True:
            for color_value in range(255):
                await asyncio.sleep(0.001)
                pixel[0] = colorwheel(color_value)
                await asyncio.sleep(0.001)

async def blink_led():
    with DigitalInOut(board.LED) as led:
        led.direction = Direction.OUTPUT
        while True:
            led.value = True
            await asyncio.sleep(1)
            led.value = False
            await asyncio.sleep(1)

async def main():
    blink_led_task = asyncio.create_task(blink_led())
    blink_neopixel_task = asyncio.create_task(blink_neopixel())
    await asyncio.gather(blink_led_task, blink_neopixel_task)

asyncio.run(main())
