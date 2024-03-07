from manim import *


class Mandelbrot(Scene):
    def construct(self):
        x_min, x_max = -2, 0.5
        y_min, y_max = -1.25, 1.25
        max_iter = 256
        colors = ['GOLD', 'RED', 'ORANGE', 'YELLOW', 'GREEN', 'PURPLE', 'BLUE', 'TEAL']

        def color_map(n):
            if n == max_iter:
                return BLACK
            return colors[n % len(colors)]

        d = 0.005
        square = Square(side_length=8, fill_opacity=1, stroke_width=0, color=BLACK)
        square.move_to(ORIGIN)
        xs = np.arange(x_min, x_max, d)
        ys = np.arange(y_min, y_max, d)
        coords = [complex(x, y) for y in ys for x in xs]
        coords_len = len(coords)

        for i, c in enumerate(coords):
            z = c
            n = 0
            while abs(z) <= 2 and n < max_iter:
                z = z ** 2 + c
                n += 1
            dot = Square(side_length=d, fill_opacity=1, stroke_width=0, color=color_map(n))
            dot.move_to(np.array([c.real, c.imag, 0]))
            square.add(dot)

        self.play(Create(square))
