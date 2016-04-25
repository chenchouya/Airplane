# coding=utf-8
from activity import *
from plane_class_method import *


class GameActivity(Activity):
    MAXFPS = 200

    def __init__(self, screen, background_fn):
        Activity.__init__(self, screen, background_fn)

        self.achievement_sound = load_sound(constants.achievement_sound_fn)
        # 打破记录时的音效
        self.game_bgm = load_sound(constants.game_bgm_fn)
        self.takeoff_sound = load_sound(constants.takeoff_sound_fn)
        self.bullet_sound = load_sound(constants.launch_bullet_sound_fn)
        self.short_boom_sound = load_sound(constants.short_boom_sound_fn)
        self.great_boom_sound = load_sound(constants.great_boom_sound_fn)
        self.launch_bomb_sound = load_sound(constants.launch_bomb_sound_fn)
        self.baozou_sound = load_sound(constants.plane_thrash_sound_fn)
        self.plane_explode_sound = load_sound(constants.plane_explo_sound_fn)
        self.enemy3_appear_sound = load_sound(constants.enemy3_appear_sound_fn)

        # font
        self.font = load_font(constants.font_fn, constants.font_size)
        self.show_score_font = load_font(constants.show_score_font_fn, 50)
        self.lose_a_life = False
        self.collide_mask = pygame.sprite.collide_mask

        self._life_count = 0

    def setup(self):

        self.allSprites = MyGroup()
        self.enemy1_group = pygame.sprite.RenderPlain()
        self.enemy2_group = pygame.sprite.RenderPlain()
        self.enemy3_group = pygame.sprite.RenderPlain()
        self.all_enemies = pygame.sprite.RenderPlain()
        self.no_colli_group = pygame.sprite.RenderPlain()

        self.bullet_group = pygame.sprite.RenderPlain()
        self.bullet1_group = pygame.sprite.RenderPlain()
        self.bullet2_group = pygame.sprite.RenderPlain()
        self.bullet3_group = pygame.sprite.RenderPlain()

        self.enemy_bullets = pygame.sprite.RenderPlain()

        ##---------炸弹-------####
        self.bomb_group = pygame.sprite.RenderPlain()
        bomb_icon_y = self.screen.get_rect().height - 175
        self.bomb_location_group = ((20, bomb_icon_y), (50, bomb_icon_y), (80, bomb_icon_y), (110, bomb_icon_y))

        self.Bomb_icon_group = [BombIcon(x) for x in self.bomb_location_group]
        # 创建炸弹图标的列表

        self.plane = Plane()
        self.plane.add(self.allSprites)

        plane_icon_y = self.screen.get_rect().height - 175
        self.plane_location_group = ((388, plane_icon_y), (388 + 30, plane_icon_y), (388 + 60, plane_icon_y))
        self.plane_icon_group = [Plane_icon(x) for x in self.plane_location_group]

        # 初始化飞机图标列表
        self.ufo1 = UFO1()
        self.ufo2 = UFO2()
        self.ufo1_group = pygame.sprite.RenderPlain()
        self.ufo2_group = pygame.sprite.RenderPlain()
        self.ufo_group = pygame.sprite.RenderPlain()
        self.ufo1.add(self.ufo_group, self.ufo1_group, self.allSprites)
        self.ufo2.add(self.ufo_group, self.ufo2_group, self.allSprites)

        self.score = 0
        # 记录分数
        self.pause = False
        self.music_icon = True
        self.gameover = False

        # set volume
        self.game_bgm.set_volume(0.8)
        self.bullet_sound.set_volume(0.2)
        self.great_boom_sound.set_volume(0.5)
        self.short_boom_sound.set_volume(0.5)
        self.enemy3_appear_sound.set_volume(1.0)

        Enemy.enemy_down1_pic = load_image(constants.enemy1_down1_fn, alpha=True)[0]
        Enemy.enemy_down2_pic = load_image(constants.enemy1_down2_fn, alpha=True)[0]
        Enemy.enemy_down3_pic = load_image(constants.enemy1_down3_fn, alpha=True)[0]
        Enemy.enemy_down4_pic = load_image(constants.enemy1_down4_fn, alpha=True)[0]
        Enemy2.enemy_down1_pic = load_image(constants.enemy1_down1_fn, alpha=True)[0]
        Enemy2.enemy_down2_pic = load_image(constants.enemy1_down2_fn, alpha=True)[0]
        Enemy2.enemy_down3_pic = load_image(constants.enemy1_down3_fn, alpha=True)[0]
        Enemy2.enemy_down4_pic = load_image(constants.enemy1_down4_fn, alpha=True)[0]
        Enemy3.enemy_down1_pic = load_image(constants.enemy1_down1_fn, alpha=True)[0]
        Enemy3.enemy_down2_pic = load_image(constants.enemy1_down2_fn, alpha=True)[0]
        Enemy3.enemy_down3_pic = load_image(constants.enemy1_down3_fn, alpha=True)[0]
        Enemy3.enemy_down4_pic = load_image(constants.enemy1_down4_fn, alpha=True)[0]

        pygame.mouse.set_visible(False)

    # def enemy1_2_appear(self):
    #     if not self.pause:
    #         if len(self.enemy1_group) <= self.max_enemy1:
    #             Enemy().add(self.enemy1_group, self.all_enemies, self.allSprites, self.no_colli_group)
    #         if random.randint(1, 10) > 6 and len(self.enemy2_group) <= self.max_enemy2:
    #             Enemy2().add(self.enemy2_group, self.all_enemies, self.allSprites, self.no_colli_group)
    #             self.enemy3_appear_sound.play()
    #     threading.Timer(0.5, self.enemy1_2_appear, ())

    def run(self):
        self.screen.blit(self.background, (0, 0))
        self.setup()
        pygame.display.update()
        pygame.time.set_timer(constants.ENEMY_APPEAR_EVENT, constants.enemy12_interval)
        # self.timer_e1_2 = threading.Timer(0.5, self.enemy1_2_appear, ())
        # self.timer_e1_2.start()
        pygame.time.set_timer(constants.BULLET_SHOOT_EVENT, 250)
        self.timer_ufo1 = threading.Timer(constants.ufo1_interval, self.ufo1_appear, ())
        self.timer_ufo1.start()
        self.timer_ufo2 = threading.Timer(constants.ufo2_interval, self.ufo2_appear, ())
        self.timer_ufo2.start()
        self.timer_e3 = threading.Timer(constants.enemy3_interval, self.enemy3_appear, ())
        self.timer_e3.start()
        self.game_bgm.play(loops=-1)
        while True:
            self.change_level()
            self.clock.tick(MAXFPS)
            self.handle_events()
            self.detect_collision()
            self.check_life_add()
            self.draw_spirites()
            if self.quit:
                self.finished()
                pygame.time.wait(2000)
                break
                # if self.changed:
                #     self.screen.blit(self.background, (0, 0))
                #     self.on_change()
                #     pygame.display.flip()
                # self.changed = False

    def handle_events(self):
        for event in self.get_event():
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE and len(self.bomb_group) < 4:
                    if len(self.Bomb_icon_group) > 0:
                        Bomb().add(self.bomb_group, self.allSprites)
                        self.Bomb_icon_group.pop(-1)
                        self.score += 500
                        # 如果按下空格键，那么发射一枚炸弹,播放音效
                if event.key == K_v:
                    if not self.pause:
                        self.allSprites.suspend()
                        pygame.mixer.pause()
                    else:
                        pygame.mixer.unpause()
                        self.allSprites.recover()
                    self.pause = not self.pause
                if self.pause:
                    self.allSprites.suspend()
                    pygame.mixer.pause()

            elif event.type == constants.ENEMY_APPEAR_EVENT:
                if not self.pause:
                    if len(self.enemy1_group) <= self.max_enemy1:
                        Enemy().add(self.enemy1_group, self.all_enemies, self.allSprites, self.no_colli_group)
                    if random.randint(1, 10) > 6 and len(self.enemy2_group) <= self.max_enemy2:
                        Enemy2().add(self.enemy2_group, self.all_enemies, self.allSprites, self.no_colli_group)
                        self.enemy3_appear_sound.play()

            elif event.type == constants.BULLET_SHOOT_EVENT:
                if not self.pause:
                    if len(self.bullet1_group) <= 5:
                        Bullet1().add(self.bullet1_group, self.bullet_group, self.allSprites)
                    if self.plane.has_bullet2 and len(self.bullet2_group) <= len(self.enemy2_group):
                        Bullet2(self.plane.rect.bottomleft).add(self.bullet2_group, self.bullet_group, self.allSprites)
                        Bullet2(self.plane.rect.bottomright).add(self.bullet2_group, self.bullet_group, self.allSprites)
                    if self.plane.has_bullet3 and len(self.bullet3_group) < 10:
                        Bullet3(self.plane.rect.topleft, direction=False).add(self.bullet3_group, self.bullet_group,
                                                                              self.allSprites)
                        Bullet3(self.plane.rect.topright, direction=True).add(self.bullet3_group, self.bullet_group,
                                                                              self.allSprites)

                    self.bullet_sound.play()

    def detect_collision(self):
        self.screen.blit(self.background, (0, 0))
        if not self.gameover and not self.pause:

            for enemy in pygame.sprite.groupcollide(self.all_enemies, self.bullet_group, 0, 1,
                                                    self.collide_mask).keys():
                enemy.explode()
                self.short_boom_sound.play()
                self.score += 100

            for bomb, enemies in pygame.sprite.groupcollide(self.bomb_group, self.all_enemies, 0, 0,
                                                            self.collide_mask).items():
                bomb.explode()
                for enemy in enemies:
                    enemy.explode()
                self.great_boom_sound.play()

            for e in self.no_colli_group.sprites():
                if pygame.sprite.collide_mask(self.plane, e):
                    self.plane.explode()
                    for s in self.no_colli_group.sprites():
                        s.kill()
                    if len(self.plane_icon_group) > 0:
                        self.plane_icon_group.pop(0)
                    e.explode()
                    if self.plane.life > 0:
                        self.continue_tip = self.font.render("Press v to continue", True, (0, 0, 0))
                        self.screen.blit(self.continue_tip, (40, 500))
                        pygame.display.update()
                    self.plane_explode_sound.play()
                    self.great_boom_sound.play()
                    self.pause = True
                    break

            for ufo in pygame.sprite.spritecollide(self.plane, self.ufo_group, 0, collided=pygame.sprite.collide_mask):
                if ufo in self.ufo1_group:
                    ufo.restart()
                    self.plane.has_bullet2 = True
                    self.baozou_sound.play()
                    self.plane.reset_bullet2_timer()
                    threading.Timer(constants.bullet2_last, self.plane.lose_bullet2, ()).start()
                elif ufo in self.ufo2_group:
                    ufo.restart()
                    self.plane.has_bullet3 = True
                    self.baozou_sound.play()
                    self.plane.reset_bullet3_timer()
                    threading.Timer(constants.bullet3_last, self.plane.lose_bullet3, ()).start()

        if self.plane.life <= 0:
            self.plane.kill()
            self.game_bgm.stop()
            self.update_highscore()
            self.show_score()
            self.quit = True

    def draw_spirites(self):
        if not self.pause:
            for e in self.all_enemies.sprites():
                if e.launch_bullet:
                    EnemyBullet(e.rect.center).add(self.enemy_bullets, self.allSprites, \
                                                   self.no_colli_group)
                    e.launch_bullet = False
                    self.bullet_sound.play()

            for e in self.enemy3_group.sprites():
                e.get_player_pos(self.plane)

            self.allSprites.update()
            self.allSprites.draw(self.screen)
            for bomb_list in self.Bomb_icon_group:
                self.screen.blit(bomb_list.image, bomb_list.rect)

            for plane_list in self.plane_icon_group:
                self.screen.blit(plane_list.image, plane_list.rect)
            # 绘制炸弹图标和我军飞机小图标

            text = self.font.render("Score: %d" % self.score, 1, (0, 0, 100))
            self.screen.blit(text, (0, 0))
            pygame.display.update()

    def change_level(self):
        if self.score > 2000:
            self.max_enemy1 = 5
            self.max_enemy2 = 3
            self.max_enemy3 = 1
        elif self.score > 4000:
            self.max_enemy1 = 6
            self.max_enemy2 = 2
            self.max_enemy3 = 2
        elif self.score > 10000:
            self.max_enemy1 = 8
            self.max_enemy2 = 4
            self.max_enemy3 = 3
            constants.enemy3_chongci_dis = 400
        elif self.score > 20000:
            self.max_enemy1 = 2
            self.max_enemy2 = 10
            self.max_enemy3 = 3
        elif self.score > 30000:
            self.max_enemy1 = 8
            self.max_enemy2 = 8
            self.max_enemy3 = 5
            constants.ufo1_interval = 23.0
            constants.ufo2_interval = 33.0
            constants.enemy3_interval = 5.0
            constants.enemy3_chongci_dis = 300
        elif self.score > 40000:
            self.max_enemy1 = 5
            self.max_enemy2 = 10
            self.max_enemy3 = 7
        elif self.score > 50000:
            self.max_enemy1 = 2
            self.max_enemy2 = 12
            self.max_enemy3 = 10
            constants.enemy3_chongci_dis = 250
        elif self.score > 80000:
            self.max_enemy1 = 10
            self.max_enemy2 = 12
            self.max_enemy3 = 10
            constants.ufo1_interval = 30.0
            constants.ufo2_interval = 28.0
            constants.enemy3_interval = 3.0
            constants.enemy3_chongci_dis = 200
        elif self.score > 100000:
            self.max_enemy1 = 10
            self.max_enemy2 = 15
            self.max_enemy3 = 15
            constants.ufo1_interval = 28.0
            constants.ufo2_interval = 40.0
            constants.enemy3_interval = 3.0
            constants.enemy3_chongci_dis = 180
        elif self.score > 150000:
            self.max_enemy1 = 20
            self.max_enemy2 = 20
            self.max_enemy3 = 20
            constants.ufo1_interval = 40.0
            constants.ufo2_interval = 40.0
            constants.enemy3_interval = 2.0
            constants.enemy3_chongci_dis = 220
        elif self.score > 200000:
            self.max_enemy1 = 40
            self.max_enemy2 = 40
            self.max_enemy3 = 40
            constants.ufo1_interval = 40.0
            constants.ufo2_interval = 40.0
            constants.enemy3_interval = 1.0
            constants.enemy3_chongci_dis = 220
        else:
            self.max_enemy1 = 8
            self.max_enemy2 = 1
            self.max_enemy3 = 3
            constants.enemy3_chongci_dis = 500

    def ufo1_appear(self):
        self.ufo1.active = True
        threading.Timer(constants.ufo1_interval, self.ufo1_appear, ()).start()

    def ufo2_appear(self):
        self.ufo2.active = True
        threading.Timer(constants.ufo2_interval, self.ufo2_appear, ()).start()

    def enemy3_appear(self):
        if len(self.enemy3_group) <= self.max_enemy3:
            Enemy3().add(self.enemy3_group, self.all_enemies, self.allSprites, self.no_colli_group)
        threading.Timer(constants.enemy3_interval, self.enemy3_appear, ()).start()

    def update_highscore(self):

        with open("high_score.txt", "r") as f:
            scores = f.readlines()
        scores = map(lambda x: int(x.strip()), scores)

        if len(scores) > 0 and self.score > max(scores):
            break_score = self.font.render("WOW,Break the score!", 1, (100, 100, 0))
            self.achievement_sound.play()
            self.screen.blit(break_score, (50, 300))

        if len(scores) > 0 and self.score > min(scores):
            scores.append(self.score)
            scores.sort(reverse=True)
            scores = scores[:10]

        scores = [str(x) + "\n" for x in scores]
        with open("high_score.txt", 'w') as f:
            f.writelines(scores)

            # 将最高分写入文件

    def show_score(self):
        score_get = self.show_score_font.render("The score is %d" % self.score, 1, (80, 90, 205))
        self.screen.blit(score_get, (30, 500))
        pygame.display.update()

    def finished(self):
        pygame.mouse.set_visible(True)
        pygame.time.set_timer(constants.ENEMY_APPEAR_EVENT, 0)
        pygame.time.set_timer(constants.BULLET_SHOOT_EVENT, 0)

        self.timer_ufo1.cancel()
        self.timer_ufo2.cancel()
        self.timer_e3.cancel()
        pygame.event.set_blocked([constants.ENEMY_APPEAR_EVENT, constants.BULLET_SHOOT_EVENT])
        pygame.event.post(pygame.event.Event(constants.RESTART_EVENT))

    def check_life_add(self):

        if self.score / 100000 > self._life_count:
            self.add_life()
            self._life_count = self.score / 100000

    def add_life(self):
        if self.plane.life < 3:
            self.plane.life += 1
            self.plane_icon_group.insert(0, Plane_icon(self.plane_location_group[2 - len(self.plane_icon_group)]))

    def get_event(self):
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                self.finished()
                pygame.quit()
                exit()
        return events
