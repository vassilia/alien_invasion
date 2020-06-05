import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    #overall class to manage game assets and behavior

    def __init__(self):
        #initialize game
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_height, self.settings.screen_width))
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

    def run_game(self):
        #start the main loop
        while True:
            #watch for keybord and mouse events
            self._check_events()
            self._update_screen()
            self.ship.update()

    def _check_events(self):
        #respond to keyboard press nd mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        # update images on screen & redraw screen with bg_color
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # make recent screen visible
        pygame.display.flip()


if __name__=='__main__':
   #make a game instance and run the game
   ai = AlienInvasion()
   ai.run_game()