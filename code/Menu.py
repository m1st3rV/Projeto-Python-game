#!/usr/bin/python
#-*- coding: utf-8 -*-
import os.path

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH, WIN_HEIGHT,COLOR_BLACK, COLOR_WHITE, MENU_OPTION
#MENU_OPTION1, MENU_OPTION2, MENU_OPTION3


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load(os.path.join('./asset/nature_2/orig.png'))
        self.rect = self.surf.get_rect(left=0, top=0)
        self.menu_option = 0

    def run(self, ):
        pygame.mixer_music.load('./asset/music/843679.wav')    #EDITE O CAMINHO PARA SELECIONAR O ARQUIVO DESEJADO
        pygame.mixer_music.play(-1)

        while True:
            #DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=50, text="Welcome to Vinland", text_color=COLOR_BLACK, text_center_position=((WIN_WIDTH / 2), 70))

#            self.menu_text( text_size=30, text=MENU_OPTION1, text_color=COLOR_BLACK, text_center_position=((WIN_WIDTH / 2), 140 ))
#            self.menu_text( text_size=30, text=MENU_OPTION2, text_color=COLOR_BLACK, text_center_position=((WIN_WIDTH / 2), 170 ))
#            self.menu_text( text_size=30, text=MENU_OPTION3, text_color=COLOR_BLACK, text_center_position=((WIN_WIDTH / 2), 200 ))

            for i in range(len(MENU_OPTION)):
                if i == self.menu_option:
                    self.menu_text(30, MENU_OPTION[i], COLOR_WHITE, text_center_position=((WIN_WIDTH / 2), 150 + i * 40))
                else:
                    self.menu_text(30, MENU_OPTION[i], COLOR_BLACK, text_center_position = ((WIN_WIDTH / 2),150 + i * 40))

            pygame.display.flip()

        # CHECK FOR EVENTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # CLOSE WINDOW
                    quit() #end pygame
                if event.type == pygame.KEYDOWN: #DOWN KEY
                    if event.key == pygame.K_DOWN:
                        if self.menu_option < len(MENU_OPTION) - 1:
                            self.menu_option +=1
                        else:
                           self.menu_option = 0
                    if event.key == pygame.K_UP: #UP KEY
                        if self.menu_option > 0:
                            self.menu_option -=1
                        else:
                           self.menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: #return
                        return MENU_OPTION[self.menu_option]




    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect =  text_surf.get_rect(center=text_center_position)
        self.window.blit(source=text_surf, dest=text_rect)