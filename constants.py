#coding=utf-8
from common import *

enemy_explo_sound_fn = "enemy1_down.mp3"
# 敌机1爆炸音效
plane_explo_sound_fn = "game_over.mp3"
# 我军飞机坠毁音效
# 使用炸弹时的音效
achievement_sound_fn = "achievement_sound.mp3"
# 打破记录时的音效
game_bgm_fn = "game_music.mp3"

##--------字体--------##
font_fn = r"wel_font.ttf"
font_size = 35

wel_font_fn = r"wel_font.ttf"
wel_font_size = 50

show_score_font_fn = r"wel_font.ttf"
# 欢迎界面字体

##-------图片------------###
main_background_fn = os.path.join("shoot_background", "bg_begin.jpg")
game_background_fn = os.path.join('shoot_background', 'bg00.jpg')
help_background_fn = "shoot_background/help.jpg"
highscore_background_fn = "shoot_background/high_score.jpg"
# 背景图片
game_over_bg_fn = os.path.join("shoot_background", "game_over_bg.jpg")
# 游戏结束背景图片
# 我军飞机图片载入
pause_game_fn = r"shoot/game_pause_nor.png"
# 游戏暂停图标
continue_game_fn = r"shoot/game_resume_nor.png"
# 游戏继续图标

sound_close_fn = "bkmusic_close.png"
sound_play_icon_fn = "bkmusic_play.png"
# 音乐开关
enemy1_down1_fn = r"shoot/enemy1_down1.png"
enemy1_down2_fn = r"shoot/enemy1_down2.png"
enemy1_down3_fn = r"shoot/enemy1_down3.png"
# 敌机1爆炸效果

# game_restart = wel_font.render"Restart now", True, 0, 0, 0
# small_font = r"wel_font.ttf", 28
# author = small_font.render"Author:Xie Jun Dong", True, 0, 0, 0
##---------------------------###

#User define events
WELCOME_SCREEN_EVENT = USEREVENT + 1
SHOW_HELP_EVENT = USEREVENT + 2
HIGH_SCORE_EVENT = USEREVENT + 3
QUIT_EVENT = USEREVENT + 4
BEGIN_GAME_EVENT = USEREVENT + 5
ENEMY_APPEAR_EVENT = USEREVENT + 6
BULLET_SHOOT_EVENT = USEREVENT + 7
RESTART_EVENT = USEREVENT
