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


class Mountain(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = pygame.transform.scale(load_image("горы.png", colorkey='#ffffff'), (600, 300))
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = height


class Landing(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = pygame.transform.scale(load_image("парашют.png", colorkey='#ffffff'), (100, 100))
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0, 1)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Решение')
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    screen.fill('#ffffff')

    all_sprites = pygame.sprite.Group()

    mountain = Mountain()
    fps = 500
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Landing(event.pos)
        all_sprites.update()
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
        screen.fill('#ffffff')
    pygame.quit()
