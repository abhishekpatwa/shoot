# 1 - Import library
import pygame, math, random
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
pygame.mixer.init()
width, height = 640, 480
keys = [False, False, False, False]
playerpos = [180, 100]
screen=pygame.display.set_mode((width, height))
##acc=[0,0]
arrows = []
badtimer = 100
badtimer1 = 0
badguys = [[640, 100]]
healthvalue = 194
# 3 - Load images
player = pygame.image.load("resources/images/shooter.png")
grass = pygame.image.load("resources/images/sky.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/sk.png")
badguyimg1 = pygame.image.load("resources/images/badguy.png")
badguyimg = badguyimg1
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
gameover = pygame.image.load("resources/images/gameover.png")
youwin = pygame.image.load("resources/images/youwin.png")
# 3.1 - Load audio
hit = pygame.mixer.Sound("resources/audio/explode.wav")
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
pygame.mixer.music.load('resources/audio/moonlight.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)
