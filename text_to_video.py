from manim import *
#from manim.constants import UP_LEFT

class FiverrVideo(Scene):
    def construct(self):
        # Background color
        self.camera.background_color = "#E0FFFF"  # gradient color

        '''
        # Add logo
        logo = ImageMobject("C:/Users/BRIAn/Pictures/NewVideo/bas.jpg")
        logo.set_width(config.frame_width)
        logo.set_height(config.frame_height)
        self.add(logo)

        '''
        # full screen text overlay
        lines = [
            "Unlock Your Ideas with Professional Patent Solutions!",
            "Let me help you protect your innovations.",
            "Expert drafting, searching, and filing services.",
            "Your journey to intellectual property starts here!"
        ]
        

        text_group = VGroup()

        for i, line in enumerate(lines):
            #to center text and ensure full overlay
            text_line = Text(line, font="Arial", color=BLACK).scale(0.8)
            text_line.move_to(ORIGIN + UP * (2 - i))
            self.play(Write(text_line, run_time=2))  # Write animation
            text_group.add(text_line)

        # Call to action
        cta = Text("Contact Me Today!", font="Arial", color=YELLOW).scale(1.5)
        cta.move_to(DOWN * 2)
        self.play(FadeIn(cta, run_time = 3))
        self.wait(4)
