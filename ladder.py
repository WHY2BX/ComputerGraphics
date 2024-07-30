import maya.cmds as cmds
for i in range(30):
    cmds.polyCube(w=5,h=0.25,d=1)
    cmds.move(2.5,0.5*i,-0.5)
    cmds.rotate(0,12*i,0,p=[0,0,0])