# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 09:32:06 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

mc.setBlock(x+2,y,z,35,13)
mc.setBlock(x-2,y,z,35,12)
mc.setBlock(x,y,z+2,35,11)
mc.setBlock(x,y,z-2,35,10)
mc.setBlock(x+1,y,z+1,35,14)
mc.setBlock(x-1,y,z+1,35,15)
mc.setBlock(x+1,y,z-1,35,9)
mc.setBlock(x-1,y,z-1,35,8)



