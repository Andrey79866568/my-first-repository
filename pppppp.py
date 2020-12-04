import pygame
from math import sin, cos, pi


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Решение')
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    screen2 = pygame.Surface(screen.get_size())
    drawing = False
    stack_list = []
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                stack_list.append([event.pos[0], event.pos[1], 0, 0])
            if event.type == pygame.MOUSEBUTTONUP:
                screen2.blit(screen, (0, 0))
                drawing = False
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    stack_list[-1][-2] = event.pos[0] - stack_list[-1][0]
                    stack_list[-1][-1] = event.pos[1] - stack_list[-1][1]
            if event.type == pygame.KEYDOWN:
                if event.key == 122 and event.mod == 4160:
                    try:
                        stack_list.pop()
                    except IndexError:
                        pass
                    screen2.fill(pygame.Color('black'))
                    for i in stack_list:
                        if i[2] > 0 and stack_list[-1][3] > 0:
                            pygame.draw.rect(screen2, (0, 0, 255), ((i[0], i[1]), (i[2], i[3])), 5)
        screen.fill(pygame.Color('black'))
        screen.blit(screen2, (0, 0))
        if drawing:
            if stack_list[-1][2] > 0 and stack_list[-1][3] > 0:
                pygame.draw.rect(screen, (0, 0, 255), ((stack_list[-1][0], stack_list[-1][1]),
                                                       (stack_list[-1][2], stack_list[-1][3])), 5)
        pygame.display.flip()
    pygame.quit()
