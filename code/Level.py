#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from pygame.font import Font
import pygame
from pygame import Surface, Rect
from code.Enemy import Enemy
from code.EntityMediator import EntityMediator
from code.Const import COLOR_WHITE, EVENT_ENEMY, SPAWN_TIME, COLOR_RED, EVENT_TIMEOUT, \
    TIMEOUT_TIME, TIMEOUT_TAX, LEVEL_CONFIG
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player


class Level:
    def __init__(self, window:Surface, name:str, game_mode:str, player_score: list[int]):
        self.timeout = TIMEOUT_TIME
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.music = LEVEL_CONFIG[name]['music']
        self.entity_list: list[Entity] = [ ]
        self.entity_list.extend(EntityFactory.get_entity(LEVEL_CONFIG[name]['bg']))
        player = EntityFactory.get_entity('Player')
        player.score = player_score[0]
        self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_TAX)



    def run(self, player_score:list[int]):
        pygame.mixer_music.load(os.path.join('./asset/music/level1.wav'))
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player':
                    self.level_text(14, f'Player Health: {ent.health} | Score: {ent.score}', (20, 40), COLOR_RED)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy1'))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_TAX
                    if self.timeout <= 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player):
                                player_score[0] = ent.score
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', (10, 5), COLOR_WHITE,)
            self.level_text(14, f'fps: {clock.get_fps()}',(250, 5), COLOR_WHITE)
#            self.level_text(14, f'entidades: {len(self.entity_list)}' , (40, WIN_HEIGHT - 50),COLOR_WHITE )
            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)


    def level_text(self, text_size: int, text: str, position: tuple, color: tuple):
        text_font: Font = pygame.font.SysFont('Times New Roman', size=text_size)
        text_surface: Surface = text_font.render(text, True, color=color).convert_alpha()
        text_rect: Rect= text_surface.get_rect(left=position[0], top=position[1])
        self.window.blit(source=text_surface, dest=text_rect)
