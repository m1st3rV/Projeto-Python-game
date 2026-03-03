#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractproperty, abstractmethod
from os import name, path
from pathlib import Path
import pygame

from code.Const import ENTITY_HEALTH


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load("./asset/nature_1/" + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 1
        self.health = ENTITY_HEALTH[self.name]

    @abstractmethod
    def move(self, ):
        pass