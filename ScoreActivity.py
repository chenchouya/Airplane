#coding=utf-8
import constants
from activity import *


class ScoreActivity(Activity):

    def __init__(self, screen, background_fn):
        Activity.__init__(self, screen, background_fn)
        self.screen = screen
        self.background = load_image(background_fn)[0]
        self.font = load_font(constants.font_fn)
        self.caption = self.font.render("High Score", True, (0, 0, 0))
        self.back_btn = self.font.render("Back", True, (0, 0, 0))
        self.score_pos = [620, 200]

    def setup(self):
        self.screen.blit(self.caption, (620, 100))
        f = open("high_score.txt")
        scores = map(lambda x: int(x.strip()), f.readlines())
        scores.sort(reverse=True)
        scores = scores[:5]
        for score in scores:
            score = self.font.render(str(score), True, (0,0,0))
            self.screen.blit(score, self.score_pos)
            self.score_pos[1] += 50

        self.screen.blit(self.back_btn, (800, 480))

    def handle_events(self):
        for event in self.get_event():
            if event.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if self.back_btn.get_rect(x=800, y=480).collidepoint(pos):
                    pygame.event.post(pygame.event.Event(constants.WELCOME_SCREEN_EVENT))
                    self.quit = True
                    break
