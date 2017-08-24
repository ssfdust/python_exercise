import tensorflow as tf

hello = tf.constant("Hello Tensorflow!\n")

with tf.Session() as sess:
    print(sess.run(hello).decode('utf-8'))
