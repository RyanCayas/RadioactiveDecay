from visual import *
from random import random
from visual.graph import *
import numpy


def cos(x): #returns the cosine equivalent of the angle (in degrees)
    return numpy.cos(x*numpy.pi/180)

def sin(x): #returns the sine equivalent of the angle (in degrees)
    return numpy.sin(x*numpy.pi/180)

L = 1
variable = [] #checks if the atom has decayed already
counter =0 #checks if the atom has decayed already
while(counter<Natoms):
    variable.append(0)
    counter+=1
scene = display(title="Half Life Simulation", width=500, height=500, x=0, y=0,
                center=(L/2.,L/2.,L/2.)) #creates the canvass

graph = gdisplay(xtitle='Time', ytitle='Number of Atoms Left', x=500, y=0)  #initializes the graph
funct1 = gcurve(color=color.cyan) #initializes the function to be graphed

#creating the borders of the simulation------------
xaxis = curve(pos=[(0,0,0), (L,0,0)])
yaxis = curve(pos=[(0,0,0), (0,L,0)])
zaxis = curve(pos=[(0,0,0), (0,0,L)])
xaxis2 = curve(pos=[(L,L,L), (0,L,L), (0,0,L), (L,0,L)])
yaxis2 = curve(pos=[(L,L,L), (L,0,L), (L,0,0), (L,L,0)])
zaxis2 = curve(pos=[(L,L,L), (L,L,0), (0,L,0), (0,L,L)])
#---------------------------------------------------

Atoms = []
alpha1 = []
alpha2 = []
alpha3 = []
alpha4 = []
alpha1velocity = []
alpha2velocity = []
alpha3velocity = []
alpha4velocity = []
alphavelocity = 0.01

for i in range(Natoms): #generates random numbers for the position of the atoms as well as the angle for the ejection of the alpha particle
    Lmin = 1.1*0.04
    Lmax = L-Lmin
    x = Lmin+(Lmax-Lmin)*random()
    y = Lmin+(Lmax-Lmin)*random()
    z = Lmin+(Lmax-Lmin)*random()
    alphaangle = random()*360

    #adds the generated random values to the empty lists------------------------------------
    Atoms.append(sphere(pos=(x,y,z), radius=0.04, color=color.white))
    alpha1.append(sphere(pos=(x,y+0.01,z), radius=0.01, color=color.white))
    alpha2.append(sphere(pos=(x-0.01,y,z), radius=0.01, color=color.red))
    alpha3.append(sphere(pos=(x+0.01,y,z), radius=0.01, color=color.red))
    alpha4.append(sphere(pos=(x,y-0.01,z), radius=0.01, color=color.white))
    alpha1velocity.append(vector(alphavelocity*cos(alphaangle),alphavelocity*sin(alphaangle),0))
    alpha2velocity.append(vector(alphavelocity*cos(alphaangle),alphavelocity*sin(alphaangle),0))
    alpha3velocity.append(vector(alphavelocity*cos(alphaangle),alphavelocity*sin(alphaangle),0))
    alpha4velocity.append(vector(alphavelocity*cos(alphaangle),alphavelocity*sin(alphaangle),0))
    #----------------------------------------------------------------------------------------


t=0.0
while True: #applies the formula for half life decay to count the number of atoms remaining
    Remaining = Natoms*((0.5)**(t/Hlife))
    if Remaining > 0.1:
        funct1.plot(pos=(t,Remaining))
    Remaining = int(Remaining)
    for i in range(Natoms-Remaining): #handles the decay of the atoms
        rate(speed)
        k = 0
        if variable[i]==0:
            while k<100: #marks the particles about to decay + cool transition!
                rate(100)
                if k%2==0:
                    Atoms[i].color = color.yellow
                else:
                    Atoms[i].color = color.white
                k+=1
            variable[i]=1
        Atoms[i].color = color.yellow
        while True: #ejection of the alpha particle
            rate(speed)
            alpha1[i].pos += alpha1velocity[i]
            alpha2[i].pos += alpha2velocity[i]
            alpha3[i].pos += alpha3velocity[i]
            alpha4[i].pos += alpha4velocity[i]

            if alpha3[i].pos.x >= L or alpha1[i].pos.y >= L or alpha2[i].pos.x <= 0 or alpha4[i].pos.y <= 0:
                #when the particle has hit the boundaries of the paper
                alpha1velocity[i]=vector(0,0,0)
                alpha2velocity[i]=vector(0,0,0)
                alpha3velocity[i]=vector(0,0,0)
                alpha4velocity[i]=vector(0,0,0)
                break
    t+=1

    



