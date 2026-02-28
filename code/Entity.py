#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractproperty, abstractmethod
from os import name
import pygame

class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/''name +''.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 1

    @abstractmethod
    def move(self, ):
        pass