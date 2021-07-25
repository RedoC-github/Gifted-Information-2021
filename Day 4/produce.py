primes = []

n = 10
arr = [1]*(n+1)
arr[0] = 0
arr[1] = 0

for i in range(2, n+1, 1):
	if arr[i]:
		primes.append(i);
		for j in range(2*i, n+1, i):
			arr[j] = 0

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

plt.title("Prime Distribution")
plt.scatter(np.arange(0, len(primes)/2, 0.5), primes)
plt.ylabel("n-th prime")
plt.xlabel("n")

# regression

learning_rate = 0.000001
epoch = 40

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

deg = 2
def model(X_, w):
	polynoms = []
	for i in range(deg):
		polynom = tf.multiply(w[i], tf.pow(X_, i))
		polynoms.append(polynom)
	return tf.add_n(polynoms)

w = tf.Variable([0.]*deg, name="parameters")
y_model = model(X, w)

cost = (tf.pow(Y-y_model, 2))
train_op = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

with tf.Session() as sess:
	init = tf.global_variables_initializer()
	sess.run(init)

	for epc in range(epoch):
		for (x, y) in zip(np.arange(0, len(primes)/2, 0.5), primes):
			sess.run(train_op, feed_dict={X: x, Y: y})
	
	w_val = sess.run(w)
	print(w_val)

poly_X = np.arange(0, len(primes)/2, 0.5)
poly_Y = []
for x_ in poly_X:
	poly_y = 0
	for i in range(deg):
		poly_y += w_val[i] * pow(x_, i)
	poly_Y.append(poly_y)

plt.plot(poly_X, poly_Y, "r")
plt.show()
