import maya.cmds as cmds

obj = cmds.polySphere(r=2, name='mySphere#')
cmds.move(0, 2, 8)
cmds.move(0, 0, 0, obj[0]+".scalePivot", obj[0]+".rotatePivot", absolute=True)

cmds.playbackOptions( loop='continuous' )
cmds.playbackOptions( minTime='0sec', maxTime='9.6sec' )
cmds.expression(s=obj[0]+'.ry=-(time*37.5)%361')