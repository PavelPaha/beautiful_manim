from manim import *
from math import *

class Task3(Scene):
    def construct(self):
        # colors:
        fiit_blue = "#1AB3D5"
        fiit_purple = "#A30CFF"
        fiit_black_blue = "#03081B"
        fiit_pink = "#FE25A7"
        fiit_neutral_blue = "#110F2C"
        self.camera.background_color = fiit_neutral_blue
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 6, 1],
            tips=False,
            axis_config={"include_numbers": True},
            # y_axis_config={"scaling": LogBase(custom_labels=True)},
        )

        # x_min must be > 0 because log is undefined at 0.
        A = ValueTracker(1)
        graph = ax.plot(lambda x: A.get_value()*cos(x))
        self.play(Write(ax))
        self.wait()
        self.play(Write(graph))
        self.play(A.animate.set_value(4),run_time=3)

        self.wait(3)
        