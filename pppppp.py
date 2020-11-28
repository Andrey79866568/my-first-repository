import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Решение')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    fps = 95  # количество кадров в секунду
    clock = pygame.time.Clock()
    rad = 10
    v = 100
    xy_list = []
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                xy_list.append([event.pos[0], event.pos[1], 'vl'])
        time = clock.tick(fps)
        for i in range(len(xy_list)):
            pygame.draw.circle(screen, (255, 255, 255), (xy_list[i][0], xy_list[i][1]), rad)
            if xy_list[i][2] == 'vl':
                xy_list[i][0] -= v * time / 1000
                xy_list[i][1] -= v * time / 1000
            elif xy_list[i][2] == 'vr':
                xy_list[i][0] += v * time / 1000
                xy_list[i][1] -= v * time / 1000
            elif xy_list[i][2] == 'dl':
                xy_list[i][0] -= v * time / 1000
                xy_list[i][1] += v * time / 1000
            elif xy_list[i][2] == 'dr':
                xy_list[i][0] += v * time / 1000
                xy_list[i][1] += v * time / 1000

            if xy_list[i][0] - rad < 2:
                xy_list[i][2] = xy_list[i][2][0] + 'r'
            elif xy_list[i][1] - rad < 2:
                xy_list[i][2] = 'd' + xy_list[i][2][1]

            elif width - xy_list[i][0] - rad < 2:
                xy_list[i][2] = xy_list[i][2][0] + 'l'
            elif height - xy_list[i][1] - rad < 2:
                xy_list[i][2] = 'v' + xy_list[i][2][1]
        pygame.display.flip()
        screen.fill((0, 0, 0))
    pygame.quit()
