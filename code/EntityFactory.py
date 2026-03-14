#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Enemy import Enemy
from code.Player import Player

from code.Background import Background
from code.Const import WIN_WIDTH

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'nature_1': #BACKGROUND LEVEL 1
                list_bg = []
                for i in range(8):
                    list_bg.append(Background(f'nature_1_{i}', (0,0))) #FETCH FOR THE IMAGES WHICH NAME STARTS WITH NATURE_1
                    list_bg.append(Background(f'nature_1_{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'nature_4':  #BACKGROUND LEVEL 2
                list_bg = []
                for i in range(4):
                    list_bg.append(
                        Background(f'nature_4_{i}', (0, 0)))  # FETCH FOR THE IMAGES WHICH NAME STARTS WITH NATURE_1
                    list_bg.append(Background(f'nature_4_{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player':
                return Player('Player', (5, 240))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, 240))

