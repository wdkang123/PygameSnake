import pygame
import random
import math


screen_width = 400
screen_height = 400
pygame.init()
screencaption = pygame.display.set_caption('Snake')
screen = pygame.display.set_mode([screen_width, screen_height])
myfont = pygame.font.Font(None, 30)
clock = pygame.time.Clock()

n = 0
move_flag = 0

# 蛇
snake_list = [(3, 4), (4, 4), (5, 4)]

# 0左 1上 2右 3下
direction = 0
x = 20
y = 20
apple_x = 5
apple_y = 5
while True:
    clock.tick(30)
    screen.fill([255, 255, 255])

    # 每1秒刷新3次蛇
    if n >= 10:
        n = 0
        # 获取队尾
        head_pos = snake_list[0]
        snake_list.pop()
        x = head_pos[0]
        y = head_pos[1]
        # 吃果实
        if x == apple_x and y == apple_y:
            snake_list.insert(0, (apple_x, apple_y))
        if direction == 0:
            if x < 0:
                pass
            x = x - 1
        elif direction == 1:
            if y < 0:
                pass
            y = y - 1
        elif direction == 2:
            if x > 20:
                pass
            x = x + 1
        elif direction == 3:
            if y > 20:
                pass
            y = y + 1
        snake_list.insert(0, (x, y))
    n = n + 1

    # 画蛇
    snake_list_index = 0
    for each in snake_list:
        position = (each[0] * 22, each[1] * 22, 20, 20)
        if snake_list_index == 0:
            snake_list_index = snake_list_index + 1
            pygame.draw.rect(screen, [255, 0, 0], position, 4)
            continue
        pygame.draw.rect(screen, [125, 125, 125], position, 4)

    # 画果实
    pygame.draw.circle(screen, [0, 0, 255], [apple_x * 22 + 10, apple_y * 22 + 10], 8, 8)

    # 事件函数
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 0
            if event.key == pygame.K_UP:
                direction = 1
            if event.key == pygame.K_RIGHT:
                direction = 2
            if event.key == pygame.K_DOWN:
                direction = 3
    pygame.display.flip()

