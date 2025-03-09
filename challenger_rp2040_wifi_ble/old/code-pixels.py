print("starting")

import time
import board
from rainbowio import colorwheel
import neopixel

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel.brightness = 0.3

def rainbow(delay):
    for color_value in range(255):
        pixel[0] = colorwheel(color_value)
        time.sleep(delay)

while True:
    rainbow(0.02)

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

print("finished")
