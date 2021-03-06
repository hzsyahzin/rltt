from typing import List

import esper
import pygame

from components import Renderable, Link, VariableStat, Status
from ui import Bar


class BarProcessor(esper.Processor):
    def process(self, *args, **kwargs):
        for entity, (rend, bar, link) in self.world.get_components(Renderable, Bar, Link):
            stat: VariableStat = self.world.component_for_entity(
                entity=link.entity, component_type=Status).stats[link.component.name]
            rend.image.fill(bar.bg_color)
            pygame.draw.rect(rend.image, bar.fg_color, (0, 0, int((stat.current/stat.maximum)*rend.width), rend.height))


class RenderProcessor(esper.Processor):
    def __init__(self, surface: pygame.Surface, clear_color: List[int]=(40, 40, 40)) -> None:
        super(RenderProcessor, self).__init__()
        self.surface: pygame.Surface = surface
        self.clear_color: List[int] = clear_color

    def process(self, *args, **kwargs) -> None:
        self.surface.fill(self.clear_color)
        for entity, rend in self.world.get_component(Renderable):
            self.surface.blit(rend.image, (rend.x_pos, rend.y_pos))
        pygame.display.flip()
