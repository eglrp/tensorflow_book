import tensorflow as tf
x = tf.placeholder(tf.float32, [None, 5])
ep_ = tf.placeholder(tf.float32, [None, 1])
theta = tf.Variable(tf.ones([5, 1]))
ep = tf.matmul(x,theta)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
print(sess.run(ep,feed_dict={x:[[1,2,3,4,5]]}))