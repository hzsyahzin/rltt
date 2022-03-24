import pygame
import esper

from components import HealthStat, Link
from globals import FPS, RESOLUTION, FONT
from processors import RenderProcessor
from spritesheet import Fontsheet
from ui import ShortText, Bar


# Core
class App:
    def __init__(self) -> None:
        self.running = False
        self.clock = pygame.time.Clock()

        self.screen_size = RESOLUTION
        self.screen = pygame.display.set_mode(size=self.screen_size)

        self.world = esper.World()
        self.world.add_processor(RenderProcessor(surface=self.screen))

        self.fontsheet = Fontsheet(filename="res/font_sheet_2.png", tile_size=10, font_string=FONT)

        self.player = self.world.create_entity(
            ShortText(text="@", font=self.fontsheet, x_pos=30, y_pos=30).as_renderable(),
            HealthStat(current=50, maximum=120)
        )

        health_bar = self.world.create_entity(
            Bar(width=50, height=10, bg_color=[255, 0, 0], fg_color=[0, 255, 0], x_pos=0, y_pos=0),
            Link(entity=self.player, component=HealthStat)
        )

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.world.process()


if __name__ == '__main__':
    App().run()
