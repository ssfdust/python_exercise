import tensorflow as tf

save = '/tmp/saver.ckpt'

feed_dict = {'x':4.5, 'y':6.7}
x = tf.Variable(5.6)
y = tf.Variable(5.8)

z = tf.multiply(x, y)
saver = tf.train.Saver()

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    t_x = sess.run(x)
    t_z = sess.run(z)
    print(t_z)
    saver.save(sess, save)
