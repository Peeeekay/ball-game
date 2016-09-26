import pygame, sys, random, math
from pygame.locals import *
from math import *
pygame.init()

WINDOW_X = 800
WINDOW_Y = 600
screen = pygame.display.set_mode((WINDOW_X,WINDOW_Y))     #set up PyGame Window
black = 0,0,0
count=0

#X,Y Coordinates for where to draw the cannon
CANNON_X = 30
CANNON_Y = 425
#counter fro shots
sn=20
#number of cannon shots
NUMBER_SHOTS= []
for i in range(1,21):
    NUMBER_SHOTS.append(pygame.image.load("images/shots"+str(i)+".png"))
xa=0
POWER=[]
GRAVITY = 0.8
#target hits
score=0
#Load Cannon Ball image
cannonball=pygame.image.load("images/Cannonball.png")
#Load the background image
background = pygame.image.load("images/Background.png")
background_pos = background.get_rect()
grade=""
#Load a list of sprite images for the Cannon
cannon = []
e= []
for x in range(7):
    cannon.append(pygame.image.load("images/Cannon-"+str(x*15)+".png"))
for i in range(1,7):
    e.append(pygame.image.load("images/ex"+str(i)+".png"))
#uploading target image
TARGET= pygame.image.load("images/target.png")
#Target co-ordinates
TARGET_Y= random.randint(110,500)
TARGET_X= random.randint(120,750)
TARGET_POS= (TARGET_X,TARGET_Y)


#image of target
# loading a list of power images
for i in range(1,11):
    POWER.append(pygame.image.load("images/power"+str(i)+".png"))
#new list and function adding explostion
e=[]
T_Images=[]

for i in range(1,21):
    T_Images.append(pygame.image.load("images/target"+str(i)+".png"))

#We will limit possible shooting angles. A list will correspond with sprite images from cannon[]
angles = [0,15,30,45,60,75,90]
power=[7, 8, 9, 10, 12, 13, 14, 15, 16, 18]
power_image = 3
cannon_image = 2
shots_image=20
running = True




#Cannonball class
class Ball(object):
    def __init__(self,image,dir_x,dir_y,emit_x,emit_y,CANNON_POWER,TARGET_Y,TARGET_X):
        self.x= dir_x * CANNON_POWER
        self.y= dir_y *CANNON_POWER
        self.image=image
        self.pos=image.get_rect().move(emit_x,emit_y)
        self.alive=True
        self.will_collide=0 #flag for if cannon ball will hit ground
        self.hit_target=0   #flag for if cannon ball will hit target
        self.TARGET_Y=TARGET_Y
        self.TARGET_X=TARGET_X
        self.countdown=random.randint(1,5)
        self.lifetime=random.randint(4,30)
        self.steps=0
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
            #if target was hit
            if (self.TARGET_Y)<=(self.pos.bottom)<=(self.TARGET_Y+40) or (self.TARGET_Y)<=(self.pos.top)<=(self.TARGET_Y+40):
                if (self.TARGET_X)<=(self.pos.right)<= (self.TARGET_X+40) or (self.TARGET_X)<=( self.pos.left)<=(self.TARGET_X+40):
                    self.hit_target=1
    def move_smoke(self):
        self.steps +=1
        if self.steps==self.lifetime:
            self.alive=False
        self.pos=self.pos.move(self.x,-self.y)



ex=[]
smoke_Particles=[]
my_font = pygame.font.SysFont("monospace",25)
my_font2= pygame.font.SysFont("monospace",18)
#smoke
smoke=[]
for i in range(1,5):
    smoke.append(pygame.image.load("images/smoke"+str(i)+".png"))
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
                    c=Ball(cannonball,x,y*-1,EMIT_X,EMIT_Y,power[power_image],TARGET_Y,TARGET_X)
                    shots.append(c) #fire cannon balls
                    sn -= 1 #remaining shots left

    screen.blit(background, background_pos)  # Clear the screen by filling with out background image)


    screen.blit(NUMBER_SHOTS[sn-1],(250,30))#shots image on the screen.


    if sn == 0:
        screen.blit(background, background_pos)  # Clear the screen by filling with out background image)


    screen.blit(TARGET,(TARGET_X,TARGET_Y)) #TARGET AT RANDOM POSITIONS ON SCREEN



    for s in shots:
        screen.blit(s.image, s.pos)
        if s.hit_target==1:
            T= TARGET_POS
            for i in e:
                ex.append(i)
            TARGET_Y= random.randint(110,500)
            TARGET_X= random.randint(120,750)
            TARGET_POS= (TARGET_X,TARGET_Y)
            score +=1
            count=0

        if s.will_collide==1:
            xt=s.pos.x

            if xt <750:
                for t in range(0,100):
                    sp=Ball(smoke[random.randint(0,3)],random.uniform(-1,1),random.uniform(1,5),random.uniform(xt-2,xt+2),551,1,TARGET_Y,TARGET_X)
                    smoke_Particles.append(sp)
        s.move()
        if s.alive==False:
            shots.remove(s)

    if score > 0 and sn > 0:
        screen.blit(T_Images[score-1], ( 500,30))

    if sn==0 and(c.will_collide==1 or c.hit_target==1): #All the available shots fired.
        screen.blit(background, background_pos)  # Clear the screen by filling with out background image)
        if score >= 18:
            grade="A+"
        elif 18> score >= 16:
            grade="A"
        elif 16> score>= 14:
            grade="B+"
        elif 14> score>=12:
            grade="B"
        elif 12> score >=8:
            grade="C"
        elif 8>score>5:
            grade="D"
        else:
            grade="F"

        report = my_font.render("In 20 shots, you have hit " + str(score) +" targets.",False,(0,0,0))
        report2 = my_font.render("Accuracy: "+ str(score*100/20)+". Your grade is " + grade,False,(0,0,0))
        report3= my_font2.render("Press Enter to play NEW GAME",False,(0,0,0))
        screen.blit(report,(200,250))
        screen.blit(report2,(200,280))
        screen.blit(report3,(250,310))


    if event.type==pygame.KEYDOWN: #if a player want to start a new game.
        if event.key==pygame.K_RETURN:
            if sn==0:

                score=0
                screen.blit(background,background_pos)
                power_image = 3
                cannon_image = 2
                sn=20


#smoke, when it hits the ground
    if len(smoke_Particles)>0:
        for sp in smoke_Particles:
            sp.move_smoke()

            if sp.countdown==0:
                if sp.steps <= 4:
                    draw= pygame.transform.scale(sp.image,(30,30))
                elif sp.steps <=11:
                    draw=pygame.transform.scale(sp.image,(random.randint(16,24),random.randint(16,24)))

                else:
                     draw=pygame.transform.scale(sp.image,(random.randint(3,14),random.randint(3,14)))

                screen.blit(draw,sp.pos)

                if sp.alive==False:
                    smoke_Particles.remove(sp)




            else:
                sp.countdown -=1
#explosion, when it hits the target
    if len(ex)>0:
        if count <6:
            screen.blit(ex[count],T)
            count=count+1


    cannon_location = cannon[cannon_image].get_rect().move(CANNON_X,CANNON_Y)
    screen.blit(cannon[cannon_image], cannon_location)
    screen.blit(POWER[power_image],(0,0)) #blitting power on the screen

    #Update the display and delay for animation
    pygame.display.update()
    pygame.time.delay(10)





pygame.quit()










