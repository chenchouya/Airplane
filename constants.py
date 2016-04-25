#coding=utf-8
from common import *

##-------图片------------###
myplane_pic = os.path.join("shoot", "my_plane.png")
enemy1_pic = os.path.join("shoot", "enemy1.png")
enemy2_pic = os.path.join("shoot", "enemy3.png")
enemy3_pic = os.path.join("shoot", "enemy3.png")
ufo1_pic = os.path.join("shoot", "ufo1.png")
ufo2_pic = os.path.join("shoot", "ufo2.png")
bullet1_pic = os.path.join("shoot", "bullet1.png")
bullet2_pic = os.path.join("shoot", "bullet2.png")
bullet3_pic = os.path.join("shoot", "bullet1.png")
boom_pic = os.path.join("shoot", "boom.jpg")
bomb_pic = os.path.join("shoot", "bomb.png")

main_background_fn = os.path.join("shoot_background", "bg_begin.jpg")
game_background_fn = os.path.join('shoot_background', 'bg00.jpg')
help_background_fn = os.path.join("shoot_background", "help.jpg")
highscore_background_fn = os.path.join("shoot_background", "high_score.jpg")  # 背景图片
game_over_bg_fn = os.path.join("shoot_background", "game_over_bg.jpg")  # 游戏结束背景图片
# 我军飞机图片载入
pause_game_fn = os.path.join("shoot", "game_pause_nor.png")
# 游戏暂停图标
continue_game_fn = os.path.join("shoot", "game_resume_nor.png")
# 游戏继续图标
sound_close_fn = "bkmusic_close.png"
sound_play_icon_fn = "bkmusic_play.png"
# 音乐开关
enemy1_down1_fn = os.path.join("shoot", "enemy1_down1.png")
enemy1_down2_fn = os.path.join("shoot", "enemy1_down2.png")
enemy1_down3_fn = os.path.join("shoot", "enemy1_down3.png")
enemy1_down4_fn = os.path.join("shoot", "enemy1_down4.png")
# 敌机1爆炸效果
my_plane_down1_fn = os.path.join("shoot", "hero_blowup_n1.png")
my_plane_down2_fn = os.path.join("shoot", "hero_blowup_n2.png")
my_plane_down3_fn = os.path.join("shoot", "hero_blowup_n3.png")
my_plane_down4_fn = os.path.join("shoot", "hero_blowup_n4.png")

enemy_explo_sound_fn = "enemy1_down.mp3"  # 敌机1爆炸音效
plane_explo_sound_fn = "myplane_explode.wav"  # 我军飞机坠毁音效
achievement_sound_fn = "achievement_sound.mp3"  # 打破记录时的音效
game_bgm_fn = "IAM.wav"
takeoff_sound_fn = "波音747.wav"
enemy3_appear_sound_fn = "波音747.wav"
launch_bomb_sound_fn = "daodan.wav"
launch_bullet_sound_fn = "bullet.wav"
plane_thrash_sound_fn = "baozou.wav"
short_boom_sound_fn = "boom_big.wav"
great_boom_sound_fn = "boom_big.wav"


##--------字体--------##
font_fn = r"wel_font.ttf"
font_size = 35

wel_font_fn = r"wel_font.ttf"
wel_font_size = 50

show_score_font_fn = r"wel_font.ttf"
# 欢迎界面字体



# interval
ufo1_interval = 20.0
ufo2_interval = 30.0
enemy12_interval = 250  # ms
enemy3_interval = 10.0
bullet2_last = 10.0
bullet3_last = 10.0

# other
enemy3_chongci_dis = 200
#User define events
WELCOME_SCREEN_EVENT = USEREVENT + 1
SHOW_HELP_EVENT = USEREVENT + 2
HIGH_SCORE_EVENT = USEREVENT + 3
QUIT_EVENT = USEREVENT + 4
BEGIN_GAME_EVENT = USEREVENT + 5
ENEMY_APPEAR_EVENT = USEREVENT + 6
BULLET_SHOOT_EVENT = USEREVENT + 7
RESTART_EVENT = USEREVENT
