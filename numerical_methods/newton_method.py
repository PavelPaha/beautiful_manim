import math

import numpy as np
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

        eq = Tex(r' Найдём корень $\displaystyle \sin x + \frac{1}{10} - \frac{7}{5} x^2 = 0$ методом Ньютона').set_color(self.fiit_pink)
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
class BisectionMethodScene(MovingCameraScene):
    iterations = 9
    fiit_blue = "#1AB3D5"
    fiit_purple = "#A30CFF"
    fiit_black_blue = "#03081B"
    fiit_pink = "#FE25A7"
    fiit_neutral_blue = "#110F2C"
    def construct(self):
        # Определение системы координат
        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-20, 10, 4],
            x_length=10,
            y_length=10,
            axis_config={"include_ticks": False, "include_tip": False, "include_numbers": True},
        )
        self.camera.background_color = self.fiit_neutral_blue

        func = Tex(r'$\displaystyle f(x) = \sin x + \frac{1}{10} - \frac{7}{5} x^2$').set_color(self.fiit_pink)

        eq = Tex(
            r' Найдём корень $\displaystyle \sin x + \frac{1}{10} - \frac{7}{5} x^2 = 0$ методом половинного деления').set_color(
            self.fiit_pink)

        self.play(Write(func))
        self.wait(1)
        self.play(Transform(func, eq))
        self.wait(1)
        self.play(FadeOut(func))

        self.play(Create(axes))

        # Определение функции и её графика
        func = lambda x: np.sin(x) + 0.1 - 1.4 * x ** 2
        graph = axes.plot(func)
        self.play(Create(graph))

        # Метод половинного деления (бисекции)
        def bisection(f, a, b, tol=1e-6, max_iter=100):
            iter_count = 0
            while iter_count < max_iter:
                c = (a + b) / 2
                if f(c) == 0 or (b - a) / 2 < tol:
                    return c
                iter_count += 1
                if f(c) * f(a) > 0:
                    a = c
                else:
                    b = c
            return c

        # Нахождение корня уравнения
        a, b = 0, 5
        root = bisection(func, a, b)

        # Создание точек до начала анимации
        dot_a = Dot(color=GRAY_BROWN)
        dot_b = Dot(color=GRAY_BROWN)
        dot_c = Dot(color=self.fiit_pink)
        self.camera.frame.save_state()

        # Добавление точек на сцену
        self.play(Write(dot_a), Write(dot_b), Write(dot_c))

        line_a = DashedLine(axes.c2p(a, axes.y_range[0]), axes.c2p(a, axes.y_range[1]), stroke_color=GREEN_C)
        line_b = DashedLine(axes.c2p(b, axes.y_range[0]), axes.c2p(b, axes.y_range[1]), stroke_color=GREEN_C)
        self.play(Create(line_a), Create(line_b))

        # Подсветка рассматриваемой области графика
        highlighted_area = Rectangle(
            width=2*(axes.x_axis.point_to_number(5) - axes.x_axis.point_to_number(0)),
            height=axes.y_axis.point_to_number(5) - axes.y_axis.point_to_number(-20),
            fill_opacity=0.2,
            fill_color=GRAY_A,
            stroke_opacity=0
        )
        highlighted_area.next_to(axes.c2p(0, -20), direction=RIGHT, buff=0)
        self.play(FadeIn(highlighted_area))



        # Анимация метода половинного деления
        left_boundary = a
        right_boundary = b
        for _ in range(8):  # число итераций
            midpoint = (left_boundary + right_boundary) / 2
            point_a = axes.c2p(left_boundary, func(left_boundary))
            point_b = axes.c2p(right_boundary, func(right_boundary))
            point_c = axes.c2p(midpoint, func(midpoint))

            # Перемещение точек на новые позиции
            dot_a.animate.move_to(point_a)
            dot_b.animate.move_to(point_b)
            dot_c.animate.move_to(point_c)

            self.play(
                AnimationGroup(
                    dot_a.animate.move_to(point_a),
                    dot_b.animate.move_to(point_b),
                    dot_c.animate.move_to(point_c),
                    Transform(highlighted_area, Rectangle(
                        width=2*(axes.x_axis.point_to_number(right_boundary) - axes.x_axis.point_to_number(left_boundary)),
                        height=axes.y_axis.point_to_number(5) - axes.y_axis.point_to_number(-20),
                        fill_opacity=0.2,
                        fill_color=GREEN_A,
                        stroke_opacity=0
                        ).next_to(axes.c2p(left_boundary, -20), direction=RIGHT, buff=0)),
                    Transform(line_a, DashedLine(axes.c2p(left_boundary, axes.y_range[0]), axes.c2p(left_boundary, axes.y_range[1]), stroke_color=YELLOW)),
                    Transform(line_b, DashedLine(axes.c2p(right_boundary, axes.y_range[0]), axes.c2p(right_boundary, axes.y_range[1]), stroke_color=YELLOW)),
                    self.camera.frame.animate.scale(0.9).move_to(dot_c.get_center())
                ), run_time=2
            )

            if func(midpoint) * func(left_boundary) > 0:
                left_boundary = midpoint
            else:
                right_boundary = midpoint

        # Отображение корня уравнения
        approx_root_text = Tex(fr"$x \approx {root:.6f}$", font_size=24).next_to(dot_c, UP/2+RIGHT)
        self.play(Create(approx_root_text))
        self.wait(2)
        self.play(FadeOut(approx_root_text))
        self.wait(2)

