from typing import List

import esper
import pygame

from global_vars import TILE_SIZE, active_colors
from components import Renderable, Link, HealthStat, HungerStat, SanityStat, ReputationStat
from spritesheet import Fontsheet


class UI:
    def __init__(self, player: int, font: Fontsheet, world: esper.World) -> None:
        self.player = player
        self.fontsheet = font
        self.world = world

    def add_bars(self) -> None:
        x = 685
        y = 5
        self.world.create_entity(
            Bar(width=50, height=6, bg_color=active_colors["bar_dark"],
                fg_color=active_colors["bar_bright"], x_pos=x + 40, y_pos=y + 2),
            ShortText(text="HP", font=self.fontsheet, x_pos=x + 10, y_pos=y).as_renderable(),
            Link(entity=self.player, component=HealthStat)
        )

        x += 100
        self.world.create_entity(
            Bar(width=50, height=6, bg_color=active_colors["bar_dark"],
                fg_color=active_colors["bar_bright"], x_pos=x + 40, y_pos=y + 2),
            ShortText(text="HNG", font=self.fontsheet, x_pos=x, y_pos=y).as_renderable(),
            Link(entity=self.player, component=HungerStat)
        )

        x += 100
        self.world.create_entity(
            Bar(width=50, height=6, bg_color=active_colors["bar_dark"],
                fg_color=active_colors["bar_bright"], x_pos=x + 40, y_pos=y + 2),
            ShortText(text="SAN", font=self.fontsheet, x_pos=x, y_pos=y).as_renderable(),
            Link(entity=self.player, component=SanityStat)
        )

        x += 100
        self.world.create_entity(
            Bar(width=50, height=6, bg_color=active_colors["bar_dark"],
                fg_color=active_colors["bar_bright"], x_pos=x + 40, y_pos=y + 2),
            ShortText(text="REP", font=self.fontsheet, x_pos=x, y_pos=y).as_renderable(),
            Link(entity=self.player, component=ReputationStat)
        )


class ShortText:
    def __init__(self, text: str, font: Fontsheet, x_pos: int, y_pos: int) -> None:
        self.image: pygame.Surface = pygame.Surface([len(text) * TILE_SIZE, TILE_SIZE])
        self.font = font
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos

        for index, letter in enumerate(text):
            self.image.blit(font.get_char(letter), (index*TILE_SIZE, 0))

    def as_renderable(self) -> Renderable:
        return Renderable(self.image, self.x_pos, self.y_pos)


class Bar:
    def __init__(self, width: int, height: int, fg_color: List[int], bg_color: List[int],
                 x_pos: int, y_pos: int) -> None:
        self.image: pygame.Surface = pygame.Surface([width, height])
        self.image.fill(bg_color)
        self.width = width
        self.height = height
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.x_pos = x_pos
        self.y_pos = y_pos

    def as_renderable(self) -> Renderable:
        return Renderable(self.image, self.x_pos, self.y_pos)
