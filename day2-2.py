# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:11:32 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random,time

while True:
    x,y,z = mc.player.getTilePos()

    color = random.randrange(0,16)
    mc.setBlocks(x+25,y-1,z+25,
             x-25,y-1,z-25,95,color)
    time.sleep(0.5)