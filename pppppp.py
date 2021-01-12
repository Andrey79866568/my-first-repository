import os
import sys
import pygame
from random import randint


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    assert os.path.isfile(fullname)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class GameOverSpr(pygame.sprite.Sprite):
    def __init__(self, *group, colorkey=None):
        super().__init__(*group)
        self.speed = 1
        self.image = load_image('game_over.png', colorkey)
        self.image = pygame.transform.scale(self.image, (500, 300))
        self.rect = pygame.rect.Rect(-500, 0, 500, 300)

    def update(self, x_i, time):
        if x_i - (self.rect.x + self.rect.w) > 2:
            self.rect.x += self.speed * time
        else:
            self.rect.x = x_i - self.rect.w


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Решение')
    size = width, height = 500, 300
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 255))
    all_sprites = pygame.sprite.Group()
    fps = 500
    gg = GameOverSpr(all_sprites)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.update(width, clock.tick(fps))
        all_sprites.draw(screen)
        pygame.display.flip()
        screen.fill((0, 0, 255))
    pygame.quit()
