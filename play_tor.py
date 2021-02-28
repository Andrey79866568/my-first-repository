from load_functions import load_image
import os
import sys
import pygame


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = WIDTH // 2
        self.dy = HEIGHT // 2

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def get_delta(self):
        return self.dx, self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


class Person(pygame.sprite.Sprite):
    def __init__(self, x, y, cell_size, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('mar.png', 'data'), (cell_size, cell_size))
        self.rect = pygame.rect.Rect(x, y, cell_size, cell_size)
        self.left_run = False
        self.right_run = False
        self.up_run = False
        self.down_run = False
        self.v = WIDTH // 7

    def update(self, time):
        if self.left_run and not self.right_run:
            self.rect.x += round(self.v * -1 * time / 1000)

        elif not self.left_run and self.right_run:
            self.rect.x += round(self.v * time / 1000)

        if self.up_run and not self.down_run:
            self.rect.y += round(self.v * -1 * time / 1000)

        elif not self.up_run and self.down_run:
            self.rect.y += round(self.v * time / 1000)


class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y, image, *group):
        super().__init__(*group)
        self.image = image
        self.rect = pygame.rect.Rect(x, y, *image.get_size())


class Board:
    # создание поля
    def __init__(self, file, load_image):
        read_list = open(file, encoding='utf-8').readlines()
        self.w_n = len(read_list[0]) - 1
        self.h_n = len(read_list)
        self.board = [list(i.strip()) for i in read_list]

        self.left = 0
        self.top = 0

        self.cell_size = WIDTH // 13

        self.grass = pygame.transform.scale(load_image('grass.png', 'data'), (self.cell_size, self.cell_size))
        self.box = pygame.transform.scale(load_image('box.png', 'data'), (self.cell_size, self.cell_size))

    def render(self, screen):
        x = self.left
        y = self.top
        for i in range(self.h_n):
            for j in range(self.w_n):
                if self.board[i][j] == '@':
                    screen.blit(self.grass, (x, y))
                elif self.board[i][j] == 'X':
                    self.pers = Person(x, y, self.cell_size, all_sprites)
                    self.board[i][j] = '@'
                elif self.board[i][j] == '#':
                    Ground(x, y, self.box, all_sprites, ground_sprites)
                    self.board[i][j] = '@'
                x += self.cell_size
            x = self.left
            y += self.cell_size


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pygame.transform.scale(load_image('fon.jpg', 'data'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(pygame.font.get_default_font(), 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def main_cycle():
    camera = Camera()
    board = Board('map.txt', load_image)
    board.render(screen)

    board_r = False
    board_l = False
    board_u = False
    board_d = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    board.pers.up_run = True
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    board.pers.down_run = True
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    board.pers.left_run = True
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    board.pers.right_run = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    board.pers.up_run = False
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    board.pers.down_run = False
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    board.pers.left_run = False
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    board.pers.right_run = False

        screen.fill((0, 0, 0))

        if pygame.sprite.spritecollideany(board.pers, ground_sprites):
            if board.pers.right_run and not board.pers.left_run:
                board.pers.right_run = False
                board.pers.rect.x -= 3
            elif board.pers.left_run and not board.pers.right_run:
                board.pers.left_run = False
                board.pers.rect.x += 3
            if board.pers.up_run and not board.pers.down_run:
                board.pers.up_run = False
                board.pers.rect.y += 3
            elif board.pers.down_run and not board.pers.up_run:
                board.pers.down_run = False
                board.pers.rect.y -= 3

        for sprite in ground_sprites:
            if sprite.rect.x - board.pers.rect.x > board.cell_size * 10:
                sprite.rect.x -= board.cell_size * 20
                board_l = True
                # board.left -= board.cell_size * 20
            elif board.pers.rect.x - sprite.rect.x > board.cell_size * 10:
                sprite.rect.x += board.cell_size * 20
                board_r = True
                # board.left += board.cell_size * 20
            if sprite.rect.y - board.pers.rect.y > board.cell_size * 15:
                sprite.rect.y -= board.cell_size * 30
                board_u = True
                # board.top -= board.cell_size * 20
            elif board.pers.rect.y - sprite.rect.y > board.cell_size * 15:
                sprite.rect.y += board.cell_size * 30
                board_d = True
                # board.top += board.cell_size * 20

        if board_d:
            board.top += board.cell_size
            board_d = False
            print(1)
        elif board_u:
            board.top -= board.cell_size
            board_u = False
            print(2)
        if board_l:
            board.left -= board.cell_size
            board_l = False
        elif board_r:
            board.left += board.cell_size
            board_r = False

        board.render(screen)
        camera.update(board.pers)
        board.left += camera.get_delta()[0]
        board.top += camera.get_delta()[1]
        for sprite in all_sprites:
            camera.apply(sprite)
        all_sprites.draw(screen)
        all_sprites.update(clock.tick(FPS))
        pygame.display.flip()


WIDTH = 700
HEIGHT = 700
all_sprites = pygame.sprite.Group()
ground_sprites = pygame.sprite.Group()
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60
start_screen()
main_cycle()
