from manim import *
from math import *

class tree(Scene):


    def do_step_recursion(self, original_sq, steps, width, angle, group):
            if steps==7:
                return
            UR = original_sq.get_center()+np.array([width/sqrt(2)*cos(angle+pi/4), width/sqrt(2)*sin(angle+pi/4), 0])
            square1 = original_sq.copy().scale(0.5, about_point=UR).rotate(-pi/3-pi/2, about_point=UR)
            # self.play(TransformFromCopy(original_sq, square1), run_time=0.001)
            self.do_step_recursion(square1, steps+1, width/2, angle-pi/3, group)
            group.add(square1)
            UL = original_sq.get_center()+np.array([width/sqrt(2)*cos(angle+pi-pi/4), width/sqrt(2)*sin(angle+pi-pi/4), 0])
            square2 = original_sq.copy().scale(sqrt(3)/2, about_point=UL).rotate(pi/6+pi/2, about_point=UL)
            # self.play(TransformFromCopy(original_sq, square2), run_time=0.001)
            group.add(square2)
            self.do_step_recursion(square2, steps+1, width*sqrt(3)/2, angle+pi/6, group)
            # square2 = original_sq.copy().scale(sqrt(3)/2, about_point=UL).rotate(pi/2+pi/6, about_point=UL)
            # self.play(Write(square2))
            # self.do_step_recursion(square2.copy(), steps+1)
            

    def construct(self):

        fiit_blue = "#1AB3D5"
        fiit_purple = "#A30CFF"
        fiit_black_blue = "#03081B"
        fiit_pink = "#FE25A7"
        fiit_neutral_blue = "#110F2C"
        self.camera.background_color = fiit_neutral_blue
        pi = 3.14159265358979323846264338327950288419716939937510
        start_width = 1.4

        A = ValueTracker(1)
        square = Square(side_length=start_width).to_edge(DOWN)
        squares = VGroup(square)
        sqs = VGroup(square)
        UR = square.get_right() + square.get_top()
        UL = square.get_left() + square.get_top()

        point = square.get_center()
        # +np.array([start_width/sqrt(2)*cos(pi/6-pi/2), start_width/sqrt(2)*sin(pi/6-pi/2), 0])

        self.do_step_recursion(square, 0, start_width, 0, squares)
        self.play(Write(squares))
        # self.play(A.animate.set_value(4),run_time=3)

        self.play(FadeOut(squares))
        # self.play(Write(sqs))
        

        
        # triangles = VGroup()
        # triangle1 = Tri
        self.wait(3)
        