#Importing Modules
from random import randint
from pygame.locals import *
import pygame
import sys
import os
from time import sleep
import math

# Intalize Pygame
pygame.init()

# Set Up Screen
x_size = 1200
y_size = 750
screen = pygame.display.set_mode((x_size, y_size))

# Intalizing Sprites
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
player_img = pygame.image.load(os.path.join(img_folder, 'happy_face.png')).convert()
food_img = pygame.image.load(os.path.join(img_folder, 'food.png')).convert()
BAD_food_img = pygame.image.load(os.path.join(img_folder, 'bad_food.png')).convert()
fire_ball_img = pygame.image.load(os.path.join(img_folder, 'fire_ball.png')).convert()
enemy_img = pygame.image.load(os.path.join(img_folder, 'enemy.png')).convert()
lightning_bolt_img = pygame.image.load(os.path.join(img_folder, 'lightning_bolt.png')).convert()

# Varible Used in "while" Loop
done = False


# Setting Caption of Pygame Tab
pygame.display.set_caption("Block Rush Game")

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
Lime = (0,255,0)
Yellow = (255,255,0)
Aqua = (0,255,255)
Magenta = (255,0,255)
Silver = (192,192,192)
Gray = (128,128,128)
Maroon = (128,0,0)
Olive = (128,128,0)
Purple = (128,0,128)
Teal = 	(0,128,128)
Navy = (0,0,128)

# Simple Height and Width Used in the Sprite's Classes
WIDTH = 50
HEIGHT = 50

