from typing import List

import pygame
import esper

FPS = 60
RESOLUTION = [1080, 720]
TILE_SIZE = 10
FONT = " !\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{¦}~£"


# Helpers
class Spritesheet(object):
    def __init__(self, filename: str):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error:
            print('Unable to load spritesheet image: ' + filename)
            raise SystemExit

    def image_at(self, rectangle: List[int], color_key: List[int]=None):
        """Loads image from x, y, width, height"""
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if color_key is not None:
            if color_key == -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key, pygame.RLEACCEL)
        return image


class Fontsheet(Spritesheet):
    def __init__(self, filename: str, tile_size: int, font_string: str):
        super(Fontsheet, self).__init__(filename)
        self.tile_size = tile_size
        self.font_string = font_string
        self.font_ref = {}

        self.load_font()

    def load_font(self):
        index = 0
        for y in range(6):
            for x in range(self.sheet.get_width() // self.tile_size):
                x_pos = x * self.tile_size
                y_pos = y * self.tile_size
                self.font_ref[self.font_string[index]] = self.image_at([x_pos, y_pos, self.tile_size, self.tile_size])
                index += 1

    def get_char(self, char: str, color: List[int]=None, width: int=None, height: int=None):
        image: pygame.Surface = self.font_ref[char]
        if color:
            for y in range(image.get_height()):
                for x in range(image.get_width()):
                    if image.get_at((x, y)) == (255, 255, 255, 255):
                        image.set_at((x, y), color)
        if width or height:
            image = pygame.transform.scale(image, (width, height))
        return image


# Components
class Renderable:
    def __init__(self, image: pygame.Surface, x_pos: int, y_pos: int):
        self.image = image
        self.x = x_pos
        self.y = y_pos
        self.width = image.get_width()
        self.height = image.get_height()


def ShortText(text: str, font: Fontsheet, x_pos: int, y_pos: int, color: List[int]=(255, 255, 255)):
    renderable = Renderable(pygame.Surface([len(text) * TILE_SIZE, TILE_SIZE]), x_pos, y_pos)
    for index, letter in enumerate(text):
        renderable.image.blit(font.get_char(letter, color=color), (index * TILE_SIZE, 0))
    return renderable


def Rectangle(width: int, height: int, color: List[int], x_pos: int, y_pos: int):
    renderable = Renderable(pygame.Surface([width, height]), x_pos, y_pos)
    renderable.image.fill(color)
    return renderable


# Processors
class RenderProcessor(esper.Processor):
    def __init__(self, surface: pygame.Surface, clear_color: List[int]=(0, 0, 0)):
        super(RenderProcessor, self).__init__()
        self.surface = surface
        self.clear_color = clear_color

    def process(self):
        self.surface.fill(self.clear_color)
        for ent, rend in self.world.get_component(Renderable):
            self.surface.blit(rend.image, (rend.x, rend.y))
        pygame.display.flip()


# Core
class App:
    def __init__(self):
        self.running = False
        self.clock = pygame.time.Clock()

        self.screen_size = RESOLUTION
        self.screen = pygame.display.set_mode(self.screen_size)

        self.world = esper.World()
        self.world.add_processor(RenderProcessor(surface=self.screen))

        self.fontsheet = Fontsheet("res/font_sheet_2.png", 10, FONT)
        self.world.create_entity(ShortText("Hello World!", self.fontsheet, 10, 10))

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
