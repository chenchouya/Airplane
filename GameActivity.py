# coding=utf-8
from activity import *
from plane_class_method import *


class GameActivity(Activity):
    def __init__(self, screen, background_fn):
        Activity.__init__(self, screen, background_fn)

        self.enemy_explo_sound = load_sound(constants.enemy_explo_sound_fn)
        # 敌机1爆炸音效
        self.plane_explo_sound = load_sound(constants.plane_explo_sound_fn)
        # 我军飞机坠毁音效
        self.achievement_sound = load_sound(constants.achievement_sound_fn)
        # 打破记录时的音效
        self.game_bgm = load_sound(constants.game_bgm_fn)
        self.font = load_font(constants.font_fn, constants.font_size)
        self.show_score_font = load_font(constants.show_score_font_fn, 50)
        self.lose_a_life = False

    def setup(self):
        self.allSprites = MyGroup()
        self.enemy_group = pygame.sprite.RenderPlain()

        ##-------子弹------####
        self.bullet_group = pygame.sprite.RenderPlain()
        # 子弹数量
        ##---------炸弹-------####

        # 生成炸弹
        self.bomb_group = pygame.sprite.RenderPlain()
        self.bomb_location_group = ((20, 700), (50, 700), (80, 700), (110, 700))
        self.Bomb_icon_group = []
        # 创建炸弹图标的列表
        for lo in self.bomb_location_group:
            self.Bomb_icon_group.append(BombIcon(lo))
        # 初始化炸弹图标列表

        ##--------本机--------####
        self.plane = Plane()
        self.plane.add(self.allSprites)
        # 生成本机
        self.plane_location_group = ((392, 700), (423, 700), (453, 700))
        self.plane_icon_group = []
        for lo in self.plane_location_group:
            self.plane_icon_group.append(Plane_icon(lo))

        # 初始化飞机图标列表

        self.score = 0
        # 记录分数
        self.pause = False
        self.music_icon = True
        self.gameover = False

    def run(self):
        self.screen.blit(self.background, (0,0))
        self.setup()
        pygame.display.flip()
        pygame.time.set_timer(constants.ENEMY_APPEAR_EVENT, 100)
        pygame.time.set_timer(constants.BULLET_SHOOT_EVENT, 100)
        while True:
            self.clock.tick(MAXFPS)
            self.handle_events()
            self.detect_collision()
            self.draw_spirites()
            if self.quit:
                self.finished()
                break
            if self.changed:
                self.screen.blit(self.background, (0,0))
                self.on_change()
                pygame.display.flip()
            self.changed = False

    def handle_events(self):
        self.screen.blit(self.background, (0,0))
        for event in self.get_event():
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE and len(self.bomb_group) < 4:
                    Bomb().add(self.bomb_group, self.allSprites)
                    # 如果按下空格键，那么发射一枚炸弹,播放音效
                    if len(self.Bomb_icon_group) > 0:
                        self.Bomb_icon_group.pop(-1)
                if event.key == K_v:
                    if not self.pause:
                        self.allSprites.suspend()
                        self.game_bgm.stop()
                    else:
                        self.game_bgm.play(loops=-1)
                        self.allSprites.recover()
                    self.pause = not self.pause

            elif event.type == constants.ENEMY_APPEAR_EVENT:
                Enemy().add(self.enemy_group, self.allSprites)
            elif event.type == constants.BULLET_SHOOT_EVENT and len(self.bullet_group) <= 5:
                Bullet().add(self.bullet_group, self.allSprites)



    def detect_collision(self):
        if not self.gameover and not self.pause:
            # 绘制背景

            for enemy in pygame.sprite.groupcollide(self.enemy_group, self.bullet_group, 1, 1).keys():
                enemy.explode()
                self.enemy_explo_sound.play()
                self.score += 100

            for enemy in pygame.sprite.groupcollide(self.enemy_group, self.bomb_group, 1, 1).keys():
                enemy.explode()
                self.score += 200

            for e in self.enemy_group.sprites():
                if pygame.sprite.collide_mask(self.plane, e):
                    self.plane.life -= 1
                    e.kill()
                    self.pause = True
                    break

        if self.plane.life <= 0:
            self.plane.kill()
            self.game_bgm.stop()
            self.update_highscore()
            self.show_score()
            pygame.time.set_timer(constants.ENEMY_APPEAR_EVENT, 0)
            pygame.time.set_timer(constants.BULLET_SHOOT_EVENT, 0)
            pygame.event.post(pygame.event.Event(constants.RESTART_EVENT))
            self.quit = True

    def draw_spirites(self):
            #draw spirites
        if not self.pause:
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
        pygame.time.set_timer(constants.ENEMY_APPEAR_EVENT, 0)
        pygame.time.set_timer(constants.BULLET_SHOOT_EVENT, 0)
