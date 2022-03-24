from typing import List

import pygame

from globals import TILE_SIZE
from components import Renderable
from spritesheet import Fontsheet


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
