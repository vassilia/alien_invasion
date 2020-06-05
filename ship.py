import pygame
class Ship:
    # class to manage ship
    def __init__(self, ai_game):
        #initialize starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        #load the ship image and its rect
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()
        #start each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        #movement flag
        self.moving_right = False
        self.moving_left = False
    def update(self):
        #Update the ship's position based on the movement flag.
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -=1
    def blitme(self):
        #draw ship at current location
        self.screen.blit(self.image, self.rect)