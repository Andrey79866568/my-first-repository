import pygame
import csv


def zoom(list_of_points, alpha):
    pygame.draw.polygon(screen, 'white', [
        ((k[0] - width // 2) * alpha + width // 2, (k[1] - width // 2) * alpha + width // 2) for k in
        list_of_points], 2)


if __name__ == '__main__':
    width = 501
    size = width, width
    with open('points.txt', 'r') as file1:
        reader = csv.reader(file1, delimiter=')', quotechar='"')
        for i in reader:
            x = i[0][1:].split(';')
            list_ik = [j[3:].split(';') for j in i[1:-1]]
    list_ik = [x] + list_ik
    for i in range(len(list_ik)):
        for j in range(len(list_ik[i])):
            if ',' in list_ik[i][j]:
                list_ik[i][j] = list_ik[i][j].replace(',', '.')
            if j == 0:
                list_ik[i][j] = float(list_ik[i][j]) + width // 2
            if j == 1:
                list_ik[i][j] = -1 * float(list_ik[i][j]) + width // 2
        list_ik[i] = tuple(list_ik[i])
    pygame.init()
    print(list_ik)
    pygame.display.set_caption('Решение')
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    running = True
    alpha = 20
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    alpha += 1
                elif event.button == 5:
                    alpha -= 1
        zoom(list_ik, alpha)
        pygame.display.flip()
        screen.fill((0, 0, 0))
    pygame.quit()
