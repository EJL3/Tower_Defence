
import sys
import pygame


class MainInterface(pygame.sprite.Sprite):
    def __init__(self, cfg):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(cfg.IMAGEPATHS['start']['start_interface']).convert()
        self.rect = self.image.get_rect()
        self.rect.center = cfg.SCREENSIZE[0] / 2, cfg.SCREENSIZE[1] / 2

    def update(self):
        pass


class PlayButton(pygame.sprite.Sprite):
    def __init__(self, cfg, position=(220, 415)):
        pygame.sprite.Sprite.__init__(self)
        self.image_1 = pygame.image.load(cfg.IMAGEPATHS['start']['play_black']).convert()
        self.image_2 = pygame.image.load(cfg.IMAGEPATHS['start']['play_red']).convert()
        self.image = self.image_1
        self.rect = self.image.get_rect()
        self.rect.center = position

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.image = self.image_2
        else:
            self.image = self.image_1


class QuitButton(pygame.sprite.Sprite):
    def __init__(self, cfg, position=(580, 415)):
        pygame.sprite.Sprite.__init__(self)
        self.image_1 = pygame.image.load(cfg.IMAGEPATHS['start']['quit_black']).convert()
        self.image_2 = pygame.image.load(cfg.IMAGEPATHS['start']['quit_red']).convert()
        self.image = self.image_1
        self.rect = self.image.get_rect()
        self.rect.center = position

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.image = self.image_2
        else:
            self.image = self.image_1


class StartInterface():
    def __init__(self, cfg):
        self.main_interface = MainInterface(cfg)
        self.play_btn = PlayButton(cfg)
        self.quit_btn = QuitButton(cfg)
        self.components = pygame.sprite.LayeredUpdates(self.main_interface, self.play_btn, self.quit_btn)

    def update(self, screen):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.components.update()
            self.components.draw(screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.play_btn.rect.collidepoint(mouse_pos):
                            return True
                        elif self.quit_btn.rect.collidepoint(mouse_pos):
                            return False