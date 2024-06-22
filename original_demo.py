import time

import board
import neopixel
import touchio

touch = touchio.TouchIn(board.TOUCH1)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 4)

# Color palette with a wider range of colors
colors = [
    (255, 0, 0),  # Red
    (255, 128, 0),  # Orange
    (255, 255, 0),  # Yellow
    (128, 255, 0),  # Lime
    (0, 255, 0),  # Green
    (0, 255, 128),  # Spring green
    (0, 255, 255),  # Cyan
    (0, 128, 255),  # Sky blue
    (0, 0, 255),  # Blue
    (128, 0, 255),  # Purple
    (255, 0, 255),  # Magenta
]

counter = 0
last_pad_touched = False
add = 1

while True:
    for i in range(4):
        if counter % 4 == i:
            pixels[i] = colors[counter]
        else:
            pixels[i] = (0, 0, 0)
    counter = (counter + len(colors) + add) % len(colors)
    if touch.value:
        if not last_pad_touched:
            add *= -1
        last_pad_touched = True
    else:
        last_pad_touched = False
    time.sleep(0.15)
    pixels.brightness = 0.2


# while True:
#     pixels[0] =
#     print(pixels.fill((255, 100, 500)))


# while True:
#     if touch.value:
#         print("Pad touched!")
#     time.sleep(0.1)

#     # fill with red
#     print(pixels.fill((100, 0, 0)))
#     # sleep for 0.5 seconds
#     # time.sleep(0.5)

#     # fill with green
#     pixels.fill((0, 100, 0))
#     time.sleep(1)

#     # set the first led to white
#     pixels[0] = (100, 250, 100)

#     # # set the second led to blue
#     # pixels[1] = (0, 0, 255)

#     print("looping")
