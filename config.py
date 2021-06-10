import random
from random import randint


def create_random_map(w, h, o_num, s):
    """创建随机地图
    :param w:宽度
    :param h:高度
    :param o_num:障碍块个数
    :param s:随机数种子"""
    random.seed(s)
    random_map = [[0 for x in range(w)] for y in range(h)]
    for i in range(o_num):
        x, y = (randint(0, w - 1), randint(0, h - 1))
        random_map[y][x] = 1
    return random_map


random_map = False  # 是否随机地图
if random_map is True:
    width = 20
    height = 20
    obstacle_num = 100  # 170
    seed = 18374288
    my_map = create_random_map(width, height, obstacle_num, seed)  # 选择随机地图
    f_x, f_y = 0, 0  # first和destination坐标
    d_x, d_y = 18, 18
else:
    my_map = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    ]  # 题中所给地图
    f_x, f_y = 2, 2  # first和destination坐标
    d_x, d_y = 8, 8
