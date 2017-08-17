import numpy as np

class Perceptron(object):
    def __init__(self, in_num):
        self.activator = lambda x: 1 if x > 0 else 0 
        self.weights = np.random.normal(scale= 1 / in_num**.5, size=in_num)
        self.bias = 0.0
        self.lr = 0.01
        self.epochs = 10

    def predict(self, vector):
        sigma = np.dot(self.weights, vector) + self.bias
        return self.activator(sigma)
    
    def train(self, in_vec, targets):
        for i in range(self.epochs):
            del_w = np.zeros(self.weights.shape)
            del_b = 0
            for (x, y) in zip(in_vec, targets):
                out = self.activator(np.dot(x, self.weights) + self.bias)
                error = y - out
                #del_w += error * x
                #del_b += error
                self.weights += error * x * self.lr
                self.bias += error * self.lr
            #self.weights += del_w * self.lr
            #self.bias += del_b * self.lr

    def __str__(self):
        return "weights is %s,bias is %f" % (self.weights, self.bias)

if __name__ == '__main__':
    and_p = Perceptron(2)
    or_p = Perceptron(2)
    xor_p = Perceptron(2)
    not_p = Perceptron(1)

    input_vecs = np.array([[1,1], [0,0], [1,0], [0,1]])
    and_targets = np.array([1, 0, 0, 0])
    or_targets = np.array([1, 0, 1, 1])
    xor_targets = np.array([0, 1, 1, 0])
    not_v = np.array([0, 1])

    and_p.train(input_vecs, and_targets)
    or_p.train(input_vecs, or_targets)
    xor_p.train(input_vecs, xor_targets)
    not_p.train(not_v, not_v[::-1])
    print('1 and 1 is %d' % and_p.predict(np.array([1, 1])))
    print('0 and 1 is %d' % and_p.predict(np.array([0, 1])))
    print('1 and 0 is %d' % and_p.predict(np.array([1, 0])))
    print('0 and 0 is %d' % and_p.predict(np.array([0, 0])))
    print('1 or 1 is %d' % or_p.predict(np.array([1, 1])))
    print('0 or 1 is %d' % or_p.predict(np.array([0, 1])))
    print('1 or 0 is %d' % or_p.predict(np.array([1, 0])))
    print('0 or 0 is %d' % or_p.predict(np.array([0, 0])))
    print('1 xor 1 is %d, which may be incorrect' % xor_p.predict(np.array([1, 1])))
    print('0 xor 1 is %d, which may be incorrect' % xor_p.predict(np.array([0, 1])))
    print('1 xor 0 is %d, which may be incorrect' % xor_p.predict(np.array([1, 0])))
    print('0 xor 0 is %d, which may be incorrect' % xor_p.predict(np.array([0, 0])))
    print('not 1 is %d' % not_p.predict(np.array([1])))
    print('not 0 is %d' % not_p.predict(np.array([0])))
