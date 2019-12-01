import sys
import pygame

from droplet import Droplet


def check_events():
    """Check for events in the game window"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print('check_events(): ESC key pressed, quitting game')
                pygame.QUIT
                sys.exit()

def update_screen(r_settings, screen, raindrops):
    """Redraw the entire screen"""

    screen.fill(r_settings.bg_color)
    for drop in raindrops.sprites():
        drop.draw_raindrop()
    pygame.display.flip()

def create_raindrops(r_settings, screen, raindrops):
    """Make a raindrop if the nubmer of raindrops hasn't been reached"""
    # this is also used to recycle the raindrops that fall off the screen
    try:
        while len(raindrops) != r_settings.number_raindrops:
            new_raindrop = Droplet(r_settings, screen)
            raindrops.add(new_raindrop)
    except Exception as e:
        print(e)
