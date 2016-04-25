#!/usr/bin/env python
# coding=utf-8

from plane_init import *

screen = pygame.display.set_mode((480, 852), 0, 32)
# 绘制屏幕
game_bgm = load_sound("game_music.mp3")

if music_icon:
    game_bgm.play(loops=-1)
# 播放背景音乐

clock = pygame.time.Clock()
while 1:
    # clock.tick(400)
    # enemy_add_speed(enemy1_group, score)
    interval_e -= 1
    interval_b -= 1
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE and len(bomb_group) < 4:
                Bomb().add(bomb_group, allSprites)
                # 如果按下空格键，那么发射一枚炸弹,播放音效
                if len(Bomb_icon_group) > 0:
                    Bomb_icon_group.pop(-1)
            if event.key == K_v:
                if not pause:
                    allSprites.suspend()
                    game_bgm.stop()
                else:
                    game_bgm.play(loops=-1)
                    allSprites.recover()
                pause = not pause

    if not gameover and not pause:
        screen.blit(background, (0, 0))
        # 绘制背景
        screen.blit(pause_game, (420, 5))

        if interval_b < 0 and len(bullet_group) <= 5:
            Bullet().add(bullet_group, allSprites)
            interval_b = 100
            # 重置间隔时间
        if interval_e < 0:
            Enemy().add(enemy_group, allSprites)
            interval_e = 1000

        for enemy in pygame.sprite.groupcollide(enemy_group, bullet_group, 1, 1).keys():
            enemy.explode()
            enemy_explo_sound.play()
            score += 100

        for enemy in pygame.sprite.groupcollide(enemy_group, bomb_group, 1, 1).keys():
            enemy.explode()

        for e in enemy_group.sprites():
            if pygame.sprite.collide_mask(plane, e):
                gameover = True

        #draw spirites
        allSprites.update()
        allSprites.draw(screen)

        for bomb_list in Bomb_icon_group:
            screen.blit(bomb_list.image, bomb_list.rect)

        for plane_list in plane_icon_group:
            screen.blit(plane_list.image, plane_list.rect)
        # 绘制炸弹图标和我军飞机小图标

        text = font.render("Score: %d" % score, 1, (0, 0, 100))
        screen.blit(text, (0, 0))
        pygame.display.update()
    # 显示分数在左上角

    # 如果阵亡了
    else:
        game_bgm.stop()
        f_score = open("high_score.txt")
        top_score = int(f_score.readline())
        f_score.close()
        f_score = open("high_score.txt", 'w')
        # 将最高分写入文件
        if score > top_score:
            f_score.write(str(score))
            f_score.close()
            break_score = font.render("WOW,Break the score!", 1, (100, 100, 0))
            achievement_sound.play()
            screen.blit(break_score, (50, 300))
        else:
            f_score.write(str(top_score))
            f_score.close()
        font2 = pygame.font.Font(getcwd() + r"/font/wel_font.ttf", 50)
        score_get = font2.render("The score is %d" % score, 1, (80, 90, 205))
        screen.blit(score_get, (30, 500))
        pygame.display.update()
    # 在屏幕中央显示您的得分
    if life == 0:
        game_bgm.stop()
        screen_end = pygame.display.set_mode((960, 600), 0, 32)
        screen_end.blit(game_over_bg, (0, 0))
        screen_end.blit(game_restart, (78, 58))
        screen_end.blit(game_quit, (600, 240))
        screen_end.blit(author, (640, 400))

        pygame.display.update()
        flag_restart = 0
        while flag_restart == 0:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 600 < x < 860 and 240 < y < 300:
                        exit()
                    elif 78 < x < 400 and 58 < y < 118:
                        flag_restart = 1
        life = 3
        screen = pygame.display.set_mode((480, 852), 0, 32)
        game_bgm.play()

    if gameover and event.type == pygame.MOUSEBUTTONUP and life > 0:
        # 如果按下鼠标
        life -= 1
        if music_icon:
            game_bgm.play()
        plane.restart()
        enemy_group.empty()
        bullet_group.empty()
        for lo in bomb_location_group:
            Bomb_icon_group.append(BombIcon(lo))

        # 重启各个元素
        score = 0

        pause = False
        gameover = False
        interval_e = 1000
        interval_b = 100
