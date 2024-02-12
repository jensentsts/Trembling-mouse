# -*- coding: utf-8 -*-
# @Time    : 2024/2/11 21:18
# @Author  : jensentsts
# @File    : main.py
# @Description : 抖手模拟器main

import pyautogui as pag
import random
import time
import bezier

range_left = -32
range_right = 32


def random_move():
    """随机移动"""
    screen_size = pag.size()
    while True:
        mouse_pos = pag.position()
        if mouse_pos.x == 0 and mouse_pos.y == 0 or \
                mouse_pos.x >= screen_size.width - 2 and mouse_pos.y >= screen_size.height - 2:
            exit(0)
        move_x = mouse_pos.x + random.randint(range_left, range_right)
        move_y = mouse_pos.y + random.randint(range_left, range_right)
        if move_x < 0:
            move_x = 0
        if move_x > screen_size.width:
            move_x = screen_size.width - 2
        if move_y < 0:
            move_y = 0
        if move_y > screen_size.height:
            move_y = screen_size.height - 2
        try:
            pag.moveTo(move_x, move_y)
        except pag.FailSafeException as e:
            print(mouse_pos, e)
            continue


def bezier_move():
    """
    贝塞尔随机移动
    """
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
        for i in bezier.Bezier(point_list, step_length=0.125):
            mouse_pos = pag.position()
            if mouse_pos.x == 0 and mouse_pos.y == 0 or \
                    mouse_pos.x >= screen_size.width - 2 and mouse_pos.y >= screen_size.height - 2:
                exit(0)
            move_x = int(i.x - last_x + mouse_pos.x)
            move_y = int(i.y - last_y + mouse_pos.y)
            last_x = i.x
            last_y = i.y
            if move_x < 0:
                move_x = 0
            if move_x > screen_size.width:
                move_x = screen_size.width - 2
            if move_y < 0:
                move_y = 0
            if move_y > screen_size.height:
                move_y = screen_size.height - 2
            try:
                pag.moveTo(move_x, move_y)
            except pag.FailSafeException as e:
                print(mouse_pos, e)
                continue


if __name__ == '__main__':
    random_move()
