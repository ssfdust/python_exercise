from perceptron import Perceptron
import numpy as np

class LinearRegulation(Perceptron):
    def __init__(self, in_num):
        super().__init__(in_num)
        self.activator = lambda x: x
        
if __name__ == '__main__':
    line_o = LinearRegulation(1)
    input_vec = np.array([[5], [3], [8], [1.4], [10.1]])
    labels = [5500, 2300, 7600, 1800, 11400]
    line_o.train(input_vec, labels)
    print(line_o)
    print('Work 3.4 years, monthly salary = %.2f' % line_o.predict(np.array([3.4])))
    print('Work 15 years, monthly salary = %.2f' % line_o.predict(np.array([15])))
    print('Work 1.5 years, monthly salary = %.2f' % line_o.predict(np.array([1.5])))
    print('Work 6.3 years, monthly salary = %.2f' % line_o.predict(np.array([6.3])))

