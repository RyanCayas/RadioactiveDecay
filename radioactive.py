from visual import*
from visual.controls import *
import numpy

def home():
    exec(open('GUI.py').read())
    
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
  

    #---creating the electron---------
    electron.visible = False
    electron = sphere(pos=(-80,5,0), radius=2, color=color.yellow)
    electronangle = 20
    electronvelocity = 10
    electron.velocity = vector(electronvelocity*cos(electronangle),electronvelocity*sin(electronangle),0)
    #---------------------------------

    #---creating the gamma ray--------
    gamma.trail_object.visible = False
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
        x = 0
        while x<100: #marks the particles about to decay + cool transition!
            rate(100)
            if x%2==0:
                atom23.color = color.yellow
                atom24.color = color.yellow
                atom25.color = color.yellow
                atom26.color = color.yellow
            else:
                atom23.color = color.red
                atom24.color = color.white
                atom25.color = color.red
                atom26.color = color.white
            x+=1

        while True:
            rate(100)
            alpha1.pos += alpha1.velocity
            alpha2.pos += alpha2.velocity
            alpha3.pos += alpha3.velocity
            alpha4.pos += alpha4.velocity

            if alpha3.pos.x >= paper1.pos.x - 10:
                #when the particle has hit the boundaries of the paper
                alpha1.velocity=vector(0,0,0)
                alpha2.velocity=vector(0,0,0)
                alpha3.velocity=vector(0,0,0)
                alpha4.velocity=vector(0,0,0)
                exec(open('alphadecay.py').read())
                break

    if trigger == 'b' or trigger == 'B':
        restart()
        #triggers the commands for beta decay
        x = 0
        while x<100: #marks the particles about to decay + cool transition!
            rate(100)
            if x%2==0:
                atom26.color = color.yellow
            else:
                atom26.color = color.white
            x+=1
        atom26.color = color.red
        while True:
            rate(100)
            electron.pos += electron.velocity
            if electron.pos.x >= wood1.pos.x - 7.5:
                #when the electron has hit the boundaries of the wood
                electron.velocity=vector(0,0,0)
                exec(open('betadecay.py').read())
                break
                
    if trigger == 'g' or trigger == 'G':
        restart()
        #triggers the commands for gamma decay
        #marks the particles about to decay + cool transition!-------------------------------
        x = 0
        while x<100: 
            rate(100)
            if x%2==0:
                atom1.color = color.yellow
                atom2.color = color.yellow
                atom3.color = color.yellow
                atom4.color = color.yellow
                atom5.color = color.yellow
                atom6.color = color.yellow
                atom7.color = color.yellow
                atom8.color = color.yellow
                atom9.color = color.yellow
                atom10.color = color.yellow
                atom11.color = color.yellow
                atom12.color = color.yellow
                atom13.color = color.yellow
                atom14.color = color.yellow
                atom15.color = color.yellow
                atom16.color = color.yellow
                atom17.color = color.yellow
                atom18.color = color.yellow
                atom19.color = color.yellow
                atom20.color = color.yellow
                atom21.color = color.yellow
                atom22.color = color.yellow
                atom23.color = color.yellow
                atom24.color = color.yellow
                atom25.color = color.yellow
                atom26.color = color.yellow
                atom27.color = color.yellow
                atom28.color = color.yellow
                atom29.color = color.yellow
                atom30.color = color.yellow
                atom31.color = color.yellow
                atom32.color = color.yellow
                atom33.color = color.yellow
                atom34.color = color.yellow
                atom35.color = color.yellow
                atom36.color = color.yellow
                atom37.color = color.yellow
                atom38.color = color.yellow
                atom39.color = color.yellow
                atom40.color = color.yellow
                atom41.color = color.yellow
                atom42.color = color.yellow
                atom43.color = color.yellow
                atom44.color = color.yellow
                atom45.color = color.yellow
                atom46.color = color.yellow
            else:
                atom1.color = color.white
                atom2.color = color.white
                atom3.color = color.white
                atom4.color = color.white
                atom5.color = color.white
                atom6.color = color.white
                atom7.color = color.white
                atom8.color = color.white
                atom9.color = color.red
                atom10.color = color.white
                atom11.color = color.white
                atom12.color = color.white
                atom13.color = color.white
                atom14.color = color.white
                atom15.color = color.white
                atom16.color = color.white
                atom17.color = color.white
                atom18.color = color.white
                atom19.color = color.white
                atom20.color = color.white
                atom21.color = color.white
                atom22.color = color.white
                atom23.color = color.red
                atom24.color = color.white
                atom25.color = color.red
                atom26.color = color.white
                atom27.color = color.red
                atom28.color = color.white
                atom29.color = color.white
                atom30.color = color.red
                atom31.color = color.red
                atom32.color = color.white
                atom33.color = color.red
                atom34.color = color.white
                atom35.color = color.white
                atom36.color = color.red
                atom37.color = color.red
                atom38.color = color.white
                atom39.color = color.white
                atom40.color = color.red
                atom41.color = color.red
                atom42.color = color.white
                atom43.color = color.white
                atom44.color = color.red
                atom45.color = color.red
                atom46.color = color.white
            x+=1
            #end of cool transition----------------------------
        while True:
            rate(100)
            gamma.pos += gamma.velocity

            if gamma.pos.x >= metal1.pos.x - 7.5:
                #when the gamma ray has hit the boundaries of the metal
                gamma.trail_object.visible = False
                gamma.velocity=vector(0,0,0)
                exec(open('gammadecay.py').read())
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
scene.exit = False
scene.material = materials.plastic
wirecube(100) #create the cube

