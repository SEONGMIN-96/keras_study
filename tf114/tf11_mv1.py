import tensorflow as tf
tf.set_random_seed(66)
        #  1,   2,   3,   4,   5
x1_data = [73., 93., 89., 96., 73.]     # 국어
x2_data = [80., 88., 91., 98., 66.]     # 영어
x3_data = [75., 93., 90., 100., 70.]    # 수힉
y_data = [152., 185., 180., 196., 142.] # 환산점수

# x는 (5, 3), y는 (5, 1) 또는 (5,)

x1 = tf.placeholder(tf.float32)
x2 = tf.placeholder(tf.float32)
x3 = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_normal([1]), name='weight1')
W2 = tf.Variable(tf.random_normal([1]), name='weight2')
W3 = tf.Variable(tf.random_normal([1]), name='weight3')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = x1*W1 + x2*W2 + x3*W3 + b

cost = tf.reduce_mean(tf.square(hypothesis-y)) # mse

# optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.00001)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)

sess = tf.compat.v1.Session()
sess.run(tf.global_variables_initializer())

for epochs in range(40001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train], 
    feed_dict={x1:x1_data, x2:x2_data, x3:x3_data, y:y_data}        
)
    if epochs % 10 == 0:
        print(epochs, "cost :", cost_val, "\n", hy_val)

sess.close()