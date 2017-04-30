from visual import*
from visual.controls import *
import numpy

def cos(x): #returns the cosine equivalent of the angle (in degrees)
    return numpy.cos(x*numpy.pi/180)

def sin(x): #returns the sine equivalent of the angle (in degrees)
    return numpy.sin(x*numpy.pi/180)

def reaction(): #sets what type of reaction will happen based on the user's input
    trigger = scene.kb.getkey()
    if trigger == 'a' or trigger == 'A':
        #triggers the commands for alpha decay
        while True:
            rate(100)
            alpha1.pos += alpha1.velocity
            alpha2.pos += alpha2.velocity
            alpha3.pos += alpha3.velocity
            alpha4.pos += alpha4.velocity
            if alpha3.pos.x >= paper1.pos.x - 5 or alpha1.pos.y >= paper3.pos.y - 5 or alpha2.pos.x <= paper2.pos.x + 5 or alpha4.pos.y <= paper4.pos.y + 5:
                #when the particle has hit the boundaries of the paper
                if (alphaangle-45)%90 == 0:
                    #special case when the angle is a multiple of 45 degrees
                    alpha1.velocity.x = -alpha1.velocity.x
                    alpha2.velocity.x = -alpha2.velocity.x
                    alpha3.velocity.x = -alpha3.velocity.x
                    alpha4.velocity.x = -alpha4.velocity.x
                    alpha1.velocity.y = -alpha1.velocity.y
                    alpha2.velocity.y = -alpha2.velocity.y
                    alpha3.velocity.y = -alpha3.velocity.y
                    alpha4.velocity.y = -alpha4.velocity.y
                elif alpha3.pos.x >= paper1.pos.x - 5 or alpha2.pos.x <= paper2.pos.x + 5:
                    #when the particle hits the right or left boundary
                    alpha1.velocity.x = -alpha1.velocity.x
                    alpha2.velocity.x = -alpha2.velocity.x
                    alpha3.velocity.x = -alpha3.velocity.x
                    alpha4.velocity.x = -alpha4.velocity.x
                else:
                    #when the particle hits the top or bottom boundary
                    alpha1.velocity.y = -alpha1.velocity.y
                    alpha2.velocity.y = -alpha2.velocity.y
                    alpha3.velocity.y = -alpha3.velocity.y
                    alpha4.velocity.y = -alpha4.velocity.y
            counter = 1
    if trigger == 'b' or trigger == 'B':
        #triggers the commands for beta decay
        while True:
            rate(100)
            electron.pos += electron.velocity
            if electron.pos.x >= wood1.pos.x - 5 or electron.pos.y >= wood3.pos.y - 5 or electron.pos.x <= wood2.pos.x + 5 or electron.pos.y <= wood4.pos.y + 5:
                #when the electron has hit the boundaries of the wood
                if (electronangle-45)%90 == 0:
                    #special case when the angle is a multiple of 45 degrees
                    electron.velocity.x = -electron.velocity.x
                    electron.velocity.y = -electron.velocity.y
                elif electron.pos.x >= wood1.pos.x - 5 or electron.pos.x <= wood2.pos.x + 5:
                    #when the electron hits the right or left boundary
                    electron.velocity.x = -electron.velocity.x
                else:
                    #when the electron hits the top or bottom boundary
                    electron.velocity.y = -electron.velocity.y
            counter = 1
                
    if trigger == 'g' or trigger == 'G':
        #triggers the commands for gamma decay
        while True:
            rate(100)
            gamma.pos += gamma.velocity
            if gamma.pos.x >= metal1.pos.x - 5 or gamma.pos.y >= metal3.pos.y - 5 or gamma.pos.x <= metal2.pos.x + 5 or gamma.pos.y <= metal4.pos.y + 5:
                #when the gamma ray has hit the boundaries of the metal
                if (gammaangle-45)%90 == 0:
                    #special case when the angle is a multiple of 45 degrees
                    gamma.velocity.x = -gamma.velocity.x
                    gamma.velocity.y = -gamma.velocity.y
                elif gamma.pos.x >= metal1.pos.x - 5 or gamma.pos.x <= metal2.pos.x + 5:
                    #when the gamma ray hits the right or left boundary
                    gamma.velocity.x = -gamma.velocity.x
                else:
                    #when the gamma ray hits the top or bottom boundary
                    gamma.velocity.y = -gamma.velocity.y
            counter = 1

            
