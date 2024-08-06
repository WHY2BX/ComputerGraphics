import maya.cmds as cmds

obj = cmds.polySphere(r=2, name='mySphere#')
cmds.move(0, 2, 8)
cmds.move(0, 0, 0, obj[0]+".scalePivot", obj[0]+".rotatePivot", absolute=True)

cmds.setKeyframe(obj, at='ty', t=1)
cmds.setKeyframe(obj, at='tx', t=1)


for i in range(9):
    cmds.rotate(0,45*i,0, p=[0,0,0])
    cmds.setKeyframe(obj,t=i*30)
