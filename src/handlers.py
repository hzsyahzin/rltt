import esper
import pygame

from components import Renderable, Status


class WorldEventHandler:
    def __init__(self, player: int, world: esper.World):
        self.player = player
        self.world = world

    def handle(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.world.component_for_entity(self.player, Renderable).y_pos += -20
            if event.key == pygame.K_a:
                self.world.component_for_entity(self.player, Renderable).x_pos += -20
            if event.key == pygame.K_r:
                self.world.component_for_entity(self.player, Renderable).y_pos += 20
            if event.key == pygame.K_s:
                self.world.component_for_entity(self.player, Renderable).x_pos += 20
            if event.key == pygame.K_SPACE:
                self.world.component_for_entity(self.player, Status).stats["hunger"].current += -20
