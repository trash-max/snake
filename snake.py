#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random

pygame.init()
FPS = 60
bg_color = (0, 100, 0)
win_size = (800, 600)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(win_size)

try:
    cube_red_img = pygame.image.load(r'resource/cube_red.png').convert()
    cube_green_img = pygame.image.load(r'resource/cube_green.png').convert()
except Exception as e:
    raise


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


background = pygame.Surface(win_size)


def main():
    global FPS
    background.fill(bg_color)
    velocity = (0, 0)
    velocity_speed = 30
    velocity_counter = 0
    enemies = []
    taillenght = 3
    tails = []
    hero = Enemy(background, cube_green_img, 380, 280)
    hero.draw()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    velocity = (-20, 0)
                elif event.key == pygame.K_RIGHT:
                    velocity = (20, 0)
                elif event.key == pygame.K_UP:
                    velocity = (0, -20)
                elif event.key == pygame.K_DOWN:
                    velocity = (0, 20)
                # --- Uncomment for manual move control ---
                # hero.move(velocity[0], velocity[1])
                # tail = Tail(background, cube_green_img, hero.rect.left, hero.rect.top)
                # tails.insert(0, tail)
                # --- Uncomment for manual move control ---

        # --- Uncomment for automatic move control ---
        velocity_counter += 1
        if velocity_counter == velocity_speed:
            hero.move(velocity[0], velocity[1])
            tail = Tail(background, cube_green_img, hero.rect.left, hero.rect.top)
            tails.insert(0, tail)
            velocity_counter = 0
        # --- Uncomment for automatic move control ---

        while len(enemies) < 3:
            enemy = Enemy(background, cube_red_img, random.randrange(20, win_size[0]-20, 20), random.randrange(20, win_size[1]-20, 20))
            enemy.draw()
            enemies.append(enemy)

        for enemy in enemies:
            if hero.rect.colliderect(enemy.rect):
                background.fill(bg_color, enemy.rect)
                enemies.remove(enemy)
                hero.draw()
                taillenght += 1

        for tail in tails:
            tail.draw()
            if tails.index(tail) > taillenght:
                tail.clear()
                tails.remove(tail)

        screen.blit(background, (0,0))

        if hero.rect.left <= 0 or hero.rect.right >= win_size[0]:
            return
        if hero.rect.top <= 0 or hero.rect.bottom >= win_size[1]:
            return


        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
