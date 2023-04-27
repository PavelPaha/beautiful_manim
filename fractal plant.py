import math
import numpy as np
from manim import *

config.media_embed = True
class L_system(Scene):
    def build_plant_string(self, s, n, rule):
        if n==0: return s
        return self.build_plant_string(''.join([rule[i] if i in rule else i for i in s]), n-1, rule)


    def build_dragon(self, n, length, rotate=90):
        rotate = math.radians(rotate)
        fractal = VGroup()
        cursor = 2*LEFT
        angle = 0
        rule = {'X': 'X+YF', 'Y': 'FX-Y'}
        s = self.build_plant_string("A", n, rule)
        for i in s:
            if i == 'F':
                end = [cursor[0] + length * np.cos(angle), cursor[1] + length * np.sin(angle), 0]
                fractal.add(Line(Dot(np.array(cursor)).get_center(), Dot(np.array(end)).get_center()))
                cursor = end
            elif i == '+':
                angle += rotate
            elif i == '-':
                angle -= rotate
        return fractal
    def build_serpinsky(self, n, length, rotate=60):
        rotate = math.radians(rotate)
        fractal = VGroup()
        cursor = 2*LEFT
        angle = 0
        rule = {'A': 'B-A-B', 'B': 'A+B+A'}
        s = self.build_plant_string("A", n, rule)
        for i in s:
            if i == 'A' or i == 'B':
                end = [cursor[0] + length * np.cos(angle), cursor[1] + length * np.sin(angle), 0]
                fractal.add(Line(Dot(np.array(cursor)).get_center(), Dot(np.array(end)).get_center()))
                cursor = end
            elif i == '+':
                angle += rotate
            elif i == '-':
                angle -= rotate
        return fractal
    def build_gosper(self, n, length, rotate=60):
        rotate = math.radians(rotate)
        fractal = VGroup()
        cursor = 3*UP
        angle = 0
        rule = {'F': '', 'L': 'FL-FR--FR+FL++FLFL+FR-', 'R': '+FL-FRFR--FR-FL++FL+FR'}
        s = self.build_plant_string("FL", n, rule)
        for i in s:
            if i == 'F':
                end = [cursor[0] + length * np.cos(angle), cursor[1] + length * np.sin(angle), 0]
                fractal.add(Line(Dot(np.array(cursor)).get_center(), Dot(np.array(end)).get_center()))
                cursor = end
            elif i == '+':
                angle += rotate
            elif i == '-':
                angle -= rotate
        return fractal

    def build_fractal(self, n, length, rotate=25):
        rotate=math.radians(rotate)
        tree = VGroup()
        cursor = 3*DOWN
        angle = math.pi/2
        stack = []
        rule = {'F': 'FF', 'X': 'F[+X]F[-X]+X'}
        s = self.build_plant_string("X", n, rule)
        print(s)
        for i in s:
            if i=='[':
                stack.append([cursor, angle])
            elif i==']':
                cursor, angle = stack.pop()
            elif i=='F':
                end = [cursor[0]+length*np.cos(angle), cursor[1]+length*np.sin(angle), 0]
                tree.add(Line(Dot(np.array(cursor)).get_center(), Dot(np.array(end)).get_center()))
                cursor = end
            elif i=='+':
                angle+=rotate
            elif i=='-':
                angle-=rotate*2/3
        return tree


    def construct(self):
        # print(self.build_plant_string("X", 10))
        # a = ValueTracker(15)
        # length = ValueTracker(0)
        # tr = always_redraw(lambda : self.build_fractal(7, length.get_value(), a.get_value()))
        # self.add(tr)
        # self.play(length.animate.set_value(0.02), run_tume=3)
        # self.wait()
        # self.play(a.animate.set_value(50), run_tume=3)
        # self.wait(2)
        # self.play(a.animate.set_value(90), length.animate.set_value(0), run_tume=3)
        # self.build_fractal(2)
        self.play(FadeIn(self.build_fractal(2, 0.5)))



        # triangles = [self.build_serpinsky(i, 0.24/(i**(3/2))) for i in range(1, 9)]
        # self.play(FadeIn(triangles[0]))
        # for i in range(len(triangles)-1):
        #     self.play(Transform(triangles[0], triangles[i+1]), run_time=2)
        #     self.wait()
        # self.wait(2)
        # self.play(FadeOut(triangles[0], target_position=2*DOWN))


