import maya.cmds as cmds
for i in range(18):
    cmds.polyCube(w=4, h=0.5, d=4/3, name='base%d_1' %i)
    cmds.polyCube(w=4, h=0.5, d=4/3, name='base%d_2' %i)
    if(i%2!=0):
        cmds.rotate(0,180,0)
        cmds.move(0,0.5*i,4/3)
        cmds.select('base%d_1'%i)
        cmds.rotate(0,180,0)
        cmds.move(0,0.5*i,-4/3)
    else:
        cmds.rotate(0,90,0)
        cmds.move(4/3,0.5*i,0)
        cmds.select('base%d_1'%i)
        cmds.rotate(0,90,0)
        cmds.move(-4/3,0.5*i,0)