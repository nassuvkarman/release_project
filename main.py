from typing import Any
import pygame


WIDTH = 1000
HEIGH = 600
SIZE = (WIDTH, HEIGH)
FPS = 60

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load("background_image.png"),SIZE)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, size, coords):
        self.image = pygame.transform.scale(pygame.image.load(filename),size)
        self.rect = self.image.get_rect()
        self.rect.center = coords
    def reset(self):
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def update_l(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x -= 10
        elif key[pygame.K_d]:
            self.rect.x += 10
    def update_r(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 10
        elif key[pygame.K_RIGHT]:
            self.rect.x += 10

game_over = False
finish = False

#test_object = GameSprite("test_image.png", (100,100), (100,100))
car1 = Player("car_image1.png", (100,200),(WIDTH-400,HEIGH-50))
car2 = Player("car_image2.png",(160,150), (WIDTH-600, HEIGH-50))
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    if not finish:
        window.blit(background, (0,0))
        car1.reset()
        car1.update_r()
        car2.reset()
        car2.update_l()

        if car1.rect.colliderect(car2.rect):
            game_over = True

    pygame.display.update()
    clock.tick(FPS)