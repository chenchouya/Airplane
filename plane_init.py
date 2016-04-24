# coding=utf-8

#####-------------------引入的模块--------------########
from sys import exit

from plane_class_method import *

#####--------------------------------------------########

pygame.init()
pygame.mixer.init()
# 初始化

screen_init = pygame.display.set_mode((960, 600), 0, 32)
# 开始界面的窗口

#####---------初始化各个元素------------------###############

##--------音效-------##		

enemy_explo_sound = load_sound("enemy1_down.mp3")
# 敌机1爆炸音效
plane_explo_sound = load_sound("game_over.mp3")
# 我军飞机坠毁音效
# 使用炸弹时的音效
achievement_sound = load_sound("achievement_sound.mp3")
# 打破记录时的音效

##--------字体--------##
font = load_font(r"wel_font.ttf", 35)

wel_font = load_font(r"wel_font.ttf", 50)
# 欢迎界面字体

##-------图片------------###
background = pygame.image.load(r'ui/shoot_background/bg00.jpg').convert()
# 背景图片
game_over_bg = pygame.image.load(r"ui/shoot_background/game_over_bg.jpg")
# 游戏结束背景图片
# 我军飞机图片载入
pause_game = pygame.image.load(r"ui/shoot/game_pause_nor.png").convert_alpha()
# 游戏暂停图标
continue_game = pygame.image.load(r"ui/shoot/game_resume_nor.png").convert_alpha()
# 游戏继续图标

sound_close = pygame.image.load("ui/bkmusic_close.png").convert_alpha()
sound_play = pygame.image.load("ui/bkmusic_play.png").convert_alpha()
# 音乐开关
enemy1_down1 = pygame.image.load(r"ui/shoot/enemy1_down1.png").convert_alpha()
enemy1_down2 = pygame.image.load(r"ui/shoot/enemy1_down2.png").convert_alpha()
enemy1_down3 = pygame.image.load(r"ui/shoot/enemy1_down3.png").convert_alpha()
# 敌机1爆炸效果

game_restart = wel_font.render("Restart now", True, (0, 0, 0))
small_font = load_font(r"wel_font.ttf", 28)
author = small_font.render("Author:Xie Jun Dong", True, (0, 0, 0))
##---------------------------###


###########################################################

##################开始画面################################


####---------------------检测用户点击选项-----------------#########
while True:
    flag = 0
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if game_begin.get_rect(x=500, y=50).collidepoint(pos):
                flag = 1
            elif game_score.get_rect(x=540, y=100).collidepoint(pos):
                flag = 2
            elif game_help.get_rect(x=580, y=150).collidepoint(pos):
                flag = 3
            elif game_quit.get_rect(x=620, y=200).collidepoint(pos):
                flag = 4
            elif game_music.get_rect(x=660, y=250).collidepoint(pos):
                music_icon = not music_icon
    if flag == 1:
        break
    # 游戏开始
    elif flag == 2:
        high_score = pygame.image.load(r"ui/shoot_background/high_score.jpg")
        screen_init.blit(high_score, (0, 0))
        pygame.display.update()
        caption = wel_font.render("High Score", True, (0, 0, 0))
        screen_init.blit(caption, (620, 100))
        f = open("high_score.txt")
        grade = wel_font.render(f.read(), True, (0, 0, 0))
        screen_init.blit(grade, (620, 200))
        back = wel_font.render("Back", True, (0, 0, 0))
        screen_init.blit(back, (800, 480))
        back_flag = 0
        pygame.display.update()
        while back_flag == 0:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    if 800 < x < 900 and 480 < y < 520:
                        back_flag = 1
        continue

    # 高分榜

    ###------------------------------------------##############################
    elif flag == 3:
        help_font = load_font(r"wel_font.ttf", 30)
        game_help_bg = pygame.image.load(r"ui/shoot_background/help.jpg")

        screen_init.blit(game_help_bg, (0, 0))
        caption = help_font.render("Help", True, (0, 0, 0))
        help1 = help_font.render("Move your mouse to control the plane.", True, (0, 0, 0))
        help2 = help_font.render("Press Key_space to launch a bomb.", True, (0, 0, 0))
        help3 = help_font.render("Press v to stop.", True, (0, 0, 0))
        help_back = help_font.render("Back", True, (0, 0, 0))
        screen_init.blit(caption, (400, 40))
        screen_init.blit(help1, (100, 100))
        screen_init.blit(help2, (100, 160))
        screen_init.blit(help3, (100, 220))
        screen_init.blit(help_back, (800, 480))

        pygame.display.update()
        back_flag = 0
        while back_flag == 0:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    if 800 < x < 900 and 480 < y < 520:
                        back_flag = 1

        # draw_begin_bg(bg_begin, game_begin, game_score, game_help, game_quit, game_music, sound_play_icon)
        continue

    # 帮助
    elif flag == 4:
        exit()
    draw_begin_bg(bg_begin, game_begin, game_score, game_help, game_quit, game_music, sound_play)
# 游戏结束

###########################################################

