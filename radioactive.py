from visual import*
from visual.controls import *
import numpy

def home():
    exec(open('GUI.py').read())
    scene.close()
    
def restart():
    global atom
    global electron
    global electronangle
    global electronvelocity
    global gamma
    global gammaangle
    global gammavelocity
    global alpha1
    global alpha2
    global alpha3
    global alpha4
    global alphaangle
    global alphavelocity
  
    atom = sphere(pos=(-80,0,0), radius=20, color=color.white)

    #---creating the electron---------
    electron.visible = False
    electron = sphere(pos=(-80,5,0), radius=2, color=color.yellow)
    electronangle = 20
    electronvelocity = 10
    electron.velocity = vector(electronvelocity*cos(electronangle),electronvelocity*sin(electronangle),0)
    #---------------------------------

    #---creating the gamma ray--------
    gamma.visible = False
    gamma = sphere(pos=(-80,5,0), radius=1, color=color.yellow, make_trail=true, retain=10)
    gammaangle = 20
    gammavelocity = 10
    gamma.velocity = vector(gammavelocity*cos(gammaangle),gammavelocity*sin(gammaangle),0)
    #---------------------------------

    #---creating the alpha particle---
    alpha1.visible = False
    alpha2.visible = False
    alpha3.visible = False
    alpha4.visible = False
    alpha1 = sphere(pos=(-80,5,0), radius=5, color=color.white)
    alpha2 = sphere(pos=(-85,0,0), radius=5, color=color.red)
    alpha3 = sphere(pos=(-75,0,0), radius=5, color=color.red)
    alpha4 = sphere(pos=(-80,-5,0), radius=5, color=color.white)
    alphaangle = 30
    alphavelocity = 5
    alpha1.velocity = vector(alphavelocity*cos(alphaangle),alphavelocity*sin(alphaangle),0)
    alpha2.velocity = vector(alphavelocity*cos(alphaangle),alphavelocity*sin(alphaangle),0)
    alpha3.velocity = vector(alphavelocity*cos(alphaangle),alphavelocity*sin(alphaangle),0)
    alpha4.velocity = vector(alphavelocity*cos(alphaangle),alphavelocity*sin(alphaangle),0)
    #---------------------------------

    print("HELLO WORLD")

def cos(x): #returns the cosine equivalent of the angle (in degrees)
    return numpy.cos(x*numpy.pi/180)

def sin(x): #returns the sine equivalent of the angle (in degrees)
    return numpy.sin(x*numpy.pi/180)

def reaction(): #sets what type of reaction will happen based on the user's input
    global atom
    global electron
    global electronangle
    global electronvelocity
    global gamma
    global gammaangle
    global gammavelocity
    global alpha1
    global alpha2
    global alpha3
    global alpha4
    global alphaangle
    global alphavelocity
    
    trigger = scene.kb.getkey()
    if trigger == 'a' or trigger == 'A':
        restart()
        #triggers the commands for alpha decay
        while True:
            rate(100)
            alpha1.pos += alpha1.velocity
            alpha2.pos += alpha2.velocity
            alpha3.pos += alpha3.velocity
            alpha4.pos += alpha4.velocity

            if alpha3.pos.x >= paper1.pos.x - 5:
                #when the particle has hit the boundaries of the paper
                alpha1.velocity=vector(0,0,0)
                alpha2.velocity=vector(0,0,0)
                alpha3.velocity=vector(0,0,0)
                alpha4.velocity=vector(0,0,0)
                break

    if trigger == 'b' or trigger == 'B':
        restart()
        #triggers the commands for beta decay
        while True:
            rate(100)
            electron.pos += electron.velocity
            if electron.pos.x >= wood1.pos.x - 5:
                #when the electron has hit the boundaries of the wood
                electron.velocity=vector(0,0,0)
                break
                
    if trigger == 'g' or trigger == 'G':
        restart()
        #triggers the commands for gamma decay
        while True:
            rate(100)
            gamma.pos += gamma.velocity

            if gamma.pos.x >= metal1.pos.x - 5:
                #when the gamma ray has hit the boundaries of the metal
                gamma.velocity=vector(0,0,0)
                break
            
def wirecube (s): #setting the cube borders
    c=curve (color=color.white, radius=1)
    pts = [(-s, -s, -s),(-s, -s, s), (-s, s, s),
           (-s, s, -s), (-s, -s, -s), (s, -s, -s),
           (s, s, -s), (-s, s, -s), (s, s, -s),
           (s, s, s), (-s, s, s), (s, s, s),
           (s, -s, s), (-s, -s, s), (s, -s, s),(s, -s, -s)]
    for pt in pts:
        c.append(pos=pt)

#the controls window
c = controls(x=0, y=0, width=300, height=200, range=60)
bl = button(pos=(-30,0), height=30, width=40, text='HOME', action=lambda: home())
b2 = button(pos=(30,0), height=30, width=40, text='RESET', action=lambda: restart())

scene = display(title='Radioactive Decay', x=350, y=0, background=(0,0,0)) #setting the size of the display screen
#scene.material = materials.plastic
wirecube(100) #create the cube

atom = sphere(pos=(-80,0,0), radius=20, color=color.white, material = materials.plastic)

#---creating the electron---------
electron = sphere(pos=(-80,5,0), radius=2, color=color.yellow)
electronangle = 20
electronvelocity = 10
electron.velocity = vector(electronvelocity*cos(electronangle),electronvelocity*sin(electronangle),0)
#---------------------------------

#---creating the gamma ray--------
gamma = sphere(pos=(-80,5,0), radius=1, color=color.yellow, make_trail=true, retain=10)
gammaangle = 20
gammavelocity = 10
gamma.velocity = vector(gammavelocity*cos(gammaangle),gammavelocity*sin(gammaangle),0)
#---------------------------------

#---creating the alpha particle---
alpha1 = sphere(pos=(-80,5,0), radius=5, color=color.white)
alpha2 = sphere(pos=(-85,0,0), radius=5, color=color.red)
alpha3 = sphere(pos=(-75,0,0), radius=5, color=color.red)
alpha4 = sphere(pos=(-80,-5,0), radius=5, color=color.white)
alphaangle = 30
alphavelocity = 5
alpha1.velocity = vector(alphavelocity*cos(alphaangle),alphavelocity*sin(alphaangle),0)
alpha2.velocity = vector(alphavelocity*cos(alphaangle),alphavelocity*sin(alphaangle),0)
alpha3.velocity = vector(alphavelocity*cos(alphaangle),alphavelocity*sin(alphaangle),0)
alpha4.velocity = vector(alphavelocity*cos(alphaangle),alphavelocity*sin(alphaangle),0)
#---------------------------------

#---creating the paper obstacle---
paper1 = box(pos=(0,0,0), length=5, height=200, width=200)
#---------------------------------

#---creating the wood obstacle---
wood1 = box(pos=(50,0,0), length=5, height=200, width=200, material = materials.wood)
#---------------------------------

#---creating the metal obstacle---
metal1 = box(pos=(100,0,0), length=5, height=200, width=200, material = materials.silver)
#---------------------------------

#exec(open('test2.py').read()) #execute test2 script
while True:
    reaction()
