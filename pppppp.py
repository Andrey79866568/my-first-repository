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


class Car(pygame.sprite.Sprite):
    def __init__(self, picture, x, y, *group, colorkey=None):
        super().__init__(*group)
        self.speed = 2
        self.image = load_image(picture, colorkey)
        self.rect = pygame.rect.Rect(x, y, *self.image.get_size())

    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= width - 150:
            self.speed = -2
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.rect.x <= 0:
            self.speed = 2
            self.image = pygame.transform.flip(self.image, True, False)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Решение')
    size = width, height = 500, 100
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    all_sprite = pygame.sprite.Group()
    car = Car('car.png', 0, 0, all_sprite)
    fps = 60
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprite.draw(screen)
        all_sprite.update()
        clock.tick(fps)
        pygame.display.flip()
        screen.fill((255, 255, 255))
    pygame.quit()
