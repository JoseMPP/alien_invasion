import pygame
class Character:
    def __init__(self,ai_game):
        """Initialize the character and set its starting position."""
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        #Load the character image and get its react
        self.image=pygame.image.load('images/big_boy.ico')
        self.rect=self.image.get_rect()
        self.rect.center=self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
