import tensorflow as tf
X = tf.placeholder(tf.float32, [None, 5])
ep_ = tf.placeholder(tf.float32, [None, 1])
theta = tf.Variable(tf.zeros([5, 1]))
ep = tf,matmul(X,theta)