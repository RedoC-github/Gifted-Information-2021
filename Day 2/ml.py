# ML
import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# hyperparameter
learning_rate = 0.01
epochs = 100

def LogRegression(datax, datay):
    X = tf.placeholder(tf.float32)
    Y = tf.placeholder(tf.float32)

    def model(w_, x_, b_):
        return tf.add(tf.multiply(tf.log(x_), w_), b_)
    
    w = tf.Variable(0.0, name="Weight")
    b = tf.Variable(0.0, name="Bias")
    model_y = model(w, X, b)

    cost = (tf.pow(Y-model_y, 2))
    train = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
    
    # session
    sess = tf.Session()
    init = tf.global_variables_initializer()
    sess.run(init)

    for epoch in range(epochs):
        for (x, y) in zip(datax, datay):
            sess.run(train, feed_dict={X: x, Y: y})
    
    w_val = sess.run(w)
    b_val = sess.run(b)
    sess.close()
    return w_val, b_val