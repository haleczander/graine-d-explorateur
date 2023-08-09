import pygame
from config import *
from modules.Directions import Directions


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        super().__init__(self.groups)
        
        self.x = TILE_SIZE * (x + .5) - PLAYER_WIDTH / 2
        self.y = TILE_SIZE * y
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.speed = PLAYER_SPEED
               
        self.direction = Directions.DOWN
        self.x_change = 0
        self.y_change = 0
            
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(PLAYER_FILL)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def keyMove(self, key, type):
        offset = 1 if type == pygame.KEYDOWN else -1
        if key == pygame.K_LEFT:
            self.x_change -= offset
            self.direction = Directions.LEFT
        if key == pygame.K_RIGHT:
            self.x_change += offset
            self.direction = Directions.RIGHT
        if key == pygame.K_UP:
            self.y_change -= offset
            self.direction = Directions.UP
        if key == pygame.K_DOWN:
            self.y_change += offset
            self.direction = Directions.DOWN
            
    def inBounds(self):
        self.rect.x = max(min(self.rect.x, WIN_WIDTH - self.width),self.width)
        self.rect.y = max(min(self.rect.y, WIN_HEIGHT - self.height),self.height)
    
        
    def update(self):
        self.rect.x += self.x_change * self.speed
        self.rect.y += self.y_change * self.speed
        
        self.inBounds()
        

        
        

        
    