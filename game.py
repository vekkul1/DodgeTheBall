print("""
== Ball Dodging Game =='
AUTHOR:
Veeti Halla-aho
last update 
(dd/mm/yyyy)
28/11/2020 02:48
version 1.1
""")
import pygame
import math
import random
import time

"""
Variables
"""

pygame.init()
#setting frame rate 120 suggested
framerate = 120
#initiating screen
displayWidth = 900
displayHeight = 700
displayBG = (35, 0, 35)
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("Dodge")
#initiates fonts
myfont = pygame.font.SysFont("Arial", 32)
highscorefont = pygame.font.SysFont("Arial", 64)
#highscore system
newHighScore = False
#gets highscore
f = open("scores.txt", "r")
highscore = f.read()
f.close()

"""
Classes
"""

#creating a ball class
class Ball:
    def __init__(self, posx, posy, colour = (255,255,255)):
        #balls position
        self.position = [posx, posy]
        #balls speed & speed magnitude
        self.speedMagnitude = 0.5
        self.speed = [0,0]
        #ball colour
        self.colour = colour
        #ball radius
        self.r = 10
        #direction
        self.dirx, self.diry = random.randint(-3,3), random.randint(-3,3)
        if self.dirx == 0:
            self.dirx += random.randint(1,3)
        if self.diry == 0:
            self.diry += random.randint(1,3)
        #initiates a unitvector
        #using pythagoras theorum 
        self.lenght = math.sqrt(self.dirx*self.dirx + self.diry*self.diry)
        self.unitVector = [self.dirx / self.lenght, self.diry /self.lenght]
        
        
    def calculateSpeed(self):
        #calculates speed
        self.speed[0] = self.unitVector[0]*self.speedMagnitude
        self.speed[1] = self.unitVector[1]*self.speedMagnitude
        
        
    def display(self):
        #draws the ball
        pygame.draw.circle(gameDisplay, self.colour, (int(self.position[0]), int(self.position[1])), self.r)

    def moveBall(self):
        #moves the ball
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]

#makes a player class        
class Player:
    def __init__(self, posx, posy):
        #player position
        self.posx, self.posy = posx, posy
        #player speed
        self.speed = 0.4
        #player width & height
        self.width = 40
        self.height = 15
        
    def display(self):
        #draws player
        pygame.draw.rect(gameDisplay, (255,255,255),[self.posx,self.posy,self.width,self.height])
        
    def hitUp(self,ball):
        #checks players collision on the upper edge
        upEdge = [self.posx + self.width /2, self.posy]
        distance = math.hypot(upEdge[0] - ball.position[0], upEdge[1] - ball.position[1])
        
        if distance < (ball.r +2):
            return True
        else:
            return False
            
    def hitDown(self, ball):
        #checks players collision on the down edge
        downEdge =[self.posx + self.width /2, self.posy + self.height]
        distance = math.hypot(downEdge[0] - ball.position[0], downEdge[1] - ball.position[1])
        
        if distance < (ball.r +2):
            return True
        else:
            return False
            
    def hitLeft(self, ball):
        #checks players collision on the left edge
        leftEdge = [self.posx, self.posy + self.height/2]
        distance = math.hypot(leftEdge[0] - ball.position[0], leftEdge[1] - ball.position[1])
        
        if distance < (ball.r +2):
            return True
        else:
            return False
            
    def hitRight(self, ball):
        #checks players collision on the right edge
        rightEdge = [self.posx + self.width, self.posy + self.width/2]
        distance = math.hypot(rightEdge[0] - ball.position[0], rightEdge[1] - ball.position[1])
        
        if distance < (ball.r +2):
            return True
        else:
            return False
            
    
"""
Functions
"""

def checkCollision(ppos, bpos, distance):
	#checks collisions
    if(abs(ppos - bpos) < distance):
        return True
    else:
        return False
        
def checkBallBorderCollision(ballsaulukko):
    #Checks balls for border collision
    for p in ballsaulukko:
        if checkCollision(p.position[0], 0, 10):
            p.unitVector[0] *= -1
        if checkCollision(p.position[0],displayWidth,10):
            p.unitVector[0] *= -1
        if checkCollision(p.position[1],0,10):
            p.unitVector[1] *= -1
        if checkCollision(p.position[1],displayHeight,10):
            p.unitVector[1] *= -1

def checkBallCollision(ball1,ball2):
    bdistance = math.hypot(ball1.position[0]-ball2.position[0], ball1.position[1]-ball2.position[1])
    #unitvectors
    unit1x = ball1.unitVector[0]
    unit1y = ball1.unitVector[1]
    unit2x = ball2.unitVector[0]
    unit2y = ball1.unitVector[1]
    #törmäys etäisyys
    collisionDistance = ball1.r + ball2.r
    if(bdistance <= collisionDistance):
        ball1.unitVector[0] = unit2x
        ball1.unitVector[1] = unit2y
        ball2.unitVector[0] = unit1x
        ball2.unitVector[1] = unit1y

def getStartTime():
    start = time.time()
    return start

