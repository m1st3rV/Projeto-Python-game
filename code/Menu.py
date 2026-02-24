#!/usr/bin/python
#-*- coding: utf-8 -*-
import os.path

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_BLACK, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load(os.path.join('./asset/nature_2/orig.png'))
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/music/843679.wav')    #EDITE O CAMINHO PARA SELECIONAR O ARQUIVO DESEJADO
        pygame.mixer_music.play(-1)
# DESCOMENTAR AS LINHAS ACIMA AO INFORMAR O ARQUIVO DE SOM
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=50, text="Welcome to Vinland", text_color=COLOR_BLACK, text_center_position=((WIN_WIDTH / 2), 70))

            for i in range(len(MENU_OPTION)):
                self.menu_text( text_size=30, text=(MENU_OPTION[i]), text_color=COLOR_BLACK, text_center_position=((WIN_WIDTH / 2), (WIN_HEIGHT / 2) + 30 * i ))

            pygame.display.flip()

        # CHECK FOR EVENTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # CLOSE WINDOW
                    quit() #end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect =  text_surf.get_rect(center=text_center_position)
        self.window.blit(source=text_surf, dest=text_rect)