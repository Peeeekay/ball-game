#-------------------------------------------------------------------------------
#
# Ballistics. Create Cannonball particles that reasonably observe the laws of Physics!
#-------------------------------------------------------------------------------
import pygame, sys, random, math
from pygame.locals import *
from math import *
pygame.init()

WINDOW_X = 800
WINDOW_Y = 600
screen = pygame.display.set_mode((WINDOW_X,WINDOW_Y))     #set up PyGame Window
black = 0,0,0

#X,Y Coordinates for where to draw the cannon
CANNON_X = 30
CANNON_Y = 425
#counter fro shots
sn=20
#number of cannon shots
NUMBER_SHOTS= []
for i in range(1,21):
    NUMBER_SHOTS.append(pygame.image.load("shots"+str(i)+".png"))

POWER=[]
GRAVITY = 0.8
#target hits
score=0
#Load Cannon Ball image
cannonball=pygame.image.load("Cannonball.png")
#Load the background image
background = pygame.image.load("Background.png")
background_pos = background.get_rect()

#Load a list of sprite images for the Cannon
cannon = []
for x in range(7):
    cannon.append(pygame.image.load("Cannon-"+str(x*15)+".png"))
# loading a list of power images
for i in range(1,11):
    POWER.append(pygame.image.load("power"+str(i)+".png"))
#new list and function adding explostion
e=[]
for i in range(1,7):
    e.append(pygame.image.load("ex"+str(i)+".png"))
#uploading target image
TARGET= pygame.image.load("target.png")
#Target co-ordinates
TARGET_Y= random.randint(110,530)
TARGET_X= random.randint(95,750)
TARGET_POS= (TARGET_X,TARGET_Y)
TARGET_HEIGHT= TARGET.get_height()
TARGET_WIDTH= TARGET.get_width()
print TARGET.get_size()
#image of target
T_Images=[]

for i in range(1,21):
    T_Images.append(pygame.image.load("target"+str(i)+".png"))

#We will limit possible shooting angles. A list will correspond with sprite images from cannon[]
angles = [0,15,30,45,60,75,90]
power=[7, 8, 9, 10, 12, 13, 14, 15, 16, 18]
power_image = 3
cannon_image = 2
shots_image=20
running = True
#Cannonball class
class Ball(object):
    def __init__(self,image,dir_x,dir_y,emit_x,emit_y,CANNON_POWER):
        self.x= dir_x * CANNON_POWER
        self.y= dir_y *CANNON_POWER
        self.image=image
        self.pos=image.get_rect().move(emit_x,emit_y)
        self.alive=True
        self.will_collide=0 #flag for if cannon ball will hit ground
        self.hit_target=0   #flag for if cannon ball will hit target

    def move(self):
        if self.will_collide==1:
            self.pos.bottom= 558
            self.pos.x += self.x
            self.alive= False
        if self.hit_target==1:
            self.alive= False

        else:
            self.y += 0.8
            self.pos=self.pos.move(self.x,self.y)
            if (self.pos.bottom + self.y) > 557:
                self.will_collide=1
    def explode(self):
        if self.will_collide==1:
            return "Boom"

my_font = pygame.font.SysFont("monospace",25)

#smoke
smoke=[]
for i in range(1,5):
    smoke.append(pygame.image.load("smoke"+str(i)+".png"))

shots=[]
while running:
    pygame.mouse.set_visible(1)

    # -- Check for User closing the window, and QUIT in that event ---#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Check for keyboard input, and change trajectory and power input based on arrow key presses. Space for shoot
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if cannon_image < 6: cannon_image += 1
            if event.key == pygame.K_RIGHT:
                if cannon_image > 0: cannon_image -= 1
            if event.key== pygame.K_UP:
                if power_image < 9: power_image +=1
            if event.key== pygame.K_DOWN:
                if power_image > 0 : power_image -=1
            if sn >0:
                if event.key == pygame.K_SPACE:
                    y= (2*sin(math.radians(angles[cannon_image])))
                    x= sqrt(4-(y*y))
                    EMIT_X= random.randint(90,92)
                    EMIT_Y=random.randint(503,507)
                    c=Ball(cannonball,x,y*-1,EMIT_X,EMIT_Y,power[power_image])
                    shots.append(c) #fire cannon balls
                    sn -= 1




    screen.blit(background, background_pos)  # Clear the screen by filling with out background image)


    screen.blit(NUMBER_SHOTS[sn-1],(250,30))
    screen.blit(TARGET,(TARGET_X,TARGET_Y)) #TARGET AT RANDOM POSITIONS ON SCREEN

    if sn == 0:
        screen.blit(background, background_pos)  # Clear the screen by filling with out background image)






    for s in shots:
        screen.blit(s.image, s.pos)


        #if target was hit

        if  TARGET_Y<=(s.y+s.pos.bottom)<=(TARGET_Y+40) or (TARGET_Y)<=(s.y+c.pos.top)<=(TARGET_Y+40):
            if (TARGET_X)<=(s.x + s.pos.right)<= (TARGET_X+40) or (TARGET_X)<=(s.x + s.pos.left)<=(TARGET_X+40):
                s.hit_target=1
                score += 1

                for j in range(6):
                    screen.blit(e[j],TARGET_POS)


                TARGET_Y= random.randint(110,500)
                TARGET_X= random.randint(100,750)
                TARGET_POS=(TARGET_X,TARGET_Y)


        s.move()

        if s.alive==False:
            screen.blit(smoke[3],s.pos)
            shots.remove(s)

    if score > 0 and sn > 0:
        screen.blit(T_Images[score-1], ( 500,40))


    if sn==0:

        report = my_font.render(str(score),False,(0,0,0))
        screen.blit(report,(300,250))


    cannon_location = cannon[cannon_image].get_rect().move(CANNON_X,CANNON_Y)
    screen.blit(cannon[cannon_image], cannon_location)
    screen.blit(POWER[power_image],(0,0)) #blitting power on the screen

    #Update the display and delay for animation
    pygame.display.update()
    pygame.time.delay(10)
    #when 20 shots has been fired




pygame.quit()


















































































