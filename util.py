import random
import time


class Animation:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class State:
    pixel_values: list
    duration: float

    def __init__(self, pixel_values: list, duration: float):
        self.pixel_values = pixel_values
        self.duration = duration

    def __str__(self):
        return f"State {self.pixel_values} {self.duration}"


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


class StormAnimation(Animation):
    quiet_min = 3
    quiet_max = 10
    lightning_duration = 0.5
    lightning_min = 1
    lightning_max = 5
    lightning_break_min = 0.5
    lightning_break_max = 1.5
    storm_color = (64, 70, 84)
    lightning_color_a = (255, 255, 153)
    lightning_color_b = (173, 216, 230)

    def make_sequence(self):
        state_sequence = []

        state_sequence += [
            State(
                [self.storm_color] * 4, random.uniform(self.quiet_min, self.quiet_max)
            )
        ]
        num_lightning = int(random.uniform(self.lightning_min, self.lightning_max + 1))
        print(f"Animating {num_lightning} lightnings")
        for _ in range(num_lightning):
            leds = [
                self.lightning_color_b,
                self.lightning_color_a,
                self.lightning_color_b,
                self.lightning_color_a,
            ]
            state_sequence += [State(leds, self.lightning_duration)]

            leds = [self.storm_color] * 4
            lightning_break = random.uniform(
                self.lightning_break_min, self.lightning_break_max
            )
            state_sequence += [State(leds, lightning_break)]

        [print(str(state)) for state in state_sequence]
        return state_sequence

    def __init__(self, min_duration):
        super().__init__(f"Storm Animation {min_duration}")
        self.min_duration = min_duration
        self._current_sequence = iter(self.make_sequence())
        self._current_duration = 0.0

    def __next__(self):
        if self._current_duration > self.min_duration:
            raise StopIteration
        try:
            next_state = next(self._current_sequence)
            self._current_duration += next_state.duration
            return next_state
        except StopIteration:
            self._current_sequence = iter(self.make_sequence())
            return next(self)

    def __iter__(self):
        self._current_duration = 0
        return self


class ActiveBoard:
    def __init__(self, pixels):
        self.pixels = pixels

    def set_state(self, state):
        for i, p in enumerate(state.pixel_values):
            if self.pixels is not None:
                self.pixels[i] = p
            else:
                print(state)
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
