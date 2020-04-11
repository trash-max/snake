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

cube_red_img = pygame.image.load(r'cube_red.png').convert()
cube_green_img = pygame.image.load(r'cube_green.png').convert()

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
    enemies = []
    taillenght = 3
    tails = []
    hero = Enemy(background, cube_green_img, 380, 280)
    hero.draw()
    # i = 1
    # while i < 50:
    #     hero.move(i, 0)
    #     i += 1

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
                hero.move(velocity[0], velocity[1])
                tail = Tail(background, cube_green_img, hero.rect.left, hero.rect.top)
                tails.insert(0, tail)

        while len(enemies) < 3:
            enemy = Enemy(background, cube_red_img, random.randint(50, 550), random.randint(50, 350))
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
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
