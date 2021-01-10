import os
import sys
import pygame


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


class Monster:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = load_image('monster1.png')

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Решение')
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    mon = Monster()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == 1073741904:
                    mon.x -= 10
                elif event.key == 1073741903:
                    mon.x += 10
                elif event.key == 1073741906:
                    mon.y -= 10
                elif event.key == 1073741905:
                    mon.y += 10
        mon.draw(screen)
        pygame.display.flip()
        screen.fill((255, 255, 255))
    pygame.quit()
