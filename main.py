# -*- coding: utf-8 -*-
# @Time    : 2024/2/11 21:18
# @Author  : jensentsts
# @File    : main.py
# @Description : 抖手模拟器main

import pyautogui as pag
import random
import time
import bezier

range_left = -256
range_right = 256

if __name__ == '__main__':
    print("How to stop the program:")
    print("Move your mouse to the left-up or right-down point of your screen, then it will break down.")
    screen_size = pag.size()
    while True:
        [x, y] = [0, 0]
        [last_x, last_y] = [0, 0]
        point_list = []
        for i in range(0, random.randint(2, 8)):
            x += random.randint(range_left, range_right)
            y += random.randint(range_left, range_right)
            point_list += [pag.Point(x, y)]
        print(point_list)
        for i in bezier.Bezier(point_list):
            mouse_pos = pag.position()
            move_x = int(i.x - last_x + mouse_pos.x)
            move_y = int(i.y - last_y + mouse_pos.y)
            last_x = i.x
            last_y = i.y
            if move_x < 0:
                move_x = 0
            if move_x > screen_size.width:
                move_x = screen_size.width - 1
            if move_y < 0:
                move_y = 0
            if move_y > screen_size.height:
                move_y = screen_size.height - 1
            pag.moveTo(move_x, move_y)

