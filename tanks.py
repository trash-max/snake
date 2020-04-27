#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

# Vars
GAME_NAME = 'Tanks'
WIN_SIZE = (800, 600)
FPS = 60

# Same colors
RED = (150, 0, 0)
GREEN = (0, 150, 0)
BLUE = (0, 0, 150)

# Pygame inits
pygame.init()
pygame.display.set_caption(GAME_NAME)
screen = pygame.display.set_mode(WIN_SIZE)
clock = pygame.time.Clock()

# Base surface
background = pygame.Surface(WIN_SIZE)

# images
tank_img = (pygame.image.load(r'resource/tank/Tank1.png').convert_alpha(), pygame.image.load(r'resource/tank/Tank2.png').convert_alpha())
turret_img = pygame.image.load(r'resource/tank/Turret1.png').convert_alpha()

# fonts
font = pygame.font.Font(r'resource/3976.ttf', 50)


class tank():
    def __init__(self, x, y, tank_img, turret_img):
        self.x = x
        self.y = y
        self.img = tank_img
        self.turret = turret_img
        self.angle = 0
        self.turret_angle = 0
        self.rotation = pygame.transform.rotate(self.img[0], 0)

    def draw(self, tank_angle, turret_angle, direction):
        vx = 0
        vy = 0

        # Setting tank angle
        if tank_angle != 0:
            self.angle += tank_angle
            if self.angle >= 360:
                self.angle = 0
            if self.angle < 0:
                self.angle = 345
            # Tank rotate on angle
            self.rotation = pygame.transform.rotate(self.img[0], -self.angle)

        # Setting movement direction (new coords)
        # direction: 0 - stop, 1 - forward, -1 - backward
        if direction !=0:
            if self.angle == 0:
                vx = 0
                vy = -3
            elif self.angle == 15:
                vx = 1
                vy = -3
            elif self.angle == 30:
                vx = 2
                vy = -3
            elif self.angle == 45:
                vx = 3
                vy = -3
            elif self.angle == 60:
                vx = 3
                vy = -2
            elif self.angle == 75:
                vx = 3
                vy = -1
            elif self.angle == 90:
                vx = 3
                vy = 0
            elif self.angle == 105:
                vx = 3
                vy = 1
            elif self.angle == 120:
                vx = 3
                vy = 2
            elif self.angle == 135:
                vx = 3
                vy = 3
            elif self.angle == 150:
                vx = 2
                vy = 3
            elif self.angle == 165:
                vx = 1
                vy = 3
            elif self.angle == 180:
                vx = 0
                vy = 3
            elif self.angle == 195:
                vx = -1
                vy = 3
            elif self.angle == 210:
                vx = -2
                vy = 3
            elif self.angle == 225:
                vx = -3
                vy = 3
            elif self.angle == 240:
                vx = -3
                vy = 2
            elif self.angle == 255:
                vx = -3
                vy = 1
            elif self.angle == 270:
                vx = -3
                vy = 0
            elif self.angle == 285:
                vx = -3
                vy = -1
            elif self.angle == 300:
                vx = -3
                vy = -2
            elif self.angle == 315:
                vx = -3
                vy = -3
            elif self.angle == 330:
                vx = -2
                vy = -3
            elif self.angle == 345:
                vx = -1
                vy = -3
            # Tank move (direction: 0 - stop, 1 - forward, -1 - backward)
            if direction == 1:
                self.x += vx
                self.y += vy
            else:
                self.x += -vx
                self.y += -vy

        # Tank draw
        background.blit(self.rotation, (self.x, self.y))

        turret_rot = pygame.transform.rotate(self.turret, -self.angle)
        background.blit(turret_rot, (self.x, self.y))

        text = font.render(str(self.angle), 1, (255, 255, 255))
        background.blit(text, (10, 10))
        text = font.render(str(self.turret_angle), 1, (255, 255, 255))
        background.blit(text, (150, 10))
        text = font.render(str(self.x), 1, (255, 255, 255))
        background.blit(text, (400, 10))
        text = font.render(str(self.y), 1, (255, 255, 255))
        background.blit(text, (500, 10))


# Main game
def game_cycle():
    hero = tank(100, 100, tank_img, turret_img)
    anim_counter = 0
    # Main game cycle
    while True:
        # direction: 0 - stop, 1 - forward, -1 - backward
        direction = 0
        tank_angle = 0
        turret_angle = 0
        background.fill(BLUE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            return
        if anim_counter in [10, 20, 30, 40, 50, 60]:
            if keys[pygame.K_LEFT]:
                tank_angle = -15
            if keys[pygame.K_RIGHT]:
                tank_angle = 15
            if keys[pygame.K_z]:
                turret_angle = -5
            if keys[pygame.K_x]:
                turret_angle = 5
        if anim_counter in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]:
        # direction: 0 - stop, 1 - forward, -1 - backward
            if keys[pygame.K_DOWN]:
                direction = -1
            if keys[pygame.K_UP]:
                direction = 1

        hero.draw(tank_angle, turret_angle, direction)

        if anim_counter <= 60:
            anim_counter += 1
        else:
            anim_counter = 0

        #  Display update
        screen.blit(background, (0, 0))
        pygame.display.update()
        clock.tick(FPS)


def main():
    game_cycle()

if __name__ == "__main__":
    main()
