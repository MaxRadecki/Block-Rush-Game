#Importing Modules
from random import randint
from pygame.locals import *
import pygame
import sys
import os

# intalize Pygame
pygame.init()

# Set Up Screen
x_size = 1200
y_size = 750
screen = pygame.display.set_mode((x_size, y_size))

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
player_img = pygame.image.load(os.path.join(img_folder, 'happy_face.png')).convert()
food_img = pygame.image.load(os.path.join(img_folder, 'food.png')).convert()
BAD_food_img = pygame.image.load(os.path.join(img_folder, 'bad_food.png')).convert()

# Varible Used "while" Loop
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

WIDTH = 50
HEIGHT = 50


clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (x_size // 2, y_size // 2)
        self.rect.x = x_size / 2
        self.rect.y = y_size / 2
    def move_right(self):
        self.rect.x += 20
    def move_left(self):
        self.rect.x += -20
    def move_up(self):
        self.rect.y += -20
    def move_down(self):
        self.rect.y += 20
    
    def grow(self):
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(player_img, (int(width + 20),int(height + 20)))
        self.rect = self.rect.inflate(20,20)
    def anti_grow(self):
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(player_img, (int(width - 20), int(height - 20)))
        self.rect = self.rect.inflate(-20,-20)

class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = food_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.rect.x = randint(0,x_size*5)
        self.rect.y = randint(0,y_size*5)
    def move_right(self):
        self.rect.x += -20
    def move_left(self):
        self.rect.x += 20
    def move_up(self):
        self.rect.y += 20
    def move_down(self):
        self.rect.y += -20
    
class BAD_Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = BAD_food_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.rect.x = randint(0,x_size*5)
        self.rect.y = randint(0,y_size*5)
    def move_right(self):
        self.rect.x += -20
    def move_left(self):
        self.rect.x += 20
    def move_up(self):
        self.rect.y += 20
    def move_down(self):
        self.rect.y += -20


all_sprites = pygame.sprite.Group()
food_list = []
BAD_food_list = []

player = Player()
all_sprites.add(player)
all_food = []


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

x_cor_player = x_size*5
y_cor_player = y_size*5
# Most important code here
while not done:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
      
        if event.type == KEYDOWN:
            if event.key == K_w:
                for food in all_food:
                    food.move_up()
                y_cor_player += 20 
                if y_cor_player > y_size * 5:
                    player.move.down
                elif player.rect.centery < y_size // 2:
                    player.move_down()

            if event.key == K_s:
                for food in all_food:
                    food.move_down()
                y_cor_player += -20
                if y_cor_player < 0:
                    player.move_up()
                elif player.rect.centery > y_size // 2:
                    player.move_up


            if event.key == K_a:
                for food in all_food:
                    food.move_left()
                x_cor_player += -20
                if x_cor_player < 0:
                    player.move_right()
                elif player.rect.centerx < x_size // 2:
                    player.move_right()

            if event.key == K_d:
                for food in all_food:
                    food.move_right()
                x_cor_player += 20
                if x_cor_player > x_size * 5:
                    player.move_left()
                elif player.rect.centerx > x_size // 2:
                    player.move_left()



        
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
    print(y_cor_player)
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()