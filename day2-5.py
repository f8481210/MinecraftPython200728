# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:02:45 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    x,y,z = mc.player.getTilePos()

    a = mc.getBlock(x,y-1,z+1) #前面
    b = mc.getBlock(x,y-1,z-1) #後面
    c = mc.getBlock(x+1,y-1,z) #右邊
    d = mc.getBlock(x-1,y-1,z) #左邊

    if a == 9 or b == 9 \
        or c == 9 or d == 9 :
            mc.setBlocks(x-1,y-1,z-1,
                         x+1,y-1,z+1,79)






