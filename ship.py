import pygame

class Ship:
    #class to manage the ship
    def __init__(self, ai_game):
        #initialize the ship and its starting position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        #load ship image and rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #Update the ship's position based on the movement flag
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Update rect object from self.x.
        self.rect.x = self.x
    def blitme(self):
        #draw ship at current location
        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        #center ship on the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
