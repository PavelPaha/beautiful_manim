from manim import *
from math import *



class Task3(Scene):
    #  manim .\matan-test-dkr.py -p -ql
    def construct(self):
        # colors:
        fiit_blue = "#1AB3D5"
        fiit_purple = "#A30CFF"
        fiit_black_blue = "#03081B"
        fiit_pink = "#FE25A7"
        fiit_neutral_blue = "#110F2C"
        self.camera.background_color = fiit_neutral_blue
        main_title = Tex(r"""\centering{Задача 3б из домашней контрольной работы

         по математическому анализу

         студентов 1 курса ФИИТ УрФУ}""").scale(0.8)

        task_description = Tex("Доказать по определению:")
        task = Tex(r"$\lim_{n\to \infty} \frac{2n^4+10n}{n^4+6.5} = 2$").set_color(fiit_pink).next_to(task_description, DOWN)

        step1 = Tex(r"$\forall \epsilon > 0\ \exists N(\epsilon)\ \forall n > N(\epsilon)\ |\frac{2n^4+10n}{n^4+6.5} - 2|<\epsilon$").set_color(fiit_pink)
        step2 = Tex(r"$|\frac{2n^4+10n}{n^4+6.5} - 2|$")


        step5 = Tex(r"При $\displaystyle n>1$:")
        step6 = Tex(r"$\displaystyle \frac{10n - 13}{n^4+6.5}>0 \Rightarrow |\frac{10n - 13}{n^4+6.5}| = \frac{10n - 13}{n^4+6.5}$").next_to(step5, DOWN)
        step7 = Tex(r"$\displaystyle \frac{10n - 13}{n^4+6.5} < \frac{10n - 13}{n+6.5}$(уменьшили знаменатель)$<\epsilon$").next_to(step6, DOWN)

        step8 = Tex(r"$10n-13<\epsilon n + 6.5 \epsilon$").shift(2*UP).scale(0.9)
        step9 = Tex(r"$\epsilon n - 10n + 6.5\epsilon + 13 > 0$ (*)").next_to(step8, DOWN).scale(0.9)
        # remove step8 and move step9 to up edge

        step10=Tex(r"$n>\frac{13+6.5\epsilon}{10-\epsilon}$").next_to(step9, DOWN).scale(0.9)
        step11 = Tex(r"""(здесь мы подразумеваем, что $\epsilon \neq 10$, 
        
        так как при таком значении 
        
        неравенство (*) выполняется)""").next_to(step10, DOWN).set_color(fiit_pink).scale(0.8)


        final = Tex(r"$N(\epsilon) = [\frac{13+6.5\epsilon}{10-\epsilon}]+1$")

        self.play(Write(main_title))
        self.wait()
        self.play(Transform(main_title, task_description))
        self.play(Write(task), run_time=0.6)
        self.wait()
        self.play(FadeOut(main_title), FadeOut(task), lag_ratio = 0.4)
        self.wait()
        self.play(FadeIn(step1, target_position=2*UP))
        self.play(step1.animate.scale(0.6), step1.animate.to_edge(UP))
        self.play(Write(step2))
        self.wait()
        self.play(step2.animate.to_edge(LEFT))
        step3 = Tex(r"$= |\frac{2n^4+10n - 2n^4 - 13}{n^4+6.5}|$").next_to(step2, RIGHT)
        step4 = Tex(r"$= |\frac{10n - 13}{n^4+6.5}|$").next_to(step3, RIGHT)
        self.play(TransformFromCopy(step2, step3), run_time=1.5)
        self.wait(2)
        self.play(TransformFromCopy(step3, step4), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(step2), FadeOut(step3), FadeOut(step4))
        self.wait(1)
        self.play(FadeIn(step5, target_position = 2*DOWN))
        self.wait(2)
        self.play(TransformFromCopy(step5, step6))
        self.wait(3)
        self.play(FadeOut(step5), FadeOut(step6))
        self.play(GrowFromCenter(step7))
        self.wait(2)
        self.play(Unwrite(step7))
        self.play(Write(step8))
        self.play(Write(step9))
        self.play(Write(step10))
        self.play(Write(step11))
        self.wait(4)
        self.play(FadeOut(step8), run_time=0.3)
        self.play(FadeOut(step9), run_time=0.3)
        self.play(FadeOut(step10), run_time=0.3)
        self.play(FadeOut(step11), run_time=0.3)
        self.play(Write(final), run_time=2)
        self.play(Indicate(final, color=fiit_blue), run_time=5)
        self.play(FadeOut(final, target_position=DOWN))
        self.play(FadeOut(step1, target_position=UP))
        self.wait(3)

        




