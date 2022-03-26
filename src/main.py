import pygame
import esper

from components import HealthStat, HungerStat, SanityStat, ReputationStat
from global_vars import FPS, RESOLUTION, FONT
from processors import RenderProcessor, BarProcessor
from spritesheet import Fontsheet
from ui import ShortText, UI


# Core
class App:
    def __init__(self) -> None:
        self.running = False
        self.clock = pygame.time.Clock()

        self.screen_size = RESOLUTION
        self.screen = pygame.display.set_mode(size=self.screen_size)

        self.world = esper.World()
        self.world.add_processor(BarProcessor())
        self.world.add_processor(RenderProcessor(surface=self.screen))

        self.fontsheet = Fontsheet(filename="res/font_sheet_2.png", tile_size=10, font_string=FONT)

        self.player = self.world.create_entity(
            ShortText(text="@", font=self.fontsheet, x_pos=30, y_pos=30).as_renderable(),
            HealthStat(current=50, maximum=120),
            HungerStat(current=50, maximum=300),
            SanityStat(current=50, maximum=400),
            ReputationStat(current=50, maximum=100)
        )

        self.ui = UI(player=self.player, font=self.fontsheet, world=self.world)
        self.ui.add_bars()

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        self.world.component_for_entity(self.player, HealthStat).current += 10
                    if event.key == pygame.K_e:
                        self.world.component_for_entity(self.player, HealthStat).current -= 10
            self.world.process()


if __name__ == '__main__':
    App().run()
