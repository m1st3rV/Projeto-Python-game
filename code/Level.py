#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from pygame.font import Font

import pygame
from pygame import Surface, Rect

from code.EntityMediator import EntityMediator
from code.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 2000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = [ ]
        self.entity_list.extend(EntityFactory.get_entity('nature_1'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)



    def run(self, ):
        pygame.mixer_music.load(os.path.join('./asset/music/843679.wav'))
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy1'))


            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', (10, 5), COLOR_WHITE,)
            self.level_text(14, f'fps: {clock.get_fps()}',(25, WIN_HEIGHT - 5), COLOR_WHITE)
            self.level_text(14, f'entidades: {len(self.entity_list)}' , (40, WIN_HEIGHT - 50),COLOR_WHITE )
            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass

    def level_text(self, text_size: int, text: str, position: tuple, color: tuple):
        text_font: Font = pygame.font.SysFont('Times New Roman', size=text_size)
        text_surface: Surface = text_font.render(text, True, color=COLOR_WHITE).convert_alpha()
        text_rect: Rect= text_surface.get_rect(left=position[0], top=position[0])
        self.window.blit(source=text_surface, dest=text_rect)
