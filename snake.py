#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random

pygame.init()

# Конфигурация
# Имя игры
game_name = 'Snake'
pygame.display.set_caption(game_name)

FPS = 60
# Цвет фона
bg_color = (0, 100, 0)
# Количество игровых блоков ширина/высота (40х30 блоков = 800х600 px)
blocks_w = 20
blocks_h = 20
# Размер игрового блока (лучше не менять)
block_size = 20
# Итоговое разрешение ирового поля
win_size = (blocks_w * block_size, blocks_h * block_size)
# Скорость движения змеи
velocity_speed = 30
# Размер шрифта и цвет текста
font_size = 16
text_color = (255, 255, 255)

clock = pygame.time.Clock()
# Объявим дисплей
screen = pygame.display.set_mode(win_size)
# Объявим отдельную поверхность по размерам дисплея
# весь дальнейший вывод производится на нее
background = pygame.Surface(win_size)
# Загружаем изображения
try:
    cube_red_img = pygame.image.load(r'resource/snake/cube_red.png').convert()
    cube_green_img = pygame.image.load(r'resource/snake/cube_green.png').convert()
    cube_head_img = pygame.image.load(r'resource/snake/cube_green.png').convert()
    border_line_img = pygame.image.load(r'resource/snake/border.png').convert()
    corner_img = pygame.image.load(r'resource/snake/corner.png').convert()
except Exception as e:
    raise

try:
    font = pygame.font.Font(r'resource/3976.ttf', font_size)
    # font = pygame.font.Font(None, font_size)
except Exception as e:
    raise


# Класс используется как для еды, так и для головы змеи
class Enemy():
    def __init__(self, surf, img, x, y):
        # self.color = (255, 255,255)
        self.surf = surf
        self.img = img
        self.x = x
        self.y = y
        self.rect = img.get_rect(topleft = (x, y))

    def draw(self):
        self.surf.blit(self.img, self.rect)

    def move(self, vx, vy):
        self.surf.fill(bg_color, self.rect)
        self.rect.move_ip(vx, vy)
        self.surf.blit(self.img, self.rect)

    def body():
        return self.rect


# Отдельный класс для элементов хвоста
class Tail():
    def __init__(self, surf, img, x, y):
        # self.color = (255, 255,255)
        self.surf = surf
        self.img = img
        self.x = x
        self.y = y
        self.rect = img.get_rect(topleft = (x, y))

    def draw(self):
        self.surf.blit(self.img, self.rect)

    def clear(self):
        self.surf.fill(bg_color, self.rect)

# Перенесено в раздел конфигурации
# background = pygame.Surface(win_size)

# Рисутет рамку вокруг игрового поля
def draw_border(img, cimg):
    i = block_size
    while i <= win_size[1] - (block_size * 2):
        background.blit(img, (0, i))
        i += block_size
    i = block_size
    rot = pygame.transform.rotate(img, 180)
    while i <= win_size[1] - (block_size * 2):
        background.blit(rot, (win_size[0]-block_size, i))
        i += block_size
    i = block_size
    rot = pygame.transform.rotate(img, -90)
    while i <= win_size[0] - (block_size * 2):
        background.blit(rot, (i, 0))
        i += block_size
    i = block_size
    rot = pygame.transform.rotate(img, 90)
    while i <= win_size[0] - (block_size * 2):
        background.blit(rot, (i, win_size[1]-block_size))
        i += block_size
    background.blit(cimg, (0, 0))
    rot = pygame.transform.rotate(cimg, 90)
    background.blit(cimg, (0, win_size[1]-block_size))
    rot = pygame.transform.rotate(cimg, -90)
    background.blit(cimg, (win_size[0]-block_size, 0))
    rot = pygame.transform.rotate(cimg, 180)
    background.blit(cimg, (win_size[0]-block_size, win_size[1]-block_size))


def draw_text():
    text = font.render("SPACE to pause", 1, (text_color))
    place = text.get_rect(topleft=(block_size, win_size[1]-block_size))
    background.blit(text, place)
    text = font.render("Q to quit", 1, (text_color))
    place = text.get_rect(topleft=((win_size[0] - (block_size * 4)) - 6, win_size[1]-block_size))
    background.blit(text, place)


# Пауза в игре
def game_pause():
    pause = True
    while pause:
        pygame.time.delay(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = False
    return

# Основной игровой цикл
def game_cycle():
    # global FPS
    # закрасим поле
    background.fill(bg_color)
    # нарисуем рамки
    draw_border(border_line_img, corner_img)
    draw_text()
    # изначальный вектор движения
    velocity = (0, -block_size)
    # изначальная длина хвоста
    taillenght = 1
    # далее объявление служебных переменных цикла
    nextturn = True
    velocity_counter = 0
    enemies = []
    tails = []
    score = 0
    # создаем и рисуем голову змеи на стартовой позиции
    hero = Enemy(background, cube_head_img, (blocks_w // 2) * block_size, (blocks_h // 2) * block_size)
    hero.draw()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if velocity[0] != block_size and nextturn:
                        velocity = (-block_size, 0)
                        nextturn = False

                elif event.key == pygame.K_RIGHT:
                    if velocity[0] != -block_size and nextturn:
                        velocity = (block_size, 0)
                        nextturn = False

                elif event.key == pygame.K_UP:
                    if velocity[1] != block_size and nextturn:
                        velocity = (0, -block_size)
                        nextturn = False

                elif event.key == pygame.K_DOWN:
                    if velocity[1] != -block_size and nextturn:
                        velocity = (0, block_size)
                        nextturn = False

                elif event.key == pygame.K_SPACE:
                    game_pause()

                elif event.key == pygame.K_q:
                    return

        if velocity_counter == velocity_speed:
            tail = Tail(background, cube_green_img, hero.rect.left, hero.rect.top)
            hero.move(velocity[0], velocity[1])
            tails.insert(0, tail)
            velocity_counter = 0
            nextturn = True

            # Генерация еды для змеи (три штуки)
            while len(enemies) < 3:
                enemy = Enemy(background, cube_red_img, random.randrange(block_size, win_size[0]-block_size, block_size), random.randrange(block_size, win_size[1]-block_size, block_size))
                enemy.draw()
                enemies.append(enemy)

            for enemy in enemies:
                if hero.rect.colliderect(enemy.rect):
                    background.fill(bg_color, enemy.rect)
                    enemies.remove(enemy)
                    hero.draw()
                    taillenght += 1
                    score += 1
                    pygame.display.set_caption(f'{game_name}: score: {score}')

            for tail in tails:
                tail.draw()
                if tails.index(tail) > taillenght:
                    tail.clear()
                    tails.remove(tail)
                if hero.rect.colliderect(tail.rect):
                     return
                for enemy in enemies:
                    if tail.rect.colliderect(enemy.rect):
                        enemies.remove(enemy)


            screen.blit(background, (0,0))

            if hero.rect.left <= 0 or hero.rect.right >= win_size[0]:
                return
            if hero.rect.top <= 0 or hero.rect.bottom >= win_size[1]:
                return

        velocity_counter += 1
        pygame.display.update()
        clock.tick(FPS)


def main():
    game_cycle()

if __name__ == "__main__":
    main()
