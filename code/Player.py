#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import name

import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def update(self):
        pass

    def move(self, ):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_keys[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
#        if pressed_keys[pygame.K_SPACE] and self.rect.top > 0:

        pass

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_LCTRL]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))