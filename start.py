#coding=utf-8
from GameActivity import *
from HelpActivity import *
from MainActivity import *
from RestartActivity import *
from ScoreActivity import *

if __name__ == "__main__":
    pygame.init()
    # 初始化

    pygame.event.post(pygame.event.Event(constants.WELCOME_SCREEN_EVENT))
    while True:
        for event in pygame.event.get():
            if event.type == constants.WELCOME_SCREEN_EVENT:
                welcome_screen = pygame.display.set_mode(constants.wel_window_size, 0, 32)
                MainActivity(welcome_screen, constants.main_background_fn).run()
            elif event.type == constants.SHOW_HELP_EVENT:
                help_screen = pygame.display.set_mode(constants.wel_window_size, 0, 32)
                HelpActivity(help_screen, constants.help_background_fn).run()
            elif event.type == constants.HIGH_SCORE_EVENT:
                high_score_screen = pygame.display.set_mode(constants.wel_window_size, 0, 32)
                ScoreActivity(high_score_screen, constants.highscore_background_fn).run()
            elif event.type == constants.BEGIN_GAME_EVENT:
                game_screen = pygame.display.set_mode(constants.game_window_size, 0, 32)
                GameActivity(game_screen, constants.game_background_fn).run()
            elif event.type == constants.RESTART_EVENT:
                restart_screen = pygame.display.set_mode(constants.wel_window_size, 0, 32)
                RestartActivity(restart_screen, constants.game_over_bg_fn).run()
            elif event.type == QUIT:
                pygame.quit()
                exit()



