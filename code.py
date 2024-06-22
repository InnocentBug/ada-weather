# import board
# import neopixel

from util import ActiveBoard, ColorNameAnimation, StormAnimation


def main():
    # pixels = neopixel.NeoPixel(board.NEOPIXEL, 4)
    # ab = ActiveBoard(pixels)
    ab = ActiveBoard(None)

    animation = ColorNameAnimation(["red", "blue", "purple", "green"], 3, 4)

    animation = StormAnimation(10.0)

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
