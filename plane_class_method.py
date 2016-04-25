# coding=utf-8
import random
import thread
import threading
from os import getcwd

import constants
from common import *


# 定义我机
class Plane(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.plane_down1_img = load_image(constants.my_plane_down1_fn, alpha=True, scale=0.7)[0]
        # self.plane_down2_img = load_image(constants.my_plane_down2_fn, alpha=True, scale=0.7)[0]
        # self.plane_down3_img = load_image(constants.my_plane_down3_fn, alpha=True, scale=0.7)[0]
        # self.plane_down4_img = load_image(constants.my_plane_down4_fn, alpha=True, scale=0.7)[0]
        self.screen = pygame.display.get_surface()
        self.life = 3
        self.restart()

    def explode(self):
        self.life -= 1
        self.stop = True
        self.rect.center = (2000, 2000)
        # thread.start_new_thread(self.explode_thread, ())
        self.restart()

    def explode_thread(self):
        pass
        # time_delay = 300
        # pygame.time.wait(time_delay)
        # self.image = self.plane_down1_img
        # pygame.time.wait(time_delay)
        # self.image = self.plane_down2_img
        # pygame.time.wait(time_delay)
        # self.image = self.plane_down3_img
        # pygame.time.wait(time_delay)
        # self.image = self.plane_down4_img
        # pygame.time.wait(time_delay)
        # self.restart()
        # thread.exit_thread()

    def reset_bullet2_timer(self):
        if self.timer_b2:
            self.timer_b2.cancel()

    def bullet2_timer(self):
        self.timer_b2 = threading.Timer(constants.bullet2_last, self.lose_bullet2, ())
        self.timer_b2.start()

    def reset_bullet3_timer(self):
        if self.timer_b3:
            self.timer_b3.cancel()

    def bullet3_timer(self):
        self.timer_b3 = threading.Timer(constants.bullet3_last, self.lose_bullet3, ())
        self.timer_b3.start()

    def lose_bullet2(self):
        self.has_bullet2 = False

    def lose_bullet3(self):
        self.has_bullet3 = False

    def restart(self):
        self.stop = False
        self.image, self.rect = load_image(constants.myplane_pic, alpha=True)
        self.image = pygame.transform.scale \
            (self.image, (self.rect.width / 2, self.rect.height / 2))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = 222, 800
        self.isbooming = False
        self.bomb_store = 4
        self.stop = False
        self.speed = 2
        self.has_bullet2 = False
        self.has_bullet3 = False
        self.timer_b2 = None
        self.timer_b3 = None

    def update(self):
        if not self.stop:
            pos = pygame.mouse.get_pos()
            self.rect.center = pos

    def suspend(self):
        self.stop = True

    def recover(self):
        self.stop = False


class Enemy(pygame.sprite.Sprite):
    """Enemy planes"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 3
        self.image, self.rect = load_image(constants.enemy1_pic, alpha=True)
        screen = pygame.display.get_surface()
        self.mask = pygame.mask.from_surface(self.image)
        self.area = screen.get_rect()
        self.stop = False
        self.acceleration = 0.2
        self.rect.x = random.randint(20, 460)
        self.rect.y = random.randint(-200, -50)
        self.bullet_store = 0
        self.launch_bullet = False

    def restart(self):
        self.stop = False
        self.image, self.rect = load_image(constants.enemy1_pic, alpha=True)
        self.rect.x = random.randint(20, 460)
        self.rect.y = random.randint(-200, -50)

    def update(self):
        if self.rect.bottom <= 650:
            if not self.stop:
                self.rect.y = round(self.rect.y + random.random())
        else:
            self.kill()

    def accelerate(self):
        self.speed += self.acceleration

    def explode(self):
        self.stop = True
        thread.start_new_thread(self.explode_thread, ())

    def explode_thread(self):
        pygame.time.wait(40)
        self.image = self.__class__.enemy_down1_pic
        pygame.time.wait(40)
        self.image = self.__class__.enemy_down2_pic
        pygame.time.wait(40)
        self.image = self.__class__.enemy_down3_pic
        pygame.time.wait(40)
        self.image = self.__class__.enemy_down4_pic
        pygame.time.wait(40)
        self.restart()
        thread.exit_thread()

    def suspend(self):
        self.stop = True

    def recover(self):
        self.stop = False


# enemy plane with bullets
class Enemy2(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.image, self.rect = load_image(constants.enemy2_pic, alpha=True, scale=0.6)
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 2
        self.bullet_store = 1
        self.launch_bullet = False
        self.rect.x = random.randint(20, 460)
        self.rect.y = random.randint(-200, -50)

    def update(self):
        if self.rect.bottom <= self.area.height:
            if not self.stop:
                self.rect.y = round(self.rect.y + random.random())
                if self.rect.y > 50 and self.bullet_store == 2:
                    self.launch_bullet = True
                    self.bullet_store -= 1
                if self.rect.y > 150 and self.bullet_store == 1:
                    self.launch_bullet = True
                    self.bullet_store -= 1
        else:
            self.kill()

    def restart(self):
        self.stop = False
        self.launch_bullet = False
        self.image, self.rect = load_image(constants.enemy2_pic, alpha=True, scale=0.6)
        self.rect.x = random.randint(20, 460)
        self.rect.y = random.randint(-200, -50)


# enemy plane
class Enemy3(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.image, self.rect = load_image(constants.enemy3_pic, alpha=True, scale=0.6)
        self.speed = 1
        self.h_speed = 1
        self.player_pos = []
        self.mask = pygame.mask.from_surface(self.image)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.stop = False
        self.acceleration = 0.0025
        self.rect.x = random.randint(20, 460)
        self.rect.y = random.randint(-100, -50)
        self.launch_bullet = False
        self.bullet_store = 1

    def update(self):
        self.accelerate()
        if self.rect.bottom <= 650:
            if not self.stop:
                if self.bullet_store > 0 and self.rect.y > 0:
                    self.launch_bullet = True
                    self.bullet_store -= 1
                self.rect.y += self.speed
                if self.player_pos[1] - self.rect.y < constants.enemy3_chongci_dis:
                    self.rect.x += -self.h_speed if self.rect.x > self.player_pos[0] else self.h_speed
        else:
            self.kill()

    def get_player_pos(self, plane):
        self.player_pos = plane.rect.center

    def accelerate(self):
        if self.acceleration >= 0:
            self.acceleration -= 0.0001

    def restart(self):
        self.stop = False
        self.image, self.rect = load_image(constants.enemy3_pic, alpha=True, scale=0.6)
        self.rect.x = random.randint(20, 460)
        self.rect.y = random.randint(-200, -50)
# 定义敌机类

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.stop = False

    def update(self):
        pass

    def restart(self):
        pass

    def suspend(self):
        self.stop = True

    def recover(self):
        self.stop = False

    def explode(self):
        self.restart()


class Bullet1(Bullet):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(constants.bullet1_pic, alpha=True)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = pygame.mouse.get_pos()
        self.speed = 1
        self.stop = False

    def update(self):
        if not self.stop:
            self.rect.y -= self.speed
        if self.rect.y < 0:
            self.restart()

    def restart(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    def suspend(self):
        self.stop = True

    def recover(self):
        self.stop = False

    def explode(self):
        self.restart()

        # def kill(self):
        #     self.explode()


class Bullet2(Bullet):
    def __init__(self, pos):
        Bullet.__init__(self)
        self.image, self.rect = load_image(constants.bullet2_pic, alpha=True)
        self.rect.center = pos
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 2

    def explode(self):
        self.kill()

    def update(self):
        if not self.stop:
            self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()


class Bullet3(Bullet):
    def __init__(self, pos, direction):
        Bullet.__init__(self)
        self.image, self.rect = load_image(constants.bullet3_pic, alpha=True)
        self.rect.center = pos
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 1
        self.direction = direction

    def update(self):
        if not self.stop:
            self.rect.y -= self.speed
            self.rect.x += self.speed if self.direction else -(self.speed)
        if not self.area.contains(self.rect):
            self.kill()

    def explode(self):
        self.kill()


class EnemyBullet(Bullet):
    def __init__(self, pos):
        Bullet.__init__(self)
        self.image, self.rect = load_image(constants.bullet1_pic, alpha=True)
        self.stop = False
        self.rect.center = pos
        self.speed = 1
        self.area = pygame.display.get_surface().get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if not self.stop:
            self.rect.y += self.speed
        if self.rect.y > self.area.height:
            self.kill()


# 定义了子弹类
class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(constants.bomb_pic, alpha=True)
        self.boom_image, self.boom_rect = load_image(constants.boom_pic, -1)
        self.boom_image = pygame.transform.scale(self.boom_image,
                                                 (int(self.boom_rect.width / 2), int(self.boom_rect.height / 2)))
        self.boom_rect = self.boom_image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 0.3
        self.active = True
        self.rect.center = pygame.mouse.get_pos()
        self.expand_delay = 1
        self.stop = False

    def update(self):
        self.expand_delay += 1
        if self.expand_delay % 300 == 0 and not self.stop:
            self.expand()
        if not self.stop:
            self.rect.y = round(self.rect.y - random.random())
        if self.rect.bottom < 0:
            self.kill()

    def expand(self):
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * 1.2), int(self.rect.height * 1.2)))
        self.rect = self.image.get_rect(x=self.rect.x, y=self.rect.y)

    def explode(self, enemies):
        self.raw_rect = self.rect
        self.image, self.rect = self.boom_image, self.boom_rect

        self.rect.center = self.raw_rect.center
        self.stop = True
        enemies.suspend()
        pygame.sprite.spritecollide(self, enemies, dokill=True, collided=self.collide_detect)
        enemies.recover()
        timer = threading.Timer(0.8, self.finish, ())
        timer.start()

    @staticmethod
    def collide_detect(bomb, enemy):
        distance = ((enemy.rect.center[0] - bomb.rect.center[0]) ** 2
                    + (enemy.rect.center[1] - bomb.rect.center[1]) ** 2)
        if distance < (bomb.rect.width / 2) ** 2:
            return True
        return False

    def suspend(self):
        self.stop = True

    def recover(self):
        self.stop = False

    def finish(self):
        self.kill()

# 定义巨型炸弹

class UFO(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.v_speed = 1
        self.h_speed = 1
        self.randnum = random.randint(100, 200)
        self.delay = 0

    def update(self):
        pass

    def restart(self):
        pass

    def suspend(self):
        self.stop = True

    def recover(self):
        self.stop = False


class UFO1(UFO):
    def __init__(self):
        UFO.__init__(self)
        self.image, self.rect = load_image(constants.ufo1_pic, alpha=True)
        self.mask = pygame.mask.from_surface(self.image)
        self.restart()

    def update(self):
        if self.active:
            self.delay += 1
            if self.delay % 2 == 0:
                return
            self.rect.y += self.v_speed

            self.rect.x += self.h_speed if self.direction else -self.h_speed
            self.randnum -= 1
            if self.randnum == 0:
                self.randnum = random.randint(100, 200)
                self.direction = not self.direction
        if self.rect.y > self.area.height:
            self.restart()

    def restart(self):
        self.active = False
        self.rect.x = random.randint(self.area.width / 2 - 40, self.area.width / 2 + 40)
        self.rect.y = random.randint(-150, -120)
        self.direction = True if (self.rect.x < self.area.width / 2) else False


class UFO2(UFO):
    def __init__(self):
        UFO.__init__(self)
        self.image, self.rect = load_image(constants.ufo2_pic, alpha=True)
        self.mask = pygame.mask.from_surface(self.image)
        self.restart()

    def update(self):
        if self.active:
            self.delay += 1
            if self.delay % 2 == 0:
                return
            self.rect.y += self.v_speed

            self.rect.x += self.h_speed if self.direction else -self.h_speed
            self.randnum -= 1
            if self.randnum == 0:
                self.randnum = random.randint(100, 200)
                self.direction = not self.direction
        if self.rect.y > self.area.height:
            self.restart()

    def restart(self):
        self.active = False
        self.rect.x = random.randint(self.area.width / 2 - 40, self.area.width / 2 + 40)
        self.rect.y = random.randint(-150, -120)
        self.direction = True if (self.rect.x < self.area.width / 2) else False

class BombIcon(pygame.sprite.Sprite):
    def __init__(self, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(getcwd() + r"/ui/shoot/bomb_small.png")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = init_pos


# 定义炸弹图标，继承自精灵
class PlaneIcon(pygame.sprite.Sprite):
    def __init__(self, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(getcwd() + r"/ui/plane_small.png")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = init_pos


class MyGroup(pygame.sprite.RenderClear):
    def __init__(self, *sprites):
        pygame.sprite.RenderClear.__init__(self, *sprites)

    def suspend(self):
        for s in self.sprites():
            s.suspend()

    def recover(self):
        for s in self.sprites():
            s.recover()

# 定义飞机图标
