import copy
import json
import os

import numpy as np
import re
import scipy

import pandas
import keras

import cv2

class classDef(object):
    def __init__(self, bounds, component_class,pointer, parent):
        self.bounds = bounds
        self.pointer=pointer
        self.component_class = component_class
        self.parent = parent
        self.children = []

    def __eq__(self, other):
        return self.bounds == other.bounds and self.component_class == other.component_class  # 如果两个bounds和class相等则他们相等

error_num = 0
right_num = 0
uncertain_num_collect = {}
def read_data():
    files = os.listdir('./ATMobile2020-1/ATMobile2020-1')
    json_files = {}
    for file in files:
        if file.endswith('.json'):
            json_files[file.replace('.json', '')] = json.load(open(os.path.join('ATMobile2020-1/ATMobile2020-1', file), 'r', encoding='utf-8'))
    return json_files


def dfs(root: classDef, data):
    if 'children' not in data:
        return
    global uncertain_num
    global error_num

    for child in data['children']:

        if child is None:
            continue

        t = r'[a-zA-Z0-9]*\.[a-zA-Z0-9]*'
        if ((re.match(t, child["class"]) == None) == True):
            uncertain_num += 1
            uncertain_num_collect[child["pointer"]] = child["class"]

        assert child['class'] is not None
        assert 'bounds' in child
        assert 'class' in child
        root_dis(child)
        node = classDef(child['bounds'], child['class'], child['pointer'], root)
        root.children.append(node)
        dfs(node, child)
    de_children = []
    for c in root.children:
        if c not in de_children:
            de_children.append(c)
    root.children = de_children


def de_data(data):  # 解析数据
    root = data['activity']['root']
    root_dis(root)
    root_node = classDef(root['bounds'], root['class'], root['pointer'], None)
    dfs(root_node, root)
    # json.dump(component, open('tmp.json', 'w', encoding='utf-8'))
    return root_node

total_num=0
zero=0
uncertain_num=0
zero_collect={}
error_collect={}
def root_dis(root):
    global error_num  # 冗余
    global total_num
    global right_num
    global uncertain_num  # class不存在
    global zero  # bounds is zero
    array_zero = np.array([0, 0, 0, 0])
    # 以下是判断是否是[0,0,0,0]
    if ('parent' in root):
        total_num += 1
        array_a = np.array(root['bounds'])
        if ((array_a == array_zero).all() == False):
            right_num += 1
        else:
            zero += 1
            zero_collect[root['pointer']] = root["class"]
            # print(zero_collect)
    else:  # 不是root
        total_num += 1
        array_a = np.array(root['bounds'])
        if ((array_a == array_zero).all() == False):
            right_num += 1
        else:
            zero += 1
            zero_collect[root['pointer']] = root["class"]

        # 看是不是为负 为负删除
        left_abscissa = root['bounds'][0]
        left_ordinate = root['bounds'][1]
        right_abscissa = root['bounds'][2]
        right_ordinate = root['bounds'][3]
        if left_abscissa < 0 or right_ordinate < 0 or left_ordinate < 0 or right_abscissa < 0:
            error_num += 1
            error_collect[root['pointer']] = root["class"]
        elif (right_abscissa < left_abscissa or right_ordinate < left_ordinate):
            error_num += 1
            error_collect[root['pointer']] = root["class"]
final_collect={}
def judgeme(root):
    global uncertain_num_collect
    global error_collect
    global zero_collect
    global uncertain_num
    global error_num
    global final_collect
    if root.pointer in uncertain_num_collect or root.pointer in error_collect or root.pointer in zero_collect:
        # print(root.pointer)
        print(uncertain_num_collect)
        print(error_collect)
        print(zero_collect)

    else:
        final_collect[root.component_class] = root.bounds
    for child in root.children:
        if child is None:
            continue
        judgeme(child)

datas = read_data()
root_nodes = []
num = 0
f = open("result.json", 'w', encoding='utf-8')
final_collects = {}
for id in datas:
    print(id)
    root_nodes.append(de_data(datas[id]))
    judgeme(root_nodes[num])
    print(final_collect)
    final_collects[id] = copy.deepcopy(final_collect)
json.dump(final_collects, f, ensure_ascii=False)
