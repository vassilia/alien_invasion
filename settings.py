class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_speed = 3
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 1.5
        # self.bullet_width = 30
        # self.bullet_height = 15
        # self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #how quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #initialize the settings that change the level
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #scoring
        self.alien_points = 50

    def increase_speed(self):
        #increase speed settings
        self.speed *= self.speedup_scale
        self.bullet_speed *= self.bullet_speed
        self.alien_speed *= self.speedup_scale