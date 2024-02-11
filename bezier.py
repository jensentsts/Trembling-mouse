# -*- coding: utf-8 -*-
# @Time    : 2024/2/11 21:29
# @Author  : jensentsts
# @File    : bezier.py
# @Description : 贝塞尔曲线

import pyautogui as pag


fact = [1.0]  # 阶乘


class Bezier:
    __point_list: [pag.Point]
    __point: pag.Point | None
    __t: float
    __step_length: float
    __iter_the_tail: bool  # 迭代到最后一个点

    def __init__(self, points: list[pag.Point], step_length: float = 0.015625):
        """贝塞尔曲线"""
        self.__point_list = []
        self.__point = None  # 当前点的缓存
        self.__t = 0.0
        self.__step_length = step_length
        self.__point_list = points
        self.__iter_the_tail = False
        global fact
        if len(fact) <= len(self.__point_list):
            for i in range(len(fact), len(self.__point_list) + 1):
                fact += [fact[i - 1] * i * 1.0]

    def __len__(self):
        return 1 + 1.0 / self.__step_length

    def __iter__(self):
        self.__t = 0.0
        self.__iter_the_tail = False
        return self

    def __next__(self) -> pag.Point:
        if self.is_end():
            if not self.__iter_the_tail:
                self.__iter_the_tail = True
                return self.point
            raise StopIteration()
        res = self.point
        self.next()
        return res

    @property
    def point_list(self) -> list[pag.Point]:
        """点列表"""
        return self.__point_list

    @point_list.setter
    def point_list(self, value: list | pag.Point):
        self.__point_list = list(value)
        self.__t = 0
        self.__point = self.__point_list[0]
        # 阶乘数据更新
        global fact
        if len(fact) <= len(self.__point_list):
            for i in range(len(fact), len(self.__point_list) + 1):
                fact += [fact[i - 1] * i * 1.0]

    def is_end(self) -> bool:
        """是否结束"""
        return self.__t == 1

    @property
    def point(self) -> pag.Point:
        """当前的点坐标"""
        if self.__point is not None:
            return self.__point
        global fact
        # 计算当前的点坐标
        res = [0.0, 0.0]
        n = len(self.__point_list) - 1
        for k, val in enumerate(self.__point_list):
            para = fact[n] / (fact[k] * fact[n - k]) * (self.__t ** k) * ((1.0 - self.__t) ** (n - k))
            res[0] += para * val.x
            res[1] += para * val.y
        self.__point = pag.Point(res[0], res[1])
        return self.__point

    @property
    def t(self) -> float:
        """t"""
        return self.__t

    @t.setter
    def t(self, value: float):
        self.__t = value

    @property
    def step_length(self) -> float:
        """步长"""
        return self.__step_length

    @step_length.setter
    def step_length(self, value: float):
        if value > 1.0:
            raise ValueError
        if value < 0.0:
            raise ValueError
        self.__step_length = value

    def next(self):
        """
        下一个点
        :return:
        """
        self.__t += self.__step_length
        self.__point = None
        # 越界判定
        if self.__t > 1.0:
            self.__t = 1.0
        if self.__t < 0.0:
            self.__t = 0.0


