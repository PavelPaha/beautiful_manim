from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class Permutations(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="ru", tld="com"))

        title = "Перестановки, подстановки, четность, нечетность. Свойства"
        titleTex = Text(title)

        with self.voiceover(text=title) as tracker:
            self.play(Write(titleTex), run_time=tracker.duration)

        self.wait()
