
import pygame
from .arrow import Arrow


class Turret(pygame.sprite.Sprite):
    def __init__(self, turret_type, cfg):
        assert turret_type in range(3)
        pygame.sprite.Sprite.__init__(self)
        self.cfg = cfg
        self.turret_type = turret_type
        self.imagepaths = [cfg.IMAGEPATHS['game']['basic_tower'], cfg.IMAGEPATHS['game']['med_tower'], cfg.IMAGEPATHS['game']['heavy_tower']]
        self.image = pygame.image.load(self.imagepaths[turret_type])
        self.rect = self.image.get_rect()

        self.arrow = Arrow(turret_type, cfg)

        self.coord = 0, 0
        self.position = 0, 0
        self.rect.left, self.rect.top = self.position
        self.reset()

    def shot(self, position, angle=None):
        arrow = None
        if not self.is_cooling:
            arrow = Arrow(self.turret_type, self.cfg)
            arrow.reset(position, angle)
            self.is_cooling = True
        if self.is_cooling:
            self.cool_time -= 1
            if self.cool_time == 0:
                self.reset()
        return arrow

    def reset(self):
        if self.turret_type == 0:

            self.price = 500

            self.cool_time = 30

            self.is_cooling = False
        elif self.turret_type == 1:
            self.price = 1000
            self.cool_time = 50
            self.is_cooling = False
        elif self.turret_type == 2:
            self.price = 1500
            self.cool_time = 100
            self.is_cooling = False