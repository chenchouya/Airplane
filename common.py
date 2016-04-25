import os
import pygame
from pygame.locals import *


def load_image(name, colorkey=None, alpha=False, scale=None):
    fullname = os.path.join('ui', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    if alpha:
        image = image.convert_alpha()
    else:
        image = image.convert()
    if scale is not None:
        rect = image.get_rect()
        image = pygame.transform.scale(image, (int(rect.width * scale), int(rect.height * scale)))
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def load_sound(name):
    class NoneSound:
        def __init__(self):
            pass

        def play(self): pass

    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('sound', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', name
        raise SystemExit, message
    return sound


def load_font(name, size=35):
    fullname = os.path.join("font", name)
    try:
        font = pygame.font.Font(fullname, size)
    except pygame.error, message:
        print 'Cannot load font:', name
        raise SystemError, message
    return font

