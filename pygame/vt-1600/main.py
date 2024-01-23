import pygame
import sys

# запустим pygame (инициализируем)
pygame.init()

FPS = 60
SCREEN_SIZE = (600, 400)

# создать окно
screen = pygame.display.set_mode(SCREEN_SIZE)

# для отслеживания времени
clock = pygame.time.Clock()

# создадим поверхность и закрасим
surface_1 = pygame.Surface((100, 100))
surface_1.fill((255,0,255)) # RGB - red green blue

print(pygame.event.get())

while True:
    # цикл событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # деинициализация Pygame
            pygame.quit()
            # завершение работы программы
            sys.exit()
    screen.blit(surface_1, (200, 100))

    # обновлять кадры
    pygame.display.update()

    # верхняя граница FPS
    clock.tick(FPS)