# Intalizing Clock Varible
clock = pygame.time.Clock()

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (x_size // 2, y_size // 2)
        self.rect.x = x_size / 2
        self.rect.y = y_size / 2
# Moving Functions of Player
    def move_right(self):
        self.rect.x += 20
    def move_left(self):
        self.rect.x += -20
    def move_up(self):
        self.rect.y += -20
    def move_down(self):
        self.rect.y += 20

# The Growth or Anti-growth of the Player
    def grow(self):
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(player_img, (int(width + 20),int(height + 20)))
        self.rect = self.rect.inflate(20,20)
    def anti_grow(self):
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(player_img, (int(width - 20), int(height - 20)))
        # if self.image.get_size()[0] < 20 or self.image.get_size()[1] < 20:
        #     done = True
        # else: 
        self.rect = self.rect.inflate(-20,-20)
    def super_anti_grow(self):
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(player_img, (int(width - 40),int(height - 40)))
        self.rect = self.rect.inflate(-40,-40)
    def super_grow(self):
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(player_img, (int(width + 40),int(height + 40)))
        self.rect = self.rect.inflate(40,40)

# The Food Class
class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = food_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.rect.x = randint(0,x_size*5)
        self.rect.y = randint(0,y_size*5)
# Move Functions of Food Class
    def move_right(self):
        self.rect.x += -20
    def move_left(self):
        self.rect.x += 20
    def move_up(self):
        self.rect.y += 20
    def move_down(self):
        self.rect.y += -20

# BAD_food Class
class BAD_Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = BAD_food_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.rect.x = randint(-x_size*2.5,x_size*2.5)
        self.rect.y = randint(0,y_size*5)
# Move Functions of BAD_food Class
    def move_right(self):
        self.rect.x += -20
    def move_left(self):
        self.rect.x += 20
    def move_up(self):
        self.rect.y += 20
    def move_down(self):
        self.rect.y += -20

# The Fireball Class
class FireBall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = fire_ball_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.rect.x = x_size/2
        self.rect.y = y_size/2
        self.cooldown = 4000
        self.last = pygame.time.get_ticks()
# Shoot Functions of Fireball
    def shoot_right(self):
        self.rect.x += 20
    def shoot_left(self):
        self.rect.x += -20
    def shoot_up(self):
        self.rect.y += 20
    def shoot_down(self):
        self.rect.y += -20

# The Enemy Class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.rect.x = randint(-x_size*2.5,x_size*2.5)
        self.rect.y = randint(0,y_size*5)
# Move Functions of Enemy
    def move_right(self):
        self.rect.x += -20
    def move_left(self):
        self.rect.x += 20
    def move_up(self):
        self.rect.y += 20
    def move_down(self):
        self.rect.y += -20

# Setting of the all_sprites varible
all_sprites = pygame.sprite.Group()

# The Lists for Multiple Use of Classes in Game
food_list = []
BAD_food_list = []
enemy_list = []
all_food = []

# Setting up the Player in a Varible Form
player = Player()
all_sprites.add(player)

# Creating Multiple Items
for i in range(100):
    food = Food()
    all_sprites.add(food)
    food_list.append(food)
    all_food.append(food)
for i in range(100):
    BAD_food = BAD_Food()
    all_sprites.add(BAD_food)
    BAD_food_list.append(BAD_food)
    all_food.append(BAD_food)
for i in range(100):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemy_list.append(enemy)
    all_food.append(enemy)

# Coordinates of the Player
x_cor_player = x_size*5/2
y_cor_player = y_size*5/2

# Intalizing Fireball as a Variable
fireball = None

# Game While Loop
while not done:
    # Game Speed
    clock.tick(120)
    # Event Part of While Loop
    for event in pygame.event.get():
        # Exit Out Part of While Loop
        if event.type == pygame.QUIT:
            sys.exit()
        
        # Key Pressing Part
        if event.type == KEYDOWN:
            # W Key
            if event.key == K_w:
                fireball_con = 1
                for food in all_food:
                    food.move_up()
                y_cor_player += 20 
                if y_cor_player > y_size * 5:
                    player.move.down
                elif player.rect.centery < y_size // 2:
                    player.move_down()
            # S Key
            if event.key == K_s:
                fireball_con = 2
                for food in all_food:
                    food.move_down()
                y_cor_player += -20
                if y_cor_player < 0:
                    player.move_up()
                elif player.rect.centery > y_size // 2:
                    player.move_up

            # A Key
            if event.key == K_a:
                fireball_con = 3
                for food in all_food:
                    food.move_left()
                x_cor_player += -20
                if x_cor_player < 0:
                    player.move_right()
                elif player.rect.centerx < x_size // 2:
                    player.move_right()

            # D Key
            if event.key == K_d:
                fireball_con = 4
                for food in all_food:
                    food.move_right()
                x_cor_player += 20
                if x_cor_player > x_size * 5:
                    player.move_left()
                elif player.rect.centerx > x_size // 2:
                    player.move_left()
            
            # F Key
            if event.key == K_f:
                if fireball is None or pygame.time.get_ticks() - fireball.last >= fireball.cooldown:
                    fireball = FireBall()
                    all_sprites.add(fireball)
                
                

    # Colliding Loops   
    for food in food_list:
        if player.rect.colliderect(food):
            food.kill()
            food_list.remove(food)
            all_food.remove(food)
            player.grow()
    for foodz in BAD_food_list:
        if player.rect.colliderect(foodz):
            foodz.kill()
            BAD_food_list.remove(foodz)
            all_food.remove(foodz)
            player.anti_grow()
    for enemy in enemy_list:
        if player.rect.colliderect(enemy):
            enemy.kill()
            enemy_list.remove(enemy)
            all_food.remove(enemy)
            player.super_anti_grow()
        elif fireball != None:
            if fireball.rect.colliderect(enemy):
                enemy.kill()
                enemy_list.remove(enemy)
                all_food.remove(enemy)
                player.super_grow()
    
    # Shooting Part With Fireball
    if fireball is not None:
        fireball.shoot_right()
        if fireball.rect.x == 1080:
            fireball.kill()
            fireball = None
        elif pygame.time.get_ticks() - fireball.last >= fireball.cooldown:     
            fireball.kill()
            fireball = None

    # if player.image.get_size() == (1,1):
    #     done = True

    # Screen Fill Black
    screen.fill(BLACK)

    # Draw All the Sprites on the Screen
    all_sprites.draw(screen)

    # Update the Screeen
    pygame.display.update()

# End of Everything
pygame.quit()
