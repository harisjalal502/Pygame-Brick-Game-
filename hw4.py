import pygame
from Drawable import Drawable
from Ball import Ball
from Block import Block
from Text import Text


class Line(Drawable): #Line Class to draw the ground plane
    color = 0,0,0 #line color
    width = 1 #line width

    def __init__(self, start, end, visible=True):
        self.start = start #start point of the line
        self.end = end #end point
        self.visible = visible #visibility Boolean
        #Calculating the rectangle of the line
        #pygame.Rect(x, y, width, height)
        self.rect = pygame.Rect(*self.position,
                                self.end[0]-self.start[0],
                                self.end[1]-self.end[0])

    def draw(self, surface):
        #draw line if visible
        if self.visible:
            #pygame.draw.line(surface, color, start_point, end_point, width)
            self.rect = pygame.draw.line(surface, self.color, self.start, self.end, self.width)

    def get_rect(self):
        return self.rect #return the lines rect


#function given in the document
#returns True if rect1 collides with rect2
def intersect(rect1,rect2):
    if (rect1.x < rect2.x + rect2.width
        and rect1.x + rect1.width > rect2 .x
        and rect1.y < rect2.y + rect2.height
        and rect1.height + rect1.y > rect2.y):
        return True
    return False

#load the highscore as integer from textfile
#if theres no file, highscore is 0
try:
    highscore = int(open("Highscore.txt").read())
except:
    highscore = 0

            
#Initialize all 6 PyGame modules
pygame.init()

resolution = 500,500 #window size
display = pygame.display.set_mode(resolution) #create window
Clock = pygame.time.Clock() #PyGame clock module to keep 60fps in this game

background = pygame.transform.smoothscale(pygame.image.load("Background.png").convert(), resolution)
#create highscore and normal score text
#Text(position, text, visible=True)
highscoretext = Text([0,0], "Highscore: "+str(highscore))
highscoretext.position[0] = resolution[0]-highscoretext.get_rect()[2] #align text to the right
scoretext = Text([0,0], "Score: 0")

wintext = Text([50,200], "You completed the level! Try again!", False, pygame.font.SysFont("", 35))
wintext.color = highscoretext.color = scoretext.color = 255,255,255

ground_plane = Line((0,400), (500,400)) #create ground_plane Line class
ball = Ball([20,400]) #create Ball class


blocks = [] #list with all 9 blocks

#create 3x3 blocks with size 20 --> 9 blocks
#starting at x-position 400 and y-position 340
y = 340
for i in range(3):
    x = 400
    for n in range(3):
        blocks.append(Block([x, y]))
        x += 20
    y += 20



drag_start = None #will contain a tuple with the mouse cursor position on click
#Variables given in the document:
dt = .1 #delta time constant
g = 6.67 #gravity constant
R = .7 #rebound constant
eta = .5 #friction constant

xv = 0 #changing velocity on x-axis
yv = 0 #changing velocity on y-axis

score = 0 #current score

#Start game loop
#Game stops when running is False
running = True
win = 0
while running:
    MousePos = pygame.mouse.get_pos() #get mouse cursor position
    for event in pygame.event.get():

        #Quit the game when closing the window
        if event.type == pygame.QUIT:
            running = False

        #Mouse click event (save mouse position)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drag_start = MousePos

        #Mouse button up event
        #calculate velocity by subtracting the old position by the new position
        elif event.type == pygame.MOUSEBUTTONUP:
            drag_end = MousePos
            xv = drag_end[0]-drag_start[0] #set new x-velocity
            yv = drag_end[1]-drag_start[1] #set new y-velocity

    #gravity impact on the ball if ball is over the ground
    if ball.position[1] < ground_plane.start[1]:
        yv += g*dt

    #change ball position by velocity*delta time
    ball.position[0] += dt*xv
    ball.position[1] += dt*yv

    #ball rebounce when hitting the ground
    if ball.position[1] > ground_plane.start[1] and yv > 0:
        yv *= -R
        xv *= eta

    elif ball.position[1] < 0 and yv < 0:
        yv *= -R
        xv *= eta

    if ball.position[0] < 0 and xv < 0:
        xv *= -R
        yv *= eta

    elif ball.position[0] > resolution[0] and xv > 0:
        xv *= -R
        yv *= eta
            

    #background image
    display.blit(background, (0,0))

    #draw ground plane and ball
    ground_plane.draw(display)
    ball.draw(display)
    
    #run function for every block in the blocks list
    for block in blocks:
        #if ball collides with block
        if block.visible and intersect(block.get_rect(), ball.get_rect()):
            block.visible = False #set visibility of the block to False
            score += 1 #count score
            scoretext.text = "Score: "+str(score) #refresh score text

            #if new highscore
            if score > highscore:
                highscore = score #apply new highscore
                highscoretext.text = "Score: "+str(highscore) #refresh highscore text

        #draw the block (will be drawn if visible variable is True)
        block.draw(display)

    if score >= 9:
        rect = pygame.Surface(resolution)
        rect.set_alpha(200)
        rect.fill((0,0,0))
        display.blit(rect, (0,0))
        wintext.visible = True
        
    #dipslay score and highscore
    scoretext.draw(display)
    highscoretext.draw(display)
    wintext.draw(display)

    #update the screen and delay to keep 60 frames per second
    pygame.display.update()
    Clock.tick(60)

#after quitting the game:
open("Highscore.txt", "w+").write(str(highscore)) #save highscore in text file
pygame.display.quit() #uninitialize display module first for faster window closing
pygame.quit() #end PyGame
