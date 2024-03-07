from manim import *
from math import *

# manim .\tailor.py -pql

class TailorApprox(Scene):

    def f(self, x, n):
        sum = 0
        for i in range(n):
            sum+=(-1)**i/factorial(i)*x**(2*i)
        return sum

    def construct(self):

        self.iterations = 4
        # self.camera.background_color = GREY_A

        ax = Axes(
            x_range=np.array([-8, 8, 2]),
            y_range=np.array([-4, 4, 2]),
            x_length=13,
            y_length=7,
            axis_config={
                'color': WHITE,
                'stroke_width': 1,
                'include_numbers': False,
                'decimal_number_config': {
                    'num_decimal_places': 0,
                    'include_sign': True,
                    'color': WHITE
                }
            },

        )

        function_name = Tex("$ f(x) = e^{-x^2} $").scale(0.8).shift(2*RIGHT+3*DOWN/5)

        count = MathTex("n =", r"0").to_edge(LEFT+DOWN)

        graph = ax.plot(lambda x: e ** (-x ** 2), x_range=[-10, 10], use_smoothing=True, color=BLUE)

        graphs = VGroup()

        for i in range(self.iterations):
            graphs.add(ax.plot(lambda x: self.f(x, i+1), x_range=[-10, 10], use_smoothing=True, color=PINK))

        self.play(Create(ax))
        self.play(Create(graph))
        self.play(Write(count))
        self.play(Create(function_name))

        self.wait()

        self.play(Create(graphs[0]))
        self.wait()

        for i in range(1, self.iterations):
            k = Transform(count[1], Tex(f"${str(i)}$").next_to(count[0], RIGHT).shift(0.01*UP))
            self.play(Transform(graphs[i-1], graphs[i]), k, run_time=1/i)
            if i >= 2:
                self.play(FadeOut(graphs[i-2]), run_time=1/i**0.5)

        self.wait(3)
        self.play(FadeOut(function_name))
        # x_min must be > 0 because log is undefined at 0.
