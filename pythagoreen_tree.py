from manim import *
from math import *
import math
class tree(Scene):
    n = 5
    def do_step_recursion(self, original_sq, steps, width, angle, angle1, group, animate):
        if steps==self.n:
            return
        UR = original_sq.get_center()+np.array([width/sqrt(2)*cos(angle+pi/4), width/sqrt(2)*sin(angle+pi/4), 0])
        current_scale = sin(angle1)
        square1 = original_sq.copy().scale(sqrt(1-current_scale*current_scale), about_point=UR).rotate(-angle1-pi/2, about_point=UR)
        if animate: self.play(TransformFromCopy(original_sq, square1), run_time=0.5/steps)
        self.do_step_recursion(square1, steps+1, width*sqrt(1-current_scale*current_scale), angle-angle1, angle1, group, animate)
        group.add(square1)
        UL = original_sq.get_center()+np.array([width/sqrt(2)*cos(angle+pi-pi/4), width/sqrt(2)*sin(angle+pi-pi/4), 0])
        square2 = original_sq.copy().scale(current_scale, about_point=UL).rotate((pi/2-angle1)+pi/2, about_point=UL)
        if animate: self.play(TransformFromCopy(original_sq, square2), run_time=0.5/steps)
        group.add(square2)
        self.do_step_recursion(square2, steps+1, width*current_scale, angle+(pi/2-angle1), angle1, group, animate)
        # square2 = original_sq.copy().scale(sqrt(3)/2, about_point=UL).rotate(pi/2+pi/6, about_point=UL)
        # self.play(Write(square2))
        # self.do_step_recursion(square2.copy(), steps+1)
    
    def fractal(self, start_width, start_angle, animate):
        
        square = Square(side_length=start_width).to_edge(DOWN).set_color("#1AB3D5")
        squares = VGroup(square)
        if animate: 
            start = Square(side_length=5)
            self.play(FadeIn(start))
            self.wait(1)
            self.play(Transform(start, square))
            squares.add(start)
        self.do_step_recursion(square, 1, start_width, 0, start_angle, squares, animate)
        if animate:
            self.wait(2)
            self.play(FadeOut(squares, target_position = 3*DOWN))
            return None
        return squares

    def construct(self):
        fiit_blue = "#1AB3D5"
        fiit_purple = "#A30CFF"
        fiit_black_blue = "#03081B"
        fiit_pink = "#FE25A7"
        fiit_neutral_blue = "#110F2C"
        self.camera.background_color = fiit_neutral_blue
        pi = 3.14159265358979323846264338327950288419716939937510
        start_width = 1.4
        start_angle = pi/6

        
    

        # point = square.get_center()+np.array([start_width/sqrt(2)*cos(start_angle-pi/2), start_width/sqrt(2)*sin(start_angle-pi/2), 0])
        square = Square(side_length=5)
        A = ValueTracker(pi/6)
        self.fractal(1, pi/3, True)
        self.n=5
        v = self.fractal(1, pi/3, False)
        self.n=10
        v = always_redraw(lambda: self.fractal((1 - abs(pi/2*3/5-A.get_value()))*2, A.get_value(), False))
        
        self.play(FadeIn(v), run_time=2)
        self.play(A.animate.set_value(pi/2*3/5),run_time=5)
        self.wait(0.5)
        self.play(A.animate.set_value(pi/6),run_time=3)
        self.wait(0.5)
        self.play(A.animate.set_value(pi/2*3/5),run_time=5)
        self.wait(1)
        self.play(FadeOut(v, target_position=3*DOWN), run_time=1.5)
        #  manim .\pythagoreen_tree.py -p -ql