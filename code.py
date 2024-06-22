import board
import neopixel
import touchio

from util import ActiveBoard, ColorNameAnimation


def main():
    touch = touchio.TouchIn(board.TOUCH1)
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 4)

    ab = ActiveBoard(pixels)

    animation = ColorNameAnimation(["red", "blue", "purple", "green"], 3, 4)

    ab.play_animation(animation)

    # pixels[0] = COLORS["red"]
    # pixels[1] = COLORS["blue"]
    # pixels[2] = COLORS["purple"]
    # pixels[3] = COLORS["magenta"]

    # while True:
    #     print(pixels[0])
    #     time.sleep(1)


if __name__ == "__main__":
    main()
