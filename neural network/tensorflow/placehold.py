import tensorflow as tf

x = tf.placeholder(tf.int64)
y = tf.placeholder(tf.string)
z = tf.placeholder(tf.double)
a = tf.constant(15)
b = tf.constant(16)

feed_dict = {
    x: 34343523523452523,
    y: "爱是一道光",
    z: 234.43242523523423424
}

with tf.Session() as sess:
    out_y = sess.run([x, y], feed_dict=feed_dict)
    print("{} {}".format(out_y[0], out_y[1]))
