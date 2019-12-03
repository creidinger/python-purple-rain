class Settings():
    """Settings for puprle rain in pygame"""

    def __init__(self):
        # screen
        self.screen_width = 1200
        self.screen_height = 665
        self.bg_color = (0, 0, 0)
        # controls
        self.exit_btn = "exc"
        # rain settings
        self.rain_height = 20
        self.rain_width = 7
        self.rain_speed_factor = 20
        # set the min fall speed to 75%
        # so the background doesn't fall to slowly
        self.rain_speed_factor_min = self.rain_speed_factor * 0.75
        self.rain_color = (85, 0, 200)
        self.number_raindrops = 800  # the nubmer of raindrops on the screen
