
import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type, cfg):
        assert enemy_type in range(4)
        pygame.sprite.Sprite.__init__(self)
        self.enemy_type = enemy_type
        self.imagepaths = [cfg.IMAGEPATHS['game']['enemy_yellow'], cfg.IMAGEPATHS['game']['enemy_red'], cfg.IMAGEPATHS['game']['enemy_pink'], cfg.IMAGEPATHS['game']['enemy_blue']]
        self.image = pygame.image.load(self.imagepaths[enemy_type])
        self.rect = self.image.get_rect()

        self.reached_path = []
        self.cell_move_dis = 0

        self.coord = 3, 2
        self.position = 60, 40
        self.rect.left, self.rect.top = self.position
        if enemy_type == 0:

            self.max_life_value = 20

            self.life_value = 20

            self.speed = 2

            self.reward = 100

            self.damage = 1
        elif enemy_type == 1:
            self.max_life_value = 40
            self.life_value = 40
            self.speed = 1
            self.reward = 200
            self.damage = 1
        elif enemy_type == 2:
            self.max_life_value = 60
            self.life_value = 60
            self.speed = 0.5
            self.reward = 300
            self.damage = 2
        elif enemy_type == 3:
            self.max_life_value = 100
            self.life_value = 100
            self.speed = 0.2
            self.reward = 500
            self.damage = 4

    def move(self, cell_len):
        is_next_cell = False
        self.cell_move_dis += self.speed
        if self.cell_move_dis > cell_len:
            self.cell_move_dis = 0
            is_next_cell = True
        return is_next_cell