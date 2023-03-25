import math
from manim import *

config.media_embed = True

def derivative(x, delta=0.00001):
    return (f(x+delta) - f(x))/delta
def f(x):
    return math.sin(x) + 0.1 - 1.4 * x * x
def tangent(x, x_0):
    return f(x_0) + derivative(x_0)*(x-x_0)

def tangent_back(x_0):
    return x_0 - f(x_0)/derivative(x_0)
class MethodNewton(MovingCameraScene):
    iterations = 9
    fiit_blue = "#1AB3D5"
    fiit_purple = "#A30CFF"
    fiit_black_blue = "#03081B"
    fiit_pink = "#FE25A7"
    fiit_neutral_blue = "#110F2C"
    def construct(self):
        self.camera.background_color = self.fiit_neutral_blue

        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            tips=False,
            axis_config={"include_numbers": True},
            stroke_width=0.2
            # y_axis_config={"scaling": LogBase(custom_labels=True)},
        )

        graph = ax.plot(lambda x: f(x), x_range=[-5, 5], use_smoothing=True, stroke_width=0.8)
        tangents = VGroup()
        current_x = 2
        root = 0.74

        xi = Tex(fr'').scale(1/2).move_to(np.array([-1.5,1,0]))

        scale_dot = Dot().move_to(np.array([root, f(root), 0]))

        func = Tex(r'$\displaystyle f(x) = \sin x + \frac{1}{10} - \frac{7}{5} x^2$').set_color(self.fiit_pink)

        eq = Tex(r'$\displaystyle \sin x + \frac{1}{10} - \frac{7}{5} x^2 = 0$').set_color(self.fiit_pink)
        self.play(Write(func))
        self.wait(1)
        self.play(Transform(func, eq))
        self.wait(1)
        self.play(FadeOut(func))

        self.camera.frame.save_state()
        self.play(Write(ax))
        self.play(Write(graph))
        self.play(self.camera.frame.animate.move_to(scale_dot))
        self.play(self.camera.frame.animate.scale(1/2))
        self.play(ax.animate.set_stroke(width=0.2))
        self.play(graph.animate.set_stroke(width=0.2))
        self.play(Write(xi))

        pick_dot = Dot(color=self.fiit_pink).scale(0.2).move_to(np.array([100, 0, 0]))
        self.play(Write(pick_dot))
        for i in range(self.iterations):
            tang = ax.plot(lambda x: tangent(x, current_x), x_range=[-5, 5], use_smoothing=False, stroke_width=0.2)
            tangents.add(tang)
            current_x = tangent_back(current_x)
            self.play(Write(tang), run_time=1/(i+1))
            self.play(pick_dot.animate.move_to(np.array([current_x*1.2, 0, 0])), run_time=1/(i+1))
            self.play(FadeOut(xi), run_time=0.2/(i+1))
            xi = Tex(fr'$x_{i+1} \approx {"{0:9f}".format(current_x)}$ \\ $f(x_{i+1}) \approx {"{0:9f}".format(f(current_x))}$').scale(1/2).move_to(np.array([-1.5,1,0]))
            self.play(FadeIn(xi), run_time=0.2/(i+1))
        result = Tex(fr'$x \approx {round(current_x,6)}$').scale(1/10).next_to(scale_dot, LEFT/3+DOWN/20)

        self.wait(1.5)
        self.play(self.camera.frame.animate.scale(1/5), run_time=2)
        self.play(Write(result))
        self.wait(2)
        self.play(FadeOut(result), run_time=0.5)
        self.play(FadeOut(tangents))
        self.play(FadeOut(ax), run_time=0.2)
        self.play(FadeOut(graph), run_time=0.2)
        self.play(FadeOut(xi), run_time=0.1)
        self.play(Restore(self.camera.frame))
        answer = Tex(rf'$x \approx {"{0:6f}".format(current_x)}$').set_color(self.fiit_pink)
        self.play(Transform(pick_dot, answer))
        self.wait()
        self.play(FadeOut(pick_dot, target_position=2*DOWN), run_time=2)
        self.wait()