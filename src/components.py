import pygame


class Link:
    def __init__(self, entity: int, component: object):
        self.entity = entity
        self.component = component


class Details:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Renderable:
    def __init__(self, image: pygame.Surface, x_pos: int, y_pos: int, scale=1) -> None:
        self.x_pos: int = x_pos
        self.y_pos: int = y_pos
        self.width: float = image.get_width() * scale
        self.height: float = image.get_height() * scale
        self.image: pygame.Surface = pygame.transform.scale(image, [self.width, self.height])


class Status:
    def __init__(self, *stats) -> None:
        self.stats = {}
        for stat in stats:
            self.stats[stat.name] = stat

        
class VariableStat:
    def __init__(self, current: int, maximum: int):
        self.current = current
        self.maximum = maximum


class HealthStat(VariableStat):
    name = "health"
    abbreviation = "HP"

    def __init__(self, current: int, maximum: int):
        super(HealthStat, self).__init__(current, maximum)


class HungerStat(VariableStat):
    name = "hunger"
    abbreviation = "HNG"

    def __init__(self, current: int, maximum: int):
        super(HungerStat, self).__init__(current, maximum)


class SanityStat(VariableStat):
    name = "sanity"
    abbreviation = "SAN"

    def __init__(self, current: int, maximum: int):
        super(SanityStat, self).__init__(current, maximum)


class ReputationStat(VariableStat):
    name = "reputation"
    abbreviation = "REP"

    def __init__(self, current: int, maximum: int):
        super(ReputationStat, self).__init__(current, maximum)
