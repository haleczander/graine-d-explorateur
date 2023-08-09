import pygame
from config import *


from modules.Player import Player

class Game:
    def __init__(self) -> None:     
        pygame.init()       
        pygame.display.set_caption(GAME_NAME)
        self.screen = pygame.display.set_mode(WIN_SIZE)
        self.clock = pygame.time.Clock()
        self.running = True
    
    def new(self):
        self.playing = True   
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.block_sprites = pygame.sprite.LayeredUpdates()
        self.player = Player(self, 10, 10)
        
    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        self.running = False
            
    def events(self):        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if (event.type == pygame.KEYDOWN or event.type == pygame.KEYUP) and event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    self.player.keyMove(event.key, event.type)

          
    def update(self):
        self.all_sprites.update()
        
    def draw(self):
        self.screen.fill(FILL)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(FPS)
        
game = Game()
game.new()
while game.running:
    game.run()
pygame.quit()