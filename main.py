from manim import *
from math import *

class SquarePyramidScene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi= 60 * DEGREES, theta= -55 * DEGREES)
        self.move_camera(zoom=0.4)
        A = [6, 3, 7]
        B = [-5, -4, 8]
        C = [2, 3, 1]
        D = [4, 1, -2]
        vertex_coords = [
            A, B, C, D
        ]
        faces_list = [
            [0, 1, 2],
            [1, 2, 3],
            [2, 3, 0],
            [3, 0, 1],
        ]
        
        # self.move_camera(phi=75 * DEGREES, theta=50 * DEGREES)

        # TODO: сделать текст в 2д так, чтобы он был прикреплён к точками!
        pyramid = Polyhedron(vertex_coords, faces_list)
        A_label = always_redraw(lambda: Tex("A").next_to(pyramid.graph[0], RIGHT).scale(2))
        B_label = always_redraw(lambda: Tex("B").next_to(pyramid.graph[1], RIGHT).scale(2))
        C_label = always_redraw(lambda: Tex("C").next_to(pyramid.graph[2], RIGHT).scale(2))
        D_label = always_redraw(lambda: Tex("D").next_to(pyramid.graph[3], RIGHT).scale(2))
        

        task_description = Tex(r"\textbf{Вариант 8 - задача 2}\ \\ Боковые грани треугольной пирамиды SABC заданы уравнениями:",
        r"\begin{enumerate} \item $3x+6y-2z-22=0$ \item $5x-y+4z-11=0$ \item $65x-101y+8z-143=0$ \item $3x-5y-2z+11=0$ (основание) \end{enumerate}",
        r"Точки E, F, G - центры боковых граней, H - основание высоты, опущенной из вершины S на основание пирамиды.",
        r"\\ Найти объём пирамиды HEFG""").scale(0.6).set_color(GOLD_A)

        self.add_fixed_in_frame_mobjects(task_description)
        self.add(task_description)
        self.play(Write(task_description))
        self.wait()
        self.play(FadeOut(task_description))        

        labels = VGroup(A_label, B_label, C_label, D_label)
        for item in labels:
            item.rotate(-PI)
        
        main_scene = VGroup(axes, pyramid, A_label, B_label, C_label, D_label).move_to(0.1*DOWN)
        self.begin_ambient_camera_rotation(rate=0.1) 
        self.play(FadeIn(axes), FadeIn(pyramid), FadeIn(labels), run_time=0.1)
        self.wait(2)
        self.stop_ambient_camera_rotation()

        self.play(main_scene.animate.move_to(8*LEFT+3*DOWN)) 


        solution = Tex(r"\textbf{Решение}").to_edge(RIGHT, buff=2)
        self.add_fixed_in_frame_mobjects(solution)
        solution_description = Tex(r"...").next_to(solution, DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(solution_description)
        self.play(Write(solution))
        self.play(Write(solution_description))
        self.wait(3)
        self.play(FadeOut(main_scene), FadeOut(solution), FadeOut(solution_description))
        self.wait()