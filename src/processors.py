from typing import List

import esper
import pygame

from components import Renderable, Link, EntityStat
from ui import Bar


class RenderProcessor(esper.Processor):
    def __init__(self, surface: pygame.Surface, clear_color: List[int]=(0, 0, 0)) -> None:
        super(RenderProcessor, self).__init__()
        self.surface: pygame.Surface = surface
        self.clear_color: List[int] = clear_color

    def process(self) -> None:
        self.surface.fill(self.clear_color)
        for entity, rend in self.world.get_component(Renderable):
            self.surface.blit(rend.image, (rend.x, rend.y))

        for entity, (bar, link) in self.world.get_components(Bar, Link):
            stat: EntityStat = self.world.component_for_entity(entity=link.entity, component_type=link.component)
            bar.image.fill(bar.bg_color)
            pygame.draw.rect(bar.image, bar.fg_color, (0, 0, int((stat.current/stat.maximum)*bar.width), bar.height))
            self.surface.blit(bar.image, (bar.x_pos, bar.y_pos))
        pygame.display.flip()
