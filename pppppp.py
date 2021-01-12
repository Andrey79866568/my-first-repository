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


class Pers(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = pygame.Surface([20, 20])
        self.image.fill('#0000ff')
        self.rect = pygame.Rect(pos[0], pos[1], 20, 20)
        self.speed = 50

    def update(self, time):
        if not pygame.sprite.spritecollideany(self, log_sprites):
            self.rect.y += round(50 * time / 1000)


class Log(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites, log_sprites)
        self.image = pygame.Surface([50, 10])
        self.image.fill((170, 170, 170))
        self.rect = pygame.Rect(pos[0], pos[1], 50, 10)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Решение')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    all_sprites = pygame.sprite.Group()
    log_sprites = pygame.sprite.Group()
    fps = 60
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                try:
                    if event.key == pygame.K_LEFT:
                        pers.rect.x -= 10
                    elif event.key == pygame.K_RIGHT:
                        pers.rect.x += 10
                except NameError:
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    try:
                        pers.rect.x, pers.rect.y = event.pos
                    except NameError:
                        pers = Pers(event.pos)
                elif event.button == 3:
                    Log(event.pos)
        all_sprites.update(clock.tick(fps))
        all_sprites.draw(screen)
        pygame.display.flip()
        screen.fill((0, 0, 0))
    pygame.quit()