#atom = sphere(pos=(-80,0,0), radius=20, color=color.white, material = materials.plastic)
#---creating the atom---

atom1 = sphere(pos=(-80,0,-5), radius=5, color=color.white)
atom2 = sphere(pos=(-80,0,5), radius=5, color=color.white)
atom3 = sphere(pos=(-80,5,5), radius=5, color=color.white)
atom4 = sphere(pos=(-80,-5,5), radius=5, color=color.white)
atom5 = sphere(pos=(-80,5,-5), radius=5, color=color.white)
atom6 = sphere(pos=(-80,-5,-5), radius=5, color=color.white)
atom7 = sphere(pos=(-85,0,-5), radius=5, color=color.white)
atom8 = sphere(pos=(-85,0,5), radius=5, color=color.white)
atom9 = sphere(pos=(-85,5,5), radius=5, color=color.red)
atom10 = sphere(pos=(-85,-5,5), radius=5, color=color.white)
atom11 = sphere(pos=(-85,5,-5), radius=5, color=color.white)
atom12 = sphere(pos=(-85,-5,-5), radius=5, color=color.white)
atom13 = sphere(pos=(-75,0,-5), radius=5, color=color.white)
atom14 = sphere(pos=(-75,0,5), radius=5, color=color.white)
atom15 = sphere(pos=(-75,5,5), radius=5, color=color.white)
atom16 = sphere(pos=(-75,-5,5), radius=5, color=color.white)
atom17 = sphere(pos=(-75,5,-5), radius=5, color=color.white)
atom18 = sphere(pos=(-75,-5,-5), radius=5, color=color.white)
atom19 = sphere(pos=(-85,5,0), radius=5, color=color.white)
atom20 = sphere(pos=(-85,-5,0), radius=5, color=color.white)
atom21 = sphere(pos=(-75,5,0), radius=5, color=color.white)
atom22 = sphere(pos=(-75,-5,0), radius=5, color=color.white)

atom23 = sphere(pos=(-77.5,2.5,7.5), radius=5, color=color.red)
atom24 = sphere(pos=(-82.5,2.5,7.5), radius=5, color=color.white)
atom25 = sphere(pos=(-82.5,-2.5,7.5), radius=5, color=color.red)
atom26 = sphere(pos=(-77.5,-2.5,7.5), radius=5, color=color.white)

atom27 = sphere(pos=(-87.5,-2.5,2.5), radius=5, color=color.red)
atom28 = sphere(pos=(-87.5,-2.5,-2.5), radius=5, color=color.white)
atom29 = sphere(pos=(-87.5,2.5,2.5), radius=5, color=color.white)
atom30 = sphere(pos=(-87.5,2.5,-2.5), radius=5, color=color.red)

atom31 = sphere(pos=(-77.5,2.5,-7.5), radius=5, color=color.red)
atom32 = sphere(pos=(-82.5,2.5,-7.5), radius=5, color=color.white)
atom33 = sphere(pos=(-82.5,-2.5,-7.5), radius=5, color=color.red)
atom34 = sphere(pos=(-77.5,-2.5,-7.5), radius=5, color=color.white)

atom35 = sphere(pos=(-72.5,-2.5,2.5), radius=5, color=color.white)
atom36 = sphere(pos=(-72.5,-2.5,-2.5), radius=5, color=color.red)
atom37 = sphere(pos=(-72.5,2.5,2.5), radius=5, color=color.red)
atom38 = sphere(pos=(-72.5,2.5,-2.5), radius=5, color=color.white)

atom39 = sphere(pos=(-82.5,7.5,2.5), radius=5, color=color.white)
atom40 = sphere(pos=(-82.5,7.5,-2.5), radius=5, color=color.red)
atom41 = sphere(pos=(-77.5,7.5,2.5), radius=5, color=color.red)
atom42 = sphere(pos=(-77.5,7.5,-2.5), radius=5, color=color.white)

atom43 = sphere(pos=(-82.5,-7.5,2.5), radius=5, color=color.white)
atom44 = sphere(pos=(-82.5,-7.5,-2.5), radius=5, color=color.red)
atom45 = sphere(pos=(-77.5,-7.5,2.5), radius=5, color=color.red)
atom46 = sphere(pos=(-77.5,-7.5,-2.5), radius=5, color=color.white)
#---------------------------------

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

while True:
    reaction() #runs the simulation showing the three types of decay indefinitely until the user exits the window