#def wirecube (s): #setting the cube borders
#    c=curve (color=color.white, radius=1)
#    pts = [(-s, -s, -s),(-s, -s, s), (-s, s, s),
#           (-s, s, -s), (-s, -s, -s), (s, -s, -s),
#           (s, s, -s), (-s, s, -s), (s, s, -s),
#           (s, s, s), (-s, s, s), (s, s, s),
#           (s, -s, s), (-s, -s, s), (s, -s, s),(s, -s, -s)]
#    for pt in pts:
#        c.append(pos=pt)
        
scene = display(title='Radioactive Decay', x=0, y=0, background=(0,0,0)) #setting the size of the display screen
#wirecube(100) #create the cube
#wirecube(125)
#wirecube(150)
counter = 0

atom = sphere(pos=(0,0,0), radius=20, color=color.white)

#---creating the electron---------
electron = sphere(pos=(0,5,0), radius=2, color=color.yellow)
electronangle = 60
electronvelocity = 10
electron.velocity = vector(electronvelocity*cos(electronangle),electronvelocity*sin(electronangle),0)
#---------------------------------

#---creating the gamma ray--------
gamma = sphere(pos=(0,5,0), radius=1, color=color.yellow, make_trail=true, retain=10)
gammaangle = 60
gammavelocity = 10
gamma.velocity = vector(gammavelocity*cos(gammaangle),gammavelocity*sin(gammaangle),0)
#---------------------------------

#---creating the alpha particle---
alpha1 = sphere(pos=(0,5,0), radius=5, color=color.white)
alpha2 = sphere(pos=(-5,0,0), radius=5, color=color.red)
alpha3 = sphere(pos=(5,0,0), radius=5, color=color.red)
alpha4 = sphere(pos=(0,-5,0), radius=5, color=color.white)
alphaangle = 60
alphavelocity = 5
alpha1.velocity = vector(alphavelocity*cos(alphaangle),alphavelocity*sin(alphaangle),0)
alpha2.velocity = vector(alphavelocity*cos(alphaangle),alphavelocity*sin(alphaangle),0)
alpha3.velocity = vector(alphavelocity*cos(alphaangle),alphavelocity*sin(alphaangle),0)
alpha4.velocity = vector(alphavelocity*cos(alphaangle),alphavelocity*sin(alphaangle),0)
#---------------------------------

#---creating the paper obstacle---
paper1 = box(pos=(100,0,0), length=5, height=200, width=200)
paper2 = box(pos=(-100,0,0), length=5, height=200, width=200)
paper3 = box(pos=(0,100,0), length=200, height=5, width=200)
paper4 = box(pos=(0,-100,0), length=200, height=5, width=200)
#---------------------------------

#---creating the wood obstacle---
wood1 = box(pos=(150,0,0), length=5, height=300, width=300, material = materials.wood)
wood2 = box(pos=(-150,0,0), length=5, height=300, width=300, material = materials.wood)
wood3 = box(pos=(0,150,0), length=300, height=5, width=300, material = materials.wood)
wood4 = box(pos=(0,-150,0), length=300, height=5, width=300, material = materials.wood)
#---------------------------------

#---creating the metal obstacle---
metal1 = box(pos=(200,0,0), length=5, height=400, width=400, material = materials.silver)
metal2 = box(pos=(-200,0,0), length=5, height=400, width=400, material = materials.silver)
metal3 = box(pos=(0,200,0), length=400, height=5, width=400, material = materials.silver)
metal4 = box(pos=(0,-200,0), length=400, height=5, width=400, material = materials.silver)
#---------------------------------

#exec(open('test2.py').read()) #execute test2 script
reaction()
