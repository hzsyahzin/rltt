import pygame


class Link:
    def __init__(self, entity: int, component: object):
        self.entity = entity
        self.component = component


class Renderable:
    def __init__(self, image: pygame.Surface, x_pos: int, y_pos: int) -> None:
        self.image: pygame.Surface = image
        self.x_pos: int = x_pos
        self.y_pos: int = y_pos
        self.width: int = image.get_width()
        self.height: int = image.get_height()
        
        
class EntityStat:
    def __init__(self, current: int, maximum: int):
        self.current = current
        self.maximum = maximum


class HealthStat(EntityStat):
    name = "HPT"

    def __init__(self, current: int, maximum: int):
        super(HealthStat, self).__init__(current, maximum)


class HungerStat(EntityStat):
    name = "HNG"

    def __init__(self, current: int, maximum: int):
        super(HungerStat, self).__init__(current, maximum)


class SanityStat(EntityStat):
    name = "SAN"

    def __init__(self, current: int, maximum: int):
        super(SanityStat, self).__init__(current, maximum)


class ReputationStat(EntityStat):
    name = "REP"

    def __init__(self, current: int, maximum: int):
        super(ReputationStat, self).__init__(current, maximum)
