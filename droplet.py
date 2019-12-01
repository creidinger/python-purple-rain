import pygame
from pygame.sprite import Sprite
import random


class Droplet(Sprite):
    """Class for making raindrops"""

    def __init__(self, r_settings, screen):
        super().__init__()

        self.screen = screen

        # get settings
        self.color = r_settings.rain_color
        self.speed_factor = r_settings.rain_speed_factor
        self.rain_height = r_settings.rain_height
        self.rain_width = r_settings.rain_width
        self.speed_factor_min = r_settings.rain_speed_factor_min

        # get a random value for the x&y start positions
        self.x_start = random.randint(0, r_settings.screen_width)
        self.y_start = random.randint(-1000, 0)
        # This is not in 3d space, I'm using the value to scale down raindrops
        # so they appear to be in the background
        self.z = random.random()

        self.rain_height = self.rain_height * self.z
        self.rain_width = self.rain_width * self.z
        self.speed_factor = self.speed_factor * self.z
        # setting a minimum speed of 70% so the background doesnt fall too slow
        if self.speed_factor < self.speed_factor_min:
            self.speed_factor = self.speed_factor_min

        # create a raindrop
        # Rect(left, top, width, height)
        self.rect = pygame.Rect(
            self.x_start, self.y_start, self.rain_width, self.rain_height)

        # store the raindrops y pos
        self.y = float(self.rect.y)

    def update(self):
        """Move the raindrops to the bottom of the screen"""
        # Update the decimal pos of the raindrop
        self.y += self.speed_factor
        # Update the droplets rect position
        self.rect.y = self.y

    def draw_raindrop(self):
        """Draw the raindrop to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def check_bottom(self, r_settings):
        """Check of the raindrop has passed the bottom of the screen"""

        if self.y > r_settings.screen_height:
            return True
        else:
            return False
