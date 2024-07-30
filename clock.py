import maya.cmds as cmds
for i in range(12):
    cmds.polySphere(r=1, name='time#')
    cmds.move(0, 6, 0)
    cmds.rotate(30*i,0,0,p=[0,0,0])

cmds.polyCube(w=4.8, h=0.5, d=0.5)
cmds.rotate(0,0,90)
cmds.move(0,2.4,0)

cmds.polyCube(w=4, h=0.5, d=0.5)
cmds.rotate(0,90,0)
cmds.move(0,0,-1.75)