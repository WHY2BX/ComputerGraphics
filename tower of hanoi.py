import maya.cmds as cmds
cmds.polyCube(w=12, h=0.5, d=5)

cmds.polyCylinder(r=0.1, h=4)
cmds.move(-3,2)
cmds.polyCylinder(r=0.1, h=4)
cmds.move(0,2)
cmds.polyCylinder(r=0.1, h=4)
cmds.move(3,2)

#(0.75, 0.5, 0.5) , (1, 0.5, 0.75), (1.25, 0.5, 1), (1.5, 0.5, 1.25) และ (1.75, 0.5, 1.5)

cmds.polyPipe(r=0.75, h=0.5, t=0.5)
cmds.move(0,1.37)
cmds.polyPipe(r=1, h=0.5, t=0.75)
cmds.move(0,1.12)
cmds.polyPipe(r=1.25, h=0.5, t=1)
cmds.move(0,0.87)
cmds.polyPipe(r=1.5, h=0.5, t=1.25)
cmds.move(0, 0.62)
cmds.polyPipe(r=1.75, h=0.5, t=1.5)
cmds.move(0,0.38)
