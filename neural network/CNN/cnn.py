#!/bin/python
# -*- coding: utf-8 -*-

import tensorflow as tf

# 使用Tensorflow实现CNN,利用tf.nn.conv2d()以及tf.nn.bias_add()函数创建卷基层

k_output = 64 #输出层的深度

# 图片属性
image_width = 10
image_height = 10
color_channels = 3

# 卷积滤波器
filter_size_width = 5
filter_size_height = 5

# 输入/图像
image_input = tf.placeholder(
    tf.float32,
    shape = [None, image_height, image_width, color_channels]
)

# 权重以及偏置
weight = tf.Variable(tf.truncated_normal(
    [filter_size_height, filter_size_width, color_channels, k_output])
)
bias = tf.Variable(tf.zeros(k_output))

conv_layer = tf.nn.conv2d(image_input, weight, strides=[1, 2, 2, 1], padding='SAME')
conv_layer = tf.nn.bias_add(conv_layer, bias)
conv_layer = tf.nn.relu(conv_layer)

# 应用最大池化
conv_layer = tf.nn.max_pool(
    conv_layer,
    ksize=[1, 2, 2, 1],
    strides=[1, 2, 2, 1],
    padding='SAME'
)

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    sess.run(conv_layer)
    print(sess.run(bias))
