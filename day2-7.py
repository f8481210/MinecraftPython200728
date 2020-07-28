# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:17:02 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

name = input("你的名字：")
message = input("你想說的話：")

mc.postToChat("[ "+name+" ]"+message)