#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION  #CASO NÃO QUEIRA INFORMAR DIMENSÕES POR UM ARQUIVO ESPECÍFICO APAGAR ESSA LINHA
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH,WIN_HEIGHT))
    
    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:  # MENU OPTION NEW GAME
                pass
            elif menu_return == MENU_OPTION[2]:  # MENU OPTION EXIT
                pygame.quit()
                quit() #END PYGAME
            else:
                pass


