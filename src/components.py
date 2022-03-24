import pygame


class Link:
    def __init__(self, entity: int, component: object):
        self.entity = entity
        self.component = component


class Renderable:
    def __init__(self, image: pygame.Surface, x_pos: int, y_pos: int) -> None:
        self.image: pygame.Surface = image
        self.x: int = x_pos
        self.y: int = y_pos
        self.width: int = image.get_width()
        self.height: int = image.get_height()
        
        
class EntityStat:
    def __init__(self, current: int, maximum: int):
        self.current = current
        self.maximum = maximum
        
        
class HealthStat(EntityStat):
    def __init__(self, current: int, maximum: int):
        super(HealthStat, self).__init__(current, maximum)
