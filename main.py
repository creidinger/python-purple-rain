import sys
import pygame
from pygame.sprite import Group

from settings import Settings
import game_functions as gf
from droplet import Droplet


def rain():
    # Init the game and create a screen object
    pygame.init()
    r_settings = Settings()
    screen = pygame.display.set_mode(
        (r_settings.screen_width, r_settings.screen_height))
    pygame.display.set_caption("Purple Rain")
    print('rain(): pygame window init...')

    raindrops = Group()
    gf.create_raindrops(r_settings, screen, raindrops)

    # start the main loop of the game
    while True:
        gf.check_events()

        # refresh the screen
        gf.update_screen(r_settings, screen, raindrops)
        # update the position of each raindrop
        for drop in raindrops:
            drop.update()
            if drop.check_bottom(r_settings):
                raindrops.remove(drop)
                gf.create_raindrops(r_settings, screen, raindrops)


if __name__ == "__main__":
    rain()
