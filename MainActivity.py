#coding=utf-8
import constants
from activity import *


class MainActivity(Activity):
    def __init__(self, screen, background_fn):
        Activity.__init__(self, screen, background_fn)
        self.font = load_font(constants.wel_font_fn, constants.wel_font_size)
        self.game_begin = self.font.render("Game Begin", True, (0, 0, 0))
        self.game_score = self.font.render("High Score", True, (0, 0, 0))
        self.game_help = self.font.render("Game Help", True, (0, 0, 0))
        self.game_quit = self.font.render("Game Quit", True, (0, 0, 0))
        # self.game_music = self.font.render("Music", True, (0, 0, 0))
        # self.sound_play_icon = load_image(constants.sound_play_icon_fn, alpha=True)[0]
        # self.music_icon = True

    def setup(self):
        pygame.display.set_caption("shoot!shoot!shoot!")
        # 标题
        # bg_begin = pygame.image.load(r"ui/shoot_background/bg_begin.jpg")

    def run(self):
        self.screen.blit(self.background, (0, 0))
        self.setup()
        # 画背景
        self.screen.blit(self.game_begin, self.game_begin.get_rect(x=500, y=50))
        self.screen.blit(self.game_score, self.game_score.get_rect(x=540, y=100))
        self.screen.blit(self.game_help, self.game_help.get_rect(x=580, y=150))
        self.screen.blit(self.game_quit, self.game_quit.get_rect(x=620, y=200))
        # self.screen.blit(self.game_music, self.game_music.get_rect(x=660, y=250))
        # 画出四个选项
        # self.screen.blit(self.sound_play_icon, (810, 250))

        pygame.display.flip()
        while True:
            self.clock.tick(MAXFPS)
            if self.finished_:
                self.finished()
            else:
                pass
            self.handle_events()
            if self.quit:
                break
            if self.changed:
                self.screen.blit(self.background, (0,0))
                self.on_change()
                pygame.display.flip()
            self.changed = False

    def handle_events(self):
        for event in self.get_event():
            if event.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if self.game_begin.get_rect(x=500, y=50).collidepoint(pos):
                    pygame.event.post(pygame.event.Event(constants.BEGIN_GAME_EVENT))
                    self.quit = True
                    break
                elif self.game_score.get_rect(x=540, y=100).collidepoint(pos):
                    pygame.event.post(pygame.event.Event(constants.HIGH_SCORE_EVENT))
                    self.quit = True
                    break
                elif self.game_help.get_rect(x=580, y=150).collidepoint(pos):
                    pygame.event.post(pygame.event.Event(constants.SHOW_HELP_EVENT))
                    self.quit = True
                    break
                elif self.game_quit.get_rect(x=620, y=200).collidepoint(pos):
                    pygame.quit()
                    exit()

