#!/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import importlib.util

#import Perceptron class from previous file
spec = importlib.util.spec_from_file_location("perceptron", "../perceptron/perceptron.py")
perceptron = importlib.util.module_from_spec(spec)
spec.loader.exec_module(perceptron)
p = perceptron.Perceptron()

'''
实现一个正向传播
梯度下降的方式为SDG，初始化用numpy库的random.normal取正太分布
假设输入节点为3
隐藏层节点为4
输出节点为1
'''
x = np.array([0.3, 0.5, 0.7])
#初始化输入权重为0 向量为(4,)
weights_0_1 = np.zeros((3, 4))
weights_1_2 = np.random.normal(0, scale=5**(-1), shape=(4,1))

