import time


class Animation:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class ColorNameAnimation(Animation):
    def __init__(self, color_names, duration, updates=1):
        super().__init__(f"Color Animation {color_names}")
        self.colors = [COLORS[name] for name in color_names]
        self.duration = duration / updates
        self.updates = updates
        self._counter = 0

    def __next__(self):
        if self._counter >= self.updates:
            raise StopIteration
        self._counter += 1

        state = State(self.colors, self.duration)
        return state

    def __iter__(self):
        self._counter = 0
        return self


class State:
    pixel_values: list
    duration: float

    def __init__(self, pixel_values: list, duration: float):
        self.pixel_values = pixel_values
        self.duration = duration


class ActiveBoard:
    def __init__(self, pixels):
        self.pixels = pixels

    def set_state(self, state):
        for i, p in enumerate(state.pixel_values):
            self.pixels[i] = p
        print(f"sleeping {state.duration}")
        time.sleep(state.duration)

    def play_animation(self, animation):
        print(f"Starting Animation {animation.name}")
        for state in animation:
            self.set_state(state)
        print(f"Ending Animation {animation.name}")


# Color palette with a wider range of colors
COLORS = {
    "red": (255, 0, 0),
    "orange": (255, 128, 0),
    "yellow": (255, 255, 0),
    "lime": (128, 255, 0),
    "green": (0, 255, 0),
    "spring_green": (0, 255, 128),
    "cyan": (0, 255, 255),
    "sky_blue": (0, 128, 255),
    "blue": (0, 0, 255),
    "purple": (128, 0, 255),
    "magenta": (255, 0, 255),
}
