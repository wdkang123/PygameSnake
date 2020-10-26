import pygame
import random
import math


screen_width = 500
screen_height = 500
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
        # 移动
        # 0左 1上 2右 3下
        if direction == 0:
            # 判断死亡 超出屏幕
            if x < 0:
                pass
            x = x - 1
        elif direction == 1:
            # 判断死亡 超出屏幕
            if y < 0:
                break
            y = y - 1
        elif direction == 2:
            # 判断死亡 超出屏幕
            if x > 20:
                break
            x = x + 1
        elif direction == 3:
            # 判断死亡 超出屏幕
            if y > 20:
                break
            y = y + 1
        # 已经移动
        # 判断是否死亡
        # 自己撞死
        pos = (x, y)
        if pos in snake_list:
            break
        # 如果没有死亡 那就移动蛇
        snake_list.insert(0, (x, y))
        # 吃果实
        head_pos = snake_list[0]
        x_ = head_pos[0]
        y_ = head_pos[1]
        if x_ == apple_x and y_ == apple_y:
            snake_list.append((x, y))
            # 随机果实坐标
            apple_x = random.randint(0, 20)
            apple_y = random.randint(0, 20)
            pos = (apple_x, apple_y)
            while pos in snake_list:
                apple_x = random.randint(0, 20)
                apple_y = random.randint(0, 20)
                pos = (apple_x, apple_y)
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
                if direction != 2:
                    direction = 0
            elif event.key == pygame.K_UP:
                if direction != 3:
                    direction = 1
            elif event.key == pygame.K_RIGHT:
                if direction != 0:
                    direction = 2
            elif event.key == pygame.K_DOWN:
                if direction != 1:
                    direction = 3
    pygame.display.flip()

