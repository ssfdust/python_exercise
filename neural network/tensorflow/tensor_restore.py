import tensorflow as tf

save = '/tmp/saver.ckpt'

x = tf.Variable(9.7)
y = tf.Variable(8.9)
z = tf.multiply(x, y)

saver = tf.train.Saver()
with tf.Session() as sess:
    saver.restore(sess, save)
    print(sess.run(z))
