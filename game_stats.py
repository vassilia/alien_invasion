class GameStats:
    #track statistics of game
    def __init__(self, ai_game):
        #initialize statistics
        self.settings = ai_game.settings
        self.reset_stats()
        #start in inactive state
        self.game_active = False

    def reset_stats(self):
        #initialize statistics that can change during the game
        self.ships_left = self.settings.ship_limit
        self.score = 0
