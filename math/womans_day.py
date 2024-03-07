from manim import *


class WomansDay(Scene):
    def construct(self):
        # config.tex_compiler = "latex"
        # config.tex_template = TEX_TEMPLATE_WITH_DOCUMENT_CLASS

        text = Text("1231")
        self.play(Write(text))