def calculateTime(startTime):
    #calculates time from start
    currentTime = time.time()
    timeElapsed = currentTime - startTime
    return round(timeElapsed,1)
    
def checkHighScore(newT):
    if newT > float(highscore):
        f = open("scores.txt", "w")
        f.write(str(newT))
        f.close()
    
    
"""
Loop
"""

#game loop
def main():
    gameGo = True
    #gets starting time
    sTime = getStartTime()
    #initiates player
    player = Player(displayWidth/2 - 20, 600)
    #gets highscore
    f = open("scores.txt", "r")
    highscore = f.read()
    f.close()

    #initiates balls
    ball1 = Ball(100, 100)
    ball2 = Ball(300, 100)
    ball3 = Ball(500, 100)
    ball4 = Ball(700, 100)
    ball5 = Ball(100, displayHeight/2)
    ball6 = Ball(200, 200)
    ball7 = Ball(200, 400)
    ball8 = Ball(200, 600)
    ball9 = Ball(200, 800)
    ball10 = Ball(400, 400)
    ball11 = Ball(300, 600)
    ball12 = Ball(200, 200)

    #ball list
    balls = [ball1, ball2, ball3, ball4, ball5, ball6, ball7, ball8, ball9]
    while gameGo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        clock = pygame.time.Clock()
        dt = clock.tick(framerate)
        
        #binds keys to player movement
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_LEFT]):
            player.posx -= player.speed * dt
        if(keys[pygame.K_RIGHT]):
            player.posx += player.speed * dt
        
        #checks player collision to walls
        if checkCollision(player.posx, 0, 1):
            player.posx += player.speed * dt
            
            
        if checkCollision(player.posx, displayWidth, player.width):
            player.posx -= player.speed * dt
            
        
        #clears canvas
        gameDisplay.fill(displayBG)
        #draws player
        player.display()
        
        
        #loop for balls
        for p in balls:
            #draws balls
            p.display()
            #checks ball and player collisions
            if player.hitUp(p):
                p.unitVector[1] *= -1
                p.position[1] -= 3
                checkHighScore(timer)
                gameGo = False
                
            elif player.hitDown(p):
                p.unitVector[1] *= -1
                p.position[1] -= 3
                checkHighScore(timer)
                gameGo = False
                
            elif player.hitLeft(p):
                p.unitVector[0] *= -1
                p.position[0] += 3
                checkHighScore(timer)
                gameGo = False
                
            elif player.hitRight(p):
                p.unitVector[0] *= -1
                p.position[0] += 3
                checkHighScore(timer)
                gameGo = False
                
            #calculates player speed
            p.calculateSpeed()
            #moves player
            p.position[0] += p.speed[0] * dt
            p.position[1] += p.speed[1] * dt
        
        #cheks balls collisions to walls
        checkBallBorderCollision(balls)
        
        #checks balls collions to balls
        x=1
        for boll in balls:
            partOfBalls = balls[x:]
            for secondBall in partOfBalls:
                checkBallCollision(boll, secondBall)
            x+=1
            if(x == len(balls)):
                break
        
        #timer
        timer = calculateTime(sTime)
        timeText = myfont.render("time:{0}".format(timer),1 ,(255,255,255))
        highscoreText = myfont.render("highscore:{0}".format(highscore), 1, (255, 255 ,255))
        gameDisplay.blit(timeText, (0,0))
        gameDisplay.blit(highscoreText, (0,32))
        
        #difficulty
        if timer == 15.0:
            #doubles balls speed
            for p in balls:
                p.speedMagnitude = 1
        if timer == 30.0:
            #halves players speed
            player.speed = 0.2
        if timer == 45.0:
            #doubles balls speed again
            for p in balls:
                p.speedMagnitude = 2
        
        #updates display
        pygame.display.update()

    #starts end screen timer    
    goStart = time.time()    

    #endscreen loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE]):
            gameGo = True
            main()
            

        elif (keys[pygame.K_ESCAPE]):
            pygame.quit()
            quit()
        
        #clears canvas
        gameDisplay.fill(displayBG)
        
        #initiates text
        topText = myfont.render("!!!GAME OVER!!!", 1, (255,255,0)) 
        lastTimeText = myfont.render("you lasted {0} seconds".format(timer), 1, (255,255,255))
        restartText = myfont.render("press space to restart",1, (255,255,255))
        escText = myfont.render("press escape to quit", 1, (255,255,255))
        bottomText = myfont.render("!!!GAME OVER!!!", 1, (255,255,0))
        
        #puts text on canvas
        gameDisplay.blit(topText, (350, 300))
        gameDisplay.blit(lastTimeText, (330, (displayHeight/2-16)))
        gameDisplay.blit(bottomText, (350, 370))
        gameDisplay.blit(restartText, (330, 400))
        gameDisplay.blit(escText, (330, 440))
        
        #timer
        goTimer = calculateTime(goStart)
        goTimer = round(goTimer)
        
        #closes the program when 10 seconds has gone by
        if goTimer > 10:
            pygame.quit()
            quit()
        
        #updates display
        pygame.display.update()

#calls loop
main()
