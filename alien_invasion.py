import sys
import pygame

class AlienInvasion:
    #overall class to manage game assets and behavior

    def __init__(self):
        #initialize game
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        background = input("What color would you like?: ")
        self.screen.fill(background)
        pygame.display.update()
        pygame.display.set_caption('Alien Invasion')
    def run_game(self):
        #start the main loop
        while True:
            #watch for keybord and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   sys.exit()
            #make recent screen visible
            pygame.display.flip()
if __name__=='__main__':
   #make a game instance and run the game
   ai = AlienInvasion()
   ai.run_game()