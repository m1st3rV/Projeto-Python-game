#C
import pygame

COLOR_BLACK= (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

#E
EVENT_ENEMY = pygame.USEREVENT +1
ENTITY_SPEED = {'nature_1_0': 0,
                'nature_1_1': 0,
                'nature_1_2': 1,
                'nature_1_3': 2,
                'nature_1_4': 3,
                'nature_1_5': 4,
                'nature_1_6': 4,
                'nature_1_7': 3,
                'Player': 3,
                'Enemy1': 2,
                'Enemy2': 1}

ENTITY_HEALTH = {
                'nature_1_0': 999,
                'nature_1_1': 999,
                'nature_1_2': 999,
                'nature_1_3': 999,
                'nature_1_4': 999,
                'nature_1_5': 999,
                'nature_1_6': 999,
                'nature_1_7': 999,
                'Player': 500,
                'Enemy1': 100,
}



#H


#M

#MENU_OPTION1 = 'NEW GAME'
#MENU_OPTION2 = 'CONTINUE'
#MENU_OPTION3 = 'EXIT'
MENU_OPTION = ('NEW GAME','COMPETITIVE', 'COOPERATIVE', 'SCORE','EXIT')


#S
SPAWN_TIME = 5500

#W

WIN_WIDTH = 576
WIN_HEIGHT = 324