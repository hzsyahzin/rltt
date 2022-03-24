from typing import List

import pygame


class Spritesheet(object):
    def __init__(self, filename: str) -> None:
        try:
            self.sheet: pygame.Surface = pygame.image.load(filename).convert()
        except pygame.error:
            print('Unable to load spritesheet image: ' + filename)
            raise SystemExit

    def image_at(self, rectangle: List[int], color_key: List[int]=None) -> pygame.Surface:
        """Loads image from x, y, width, height"""
        rect: pygame.Rect = pygame.Rect(rectangle)
        image: pygame.Surface = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if color_key is not None:
            if color_key == -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key, pygame.RLEACCEL)
        return image


class Fontsheet(Spritesheet):
    def __init__(self, filename: str, tile_size: int, font_string: str) -> None:
        super(Fontsheet, self).__init__(filename)
        self.tile_size: int = tile_size
        self.font_string: str = font_string
        self.font_ref: dict = {}

        self.load_font()

    def load_font(self) -> None:
        """ Loads font from spritesheet using string as reference """
        index: int = 0
        for y in range(6):
            for x in range(self.sheet.get_width() // self.tile_size):
                x_pos = x * self.tile_size
                y_pos = y * self.tile_size
                self.font_ref[self.font_string[index]] = self.image_at([x_pos, y_pos, self.tile_size, self.tile_size])
                index += 1

    def get_char(self, char: str, color: List[int]=None, width: int=None, height: int=None) -> pygame.Surface:
        image: pygame.Surface = self.font_ref[char]
        if color:
            for y in range(image.get_height()):
                for x in range(image.get_width()):
                    if image.get_at((x, y)) == (255, 255, 255, 255):
                        image.set_at((x, y), color)
        if width or height:
            image = pygame.transform.scale(image, (width, height))
        return image
