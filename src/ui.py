from typing import List

import esper
import pygame

from global_vars import RESOLUTION, TILE_SIZE, active_colors
from components import Renderable, Link, HealthStat, HungerStat, SanityStat, ReputationStat, Details
from spritesheet import Fontsheet


class UI:
    def __init__(self, player: int, font: Fontsheet, world: esper.World) -> None:
        self.player = player
        self.fontsheet = font
        self.world = world

        self.world.create_entity(
            Renderable(image=Rectangle(width=RESOLUTION[0], height=20).as_surface(), x_pos=0, y_pos=0))

    def add_status(self) -> None:
        details = self.world.component_for_entity(self.player, Details)
        self.world.create_entity(
            ShortText("12:45 AM", font=self.fontsheet, x_pos=5, y_pos=5).as_renderable())

    def add_bars(self) -> None:
        stats = [HealthStat, HungerStat, SanityStat, ReputationStat]
        x, y = RESOLUTION[0] - 55, 5
        for stat in reversed(stats):
            self.world.create_entity(
                Renderable(image=Rectangle(width=50, height=6).as_surface(), x_pos=x, y_pos=y + 2),
                Bar(bg_color=active_colors["bar_dark"], fg_color=active_colors["bar_bright"]),
                Link(entity=self.player, component=stat))
            label = ShortText(text=stat.abbreviation, font=self.fontsheet, x_pos=x, y_pos=y).as_renderable()
            label.x_pos -= label.width + 5
            self.world.create_entity(label)
            x -= 65 + label.width


class Rectangle:
    def __init__(self, width: int, height: int, color: List[int]=(0, 0, 0)):
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

    def as_surface(self):
        return self.image


class ShortText:
    def __init__(self, text: str, font: Fontsheet, x_pos: int, y_pos: int) -> None:
        self.image: pygame.Surface = pygame.Surface([len(text) * TILE_SIZE, TILE_SIZE])
        self.font = font
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos

        for index, letter in enumerate(text):
            self.image.blit(font.get_char(letter), (index*TILE_SIZE, 0))

    def as_renderable(self, scale=1) -> Renderable:
        return Renderable(self.image, self.x_pos, self.y_pos, scale=scale)


class Bar:
    def __init__(self, fg_color: List[int], bg_color: List[int]) -> None:
        self.fg_color = fg_color
        self.bg_color = bg_color
