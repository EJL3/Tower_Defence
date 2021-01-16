
import core
import pygame
from modules import *


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(core.AUDIOPATHS['bgm'])
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.25)
    screen = pygame.display.set_mode(core.SCREENSIZE)
    pygame.display.set_caption('Game Animation')

    start_interface = StartInterface(core)
    is_play = start_interface.update(screen)
    if not is_play:
        return

    while True:
        choice_interface = ChoiceInterface(core)
        map_choice, difficulty_choice = choice_interface.update(screen)
        game_interface = GamingInterface(core)
        game_interface.start(screen, map_path=core.MAPPATHS[str(map_choice)], difficulty_path=core.DIFFICULTYPATHS[str(difficulty_choice)])
        end_interface = EndInterface(core)
        end_interface.update(screen)


if __name__ == '__main__':
    main()