import tensorflow as tf
node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0) # 默认数据类型为tf.float32
# 上面的代码是之前的
# 下面的代码是新加的
sess = tf.Session()
print(sess.run(node1))
print(sess.run(node2))