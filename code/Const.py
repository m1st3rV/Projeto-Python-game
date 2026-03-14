import pygame


#C


COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN_LIME = (50, 205, 50)
COLOR_BLUE = (0, 0, 255)

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
                'nature_4_0': 0,
                'nature_4_1': 1,
                'nature_4_2': 2,
                'nature_4_3': 3,
                'Player': 3,
                'Enemy1': 1,
                'PlayerShot': 1,
                'Enemy1Shot': 2}

ENTITY_HEALTH = {
                'nature_1_0': 999,
                'nature_1_1': 999,
                'nature_1_2': 999,
                'nature_1_3': 999,
                'nature_1_4': 999,
                'nature_1_5': 999,
                'nature_1_6': 999,
                'nature_1_7': 999,
                'nature_4_0': 999,
                'nature_4_1': 999,
                'nature_4_2': 999,
                'nature_4_3': 999,
                'Enemy1Shot': 1,
                'PlayerShot': 1,
                'Player': 200,
                'Enemy1': 50,
}

ENTITY_SHOT_DELAY = {'Player':15,
                     'Enemy1':200}


ENTITY_DAMAGE =  {
                'nature_1_0': 0,
                'nature_1_1': 0,
                'nature_1_2': 0,
                'nature_1_3': 0,
                'nature_1_4': 0,
                'nature_1_5': 0,
                'nature_1_6': 0,
                'nature_1_7': 0,
                'nature_4_0': 0,
                'nature_4_1': 0,
                'nature_4_2': 0,
                'nature_4_3': 0,
                'Enemy1Shot': 10,
                'PlayerShot': 10,
                'Player': 50,
                'Enemy1': 50,
}

ENTITY_SCORE =  {
                'nature_1_0': 0,
                'nature_1_1': 0,
                'nature_1_2': 0,
                'nature_1_3': 0,
                'nature_1_4': 0,
                'nature_1_5': 0,
                'nature_1_6': 0,
                'nature_1_7': 0,
                'nature_4_0': 0,
                'nature_4_1': 0,
                'nature_4_2': 0,
                'nature_4_3': 0,
                'Enemy1Shot': 0,
                'PlayerShot': 0,
                'Player': 0,
                'Enemy1': 100,
}

EVENT_TIMEOUT = pygame.USEREVENT + 2


#F

#FISICA_PLAYER
GRAVITY = 0.5
JUMP_FORCE = -10



#H

#L

LEVEL_CONFIG = {'Level1' :{'bg': 'nature_1', 'music': 'level1.wav'},
                 'Level2': {'bg': 'nature_4', 'music': 'level2.wav' } }

#M

#MENU_OPTION1 = 'NEW GAME'
#MENU_OPTION2 = 'CONTINUE'
#MENU_OPTION3 = 'EXIT'
MENU_OPTION = ('NEW GAME','COMPETITIVE', 'COOPERATIVE', 'SCORE','EXIT')


#S
SPAWN_TIME = 6500



#T
TIMEOUT_TIME = 40000
TIMEOUT_TAX = 100


#W

WIN_WIDTH = 576
WIN_HEIGHT = 324