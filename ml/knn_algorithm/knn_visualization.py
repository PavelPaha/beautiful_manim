import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random
import time
from threading import Thread


from collections import Counter
import math
from manim import *

config.media_embed = True


class KNN(Scene):
    data_size = 20
    K = 5

    def length(self, a, b):
        x = a.get_x()
        y = a.get_y()
        x1 = b.get_x()
        y1 = b.get_y()
        return (x - x1) ** 2 + (y - y1)**2
    def construct(self):
        x_size = 8
        y_size = 6

        particles = VGroup()
        xs = np.random.normal(0, 1, self.data_size)
        ys = np.random.normal(0, 1, self.data_size)
        rectangle_size = 1
        k_colors = {0: '#9CDCEB', 1: '#9D52B0', 2: '#D03A2D'}
        intro = Tex("KNN")

        self.play(Write(intro, color='#9CDCEB'))
        self.wait()
        self.play(FadeOut(intro, target_position=2*DOWN))

        for i in range(self.data_size):
            particles.add(Dot(color=k_colors[i%3], z_index=3).set_x(xs[i]).set_y(ys[i]))

        self.play(Write(particles))
        rectangles = VGroup()
        for i in range(int(x_size*y_size//(rectangle_size**2))):
            rectangles.add(Rectangle(width=rectangle_size, height=rectangle_size, stroke_width=0, fill_color='#FFFFFF',
                                fill_opacity=0.7, z_index=1))

        rectangles = rectangles.arrange_in_grid(y_size//rectangle_size, x_size//rectangle_size, buff=0)
        self.create_knn_grid(rectangles, particles)
        self.play(Write(rectangles))
        self.wait(2)
        random_sample = self.select_random_sample(particles)
        rectangles = always_redraw(lambda: self.create_knn_grid(rectangles, particles))
        self.play(random_sample.animate.shift(DOWN))
        self.wait()
        self.play(random_sample.animate.rotate(np.pi*7/8))
        self.play(FadeOut(particles))
        self.wait()
        self.play(FadeOut(rectangles))

    def select_random_sample(self, particles):
        random_sample = VGroup()
        for sample in range(self.data_size // 3):
            random_sample.add(particles[random.randint(0, self.data_size - 1)])
        return random_sample

    def create_knn_grid(self, rects, particles):
        for i in range(len(rects)):
            neightbours = []
            for j in range(len(particles)):
                neightbours.append((str(particles[j].get_color()), self.length(rects[i], particles[j])))

            neightbours.sort(key=lambda x: x[1])
            k_neightbours = neightbours[:self.K]
            k_colors = [n[0] for n in k_neightbours]
            c = Counter()
            for r in range(len(k_colors)):
                c[k_colors[r]] += 1
            rects[i].set_color(c.most_common()[0][0])
            # self.play(FadeIn(rects[i]), run_time=0.01)
        return rects

