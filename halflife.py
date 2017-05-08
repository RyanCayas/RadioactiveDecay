from visual import *

Natoms = 100 #number of atoms
L = 1 #container is a cube L on a side

scene = display(title="Half Life Simulation", width=500, height=500, x=0, y=0,
                center=(L/2.,L/2.,L/2.))

xaxis = curve(pos=[(0,0,0), (L,0,0)])
yaxis = curve(pos=[(0,0,0), (0,L,0)])
zaxis = curve(pos=[(0,0,0), (0,0,L)])
xaxis2 = curve(pos=[(L,L,L), (0,L,L), (0,0,L), (L,0,L)])
yaxis2 = curve(pos=[(L,L,L), (L,0,L), (L,0,0), (L,L,0)])
zaxis2 = curve(pos=[(L,L,L), (L,L,0), (0,L,0), (0,L,L)])

Atoms = []
poslist = []

for i in range(Natoms):
    #Lmin = 1.1*Ratom
    #Lmax = L-Lmin
    x = random()
    y = random()
    z = random()

    Atoms.append(sphere(pos=(x,y,z), radius=5, color=color.white))
