# coding=utf-8
import pygame
import random
from os import getcwd
from common import *

pygame.mixer.init()

# def explosion_contain(enemy, bomb):
#     if (bomb.x - 50 < enemy.x) and (enemy.x + enemy.image.get_width() < bomb.x + bomb.image.get_width() + 50) and (
#                 enemy.y > bomb.y - 50) and (enemy.y + enemy.image.get_height() < bomb.y + bomb.image.get_height() + 50):
#         enemy.restart()
#
#
# # 检测在巨型炸弹爆炸范围内有无敌机
class Plane(pygame.sprite.Sprite):
    # 出现在屏幕下方中央的位置
    # noinspection PyCallByClass
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("my_plane.png", alpha=True)
        self.mask = pygame.mask.from_surface(self.image)
        self.bomb_store = 4
        self.stop = False
        self.life = 3
        self.restart()

    def restart(self):
        self.rect.topleft = 256, 900

    def update(self):
        if not self.stop:
            pos = pygame.mouse.get_pos()
            self.rect.center = pos

    def suspend(self):
        self.stop = True

    def recover(self):
        self.stop = False
        # def checkCrash(self, enemy):
        #     if (self.rect.x + 0.7 * self.rect.width > enemy.rect.x) and \
        #             (self.rect.x + 0.3 * self.rect.width < enemy.rect.x + enemy.rect.width) and \
        #             (self.rect.y + 0.7 * self.rect.height > enemy.rect.y) and \
        #             (self.rect.y + 0.3 * self.rect.height < enemy.rect.y + enemy.rect.height):
        #         return True
        #     return False


# 定义我机
class Enemy(pygame.sprite.Sprite):
    """Enemy planes"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 1
        self.image, self.rect = load_image("enemy1.png", alpha=True)
        screen = pygame.display.get_surface()
        self.mask = pygame.mask.from_surface(self.image)
        self.area = screen.get_rect()
        self.stop = False
        self.acceleration = 0.2
        self.rect.x = random.randint(20, 440)
        self.rect.y = random.randint(-200, -50)

    def update(self):
        if self.rect.bottom <= 650 and not self.stop:
            self.rect.y = round(self.rect.y + random.random())
        else:
            self.kill()

    def accelerate(self):
        self.speed += self.acceleration

    def explode(self):
        pass

    def suspend(self):
        self.stop = True

    def recover(self):
        self.stop = False


# 定义敌机类
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("shoot/bullet1.png", alpha=True)
        self.rect.center = pygame.mouse.get_pos()
        self.speed = 5
        self.stop = False

    def update(self):
        if not self.stop:
            self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

    def restart(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    def suspend(self):
        self.stop = True

    def recover(self):
        self.stop = False


# 定义了子弹类
class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("shoot/bomb.png", alpha=True)
        self.speed = 0.3
        self.active = True
        self.rect.center = pygame.mouse.get_pos()
        self.sound = load_sound("use_bomb.mp3")
        self.stop = False

    def update(self):
        if not self.stop:
            self.rect.y = round(self.rect.y - random.random())
        if self.rect.bottom < 0:
            self.kill()

    def explode(self):
        self.sound.play()

    def suspend(self):
        self.stop = True

    def recover(self):
        self.stop = False


# 定义巨型炸弹


class BombIcon(pygame.sprite.Sprite):
    def __init__(self, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(getcwd() + r"/ui/shoot/bomb_small.png")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = init_pos


# 定义炸弹图标，继承自精灵
class Plane_icon(pygame.sprite.Sprite):
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
            print type(s)
            s.suspend()

    def recover(self):
        for s in self.sprites():
            s.recover()

# 定义飞机图标
