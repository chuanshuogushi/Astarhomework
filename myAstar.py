"""模式识别与智能系统技术
路径规划-A*算法-启发式搜索
"""
import matplotlib.pyplot as plt
import numpy as np
import imageio
from config import *


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.dad = None

    def cal_f(self, dad, final_node):
        """计算估价函数值"""
        self.dad = dad
        if abs(dad.x-self.x)+abs(dad.y-self.y) == 1:
            self.g = dad.g+1
        else:
            self.g = dad.g+1.414
        # self.g = #dad.g + 1  # 深度加一
        self.h = abs(self.x - final_node.x) + abs(self.y - final_node.y)  # 曼哈顿距离
        self.f = self.g + self.h

    def same_loc(self, x, y):
        """判断节点位置是否一样"""
        if self.x == x and self.y == y:
            return True

    def explorable(self, open_list, close_list):
        if self.x < 0 or self.x >= len(my_map) or self.y < 0 or self.y >= len(my_map[0]):  # 是否超过边界f
            return False
        if my_map[self.x][self.y] == 1:  # 判断障碍物
            return False
        if has_node(open_list, self.x, self.y) or has_node(close_list, self.x, self.y):  # 在表中
            return False
        return True


def A_star(s_node, f_node):
    """A*算法实现
    :param s_node:初始点2
    :param f_node:目标点"""
    open_list = [s_node]  # OPEN表
    close_list = []  # CLOSE表
    while len(open_list) > 0:
        now_node = get_min_f_node(open_list)  # 得到f最小节点
        open_list.remove(now_node)  # 探索完毕，open表中删除
        close_list.append(now_node)  # 加入close表中
        near_nodes = gen_near_nodes(now_node, open_list, close_list)  # 下一层节点
        for near_node in near_nodes:  # 计算f，添加父子关系，放入open表中
            near_node.cal_f(now_node, f_node)
            open_list.append(near_node)
            print_result(near_node,'result')
        for near_node in open_list:  # 查询是否搜到目标点
            if near_node.same_loc(f_node.x, f_node.y):
                return near_node
    # Open表为空，所有节点遍历完，无法找到结果，退出
    return None


def get_min_f_node(open_list):
    """得到open_list中f最小的node"""
    if open_list is None:
        open_list = []
    min_f_node = open_list[0]
    for node in open_list:
        if node.f < min_f_node.f:
            min_f_node = node
    return min_f_node


def gen_near_nodes(node, open_list, close_list):
    """产生下一层节点"""
    near_nodes = []
    new_node = Node(node.x, node.y - 1)
    if new_node.explorable(open_list, close_list):
        near_nodes.append(new_node)
    new_node = Node(node.x, node.y + 1)
    if new_node.explorable(open_list, close_list):
        near_nodes.append(new_node)
    new_node = Node(node.x - 1, node.y)
    if new_node.explorable(open_list, close_list):
        near_nodes.append(new_node)
    new_node = Node(node.x + 1, node.y)
    if new_node.explorable(open_list, close_list):
        near_nodes.append(new_node)
    new_node = Node(node.x + 1, node.y + 1)
    if new_node.explorable(open_list, close_list):
        near_nodes.append(new_node)
    new_node = Node(node.x + 1, node.y - 1)
    if new_node.explorable(open_list, close_list):
        near_nodes.append(new_node)
    new_node = Node(node.x - 1, node.y + 1)
    if new_node.explorable(open_list, close_list):
        near_nodes.append(new_node)
    new_node = Node(node.x - 1, node.y - 1)
    if new_node.explorable(open_list, close_list):
        near_nodes.append(new_node)
    return near_nodes


def has_node(nodes, x, y):
    """判断某节点是否在节点集中"""
    for node in nodes:
        if node.same_loc(x, y):
            return True
    return False


p = 0


def plot_map(m, m_type):
    """"以热力图形式画出地图"""
    global p
    plt.figure()
    plt.imshow(m, cmap='bwr', vmin=0, vmax=2)
    if m_type == 'result':
        plt.title('寻路结果图')
    elif m_type == 'begin':
        plt.title('初始地图')
    plt.savefig('%s.jpg' % p)
    p = p+1
    plt.show()


def print_result(result, m_type):
    """输出结果
    :param result:结果节点
    :param m_type:地图类型
    """
    route = []  # 存储路线
    final_map = np.zeros_like(np.array(my_map))  # 初始化
    if result is None:  # 找不到路径，路被障碍堵住或者目标点为障碍
        print('Cannot find a way！！！')
    else:
        while result is not None:
            route.append(Node(result.x, result.y))
            result = result.dad
        # 得到最终地图
        for i in range(len(my_map)):
            for j in range(0, len(my_map[0])):
                if has_node(route, i, j):
                    final_map[i][j] = 2
                else:
                    final_map[i][j] = my_map[i][j]
    plot_map(final_map, m_type)


if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plot_map(my_map, m_type='begin')  # 展示初始地图
    first_node = Node(f_x, f_y)  # 初始点
    des_node = Node(d_x, d_y)  # 目标点
    assert f_x < len(my_map) and f_y < len(my_map[0])  # 保证在地图内取点
    assert d_x < len(my_map) and d_y < len(my_map[0])  # 保证在地图内取点
    result_node = A_star(first_node, des_node)    # A*算法查询
    print_result(result_node, m_type='result')   # 结果展示
