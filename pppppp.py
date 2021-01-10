import os
import sys
import pygame
from random import randint


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Bomb(pygame.sprite.Sprite):
    def __init__(self, *group, colorkey=None):
        super().__init__(*group)
        self.speed = 2
        self.image = load_image('bomb.png', colorkey)
        self.bang = load_image('bombbym.png', colorkey)
        w, h = self.bang.get_size()
        x = randint((self.bang.get_width() - self.image.get_width()) // 2, 500 - w)
        y = randint((self.bang.get_height() - self.image.get_height()) // 2, 500 - h)
        self.rect = pygame.rect.Rect(x, y, *self.image.get_size())

    def in_bbomb(self, x, y):
        return self.rect.x < x < self.rect.x + self.rect.w and \
               self.rect.y < y < self.rect.y + self.rect.h

    def update(self, x, y):
        if self.in_bbomb(x, y) and self.image != self.bang:
            self.rect.x -= (self.bang.get_width() - self.rect.w) // 2
            self.rect.y -= (self.bang.get_height() - self.rect.h) // 2
            self.image = self.bang


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Решение')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    all_sprite = pygame.sprite.Group()
    for i in range(20):
        Bomb(all_sprite)
    fps = 60
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    all_sprite.update(*event.pos)
        all_sprite.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
        screen.fill((0, 0, 0))
    pygame.quit()
