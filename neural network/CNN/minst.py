from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets(".", fake_data=False, one_hot=True, dtype=dtypes.float32, reshape=False, validation_size=5000, seed=None)

import tensorflow as tf

# 参数
learning_rate = 0.00001
epochs = 10
batch_size = 128

test_valid_size = 256

# 神经网络参数
n_classes = 10
dropout = 0.75

# 保存层权重以及偏置
weights = {
    'wc1': tf.Variable(tf.random_normal([5, 5, 1, 32], mean=0.0, stddev=1.0, dtype=dtypes.float32, seed=None, name=None)),
    'wc2': tf.Variable(tf.random_normal([5, 5, 32, 64])),
    'wd1': tf.Variable(tf.random_normal([7 * 7 * 64, 1024])),
    'out': tf.Variable(tf.random_normal([1024, n_classes]))
}

biases = {
    'bc1': tf.Variable(tf.random_normal([32])),
    'bc2': tf.Variable(tf.random_normal([64])),
    'bd1': tf.Variable(tf.random_normal([1024])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}

# 卷积
def conv2d(image_input, weights, bias, strides=1):
    conv_layer = tf.nn.conv2d(image_input, weights, strides=[1, strides, strides, 1], padding='SAME')
    conv_layer = tf.nn.bias_add(conv_layer, bias)
    conv_layer = tf.nn.relu(conv_layer)
    
    return conv_layer


def maxpool2d(x, k=2):
    return tf.nn.max_pool(
        x,
        ksize=[1, k, k, 1],
        strides=[1, k, k, 1],
        padding='SAME'
    )


