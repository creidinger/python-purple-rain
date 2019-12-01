class Settings():
    """Settings for puprle rain in pygame"""

    def __init__(self):
        # screen
        self.screen_width = 800
        self.screen_height = 450
        self.bg_color = (0, 0, 0)
        # controls
        self.exit_btn = "exc"
        # rain settings
        self.rain_height = 20
        self.rain_width = 4
        self.rain_speed_factor = 1.5
        self.rain_speed_factor_min = 0.7
        self.rain_color = (85, 0, 200)
        self.number_raindrops = 750 # the nubmer of raindrops on the screen
