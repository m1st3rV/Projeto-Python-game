import datetime
from datetime import datetime
import sys
import pygame
import os
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import COLOR_GREEN_LIME, WIN_WIDTH, MENU_OPTION
from code.DBProxy import DBProxy


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load(os.path.join('./asset/nature_6/orig.png')).convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.menu_option = 0

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/music/level1.wav')  # FILE PATH
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(50, 'FIM DE JOGO', COLOR_GREEN_LIME, (WIN_WIDTH / 2, 50))
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            if game_mode == MENU_OPTION[0] or game_mode == MENU_OPTION[1]:
                score = player_score[0]
                text = 'ENTER YOUR NAME (MAX 10 CHARACTERS)'
            if game_mode == MENU_OPTION[2]:
                while True:
                    self.score_text(50, 'FIM DE JOGO', COLOR_GREEN_LIME, (WIN_WIDTH / 2, 50))
                    self.score_text(30, 'Modo cooperativo não registra pontuação', COLOR_GREEN_LIME,
                                    (WIN_WIDTH / 2, 150))
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    return  # encerra aqui, sem salvar nada
            self.score_text(35, text, COLOR_GREEN_LIME, (WIN_WIDTH / 2, 90))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) > 0:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 10 and event.unicode.isprintable():
                            name += event.unicode

            self.score_text(35, name, COLOR_GREEN_LIME, (WIN_WIDTH / 2, 120))

            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load('./asset/music/level1.wav')  # FILE PATH
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(50, 'TOP 10 SCORE', COLOR_GREEN_LIME, (WIN_WIDTH / 2, 50))
        self.score_text(40, 'NOME            SCORE              DATA', COLOR_GREEN_LIME, (WIN_WIDTH / 2, 80))
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for i, player_score in enumerate(list_score):
            id_, name, score, date = player_score
            self.score_text(25, f'{name}         {score: 05d}         {date}', COLOR_GREEN_LIME, (WIN_WIDTH / 2, 120 + i * 30))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            pygame.display.flip()


    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect =  text_surf.get_rect(center=text_center_position)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime  = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%m/%d/%Y")
    return f"{current_time} - {current_date}"