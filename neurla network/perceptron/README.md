### 与运算感知器实现

#### 感知器原理
y = f(∑(x<sub>i</sub> * w<sub>i</sub>) + b)

t = f(h)为阶跃函数

通过梯度下降来实现一个与运算感知器

详见：https://www.zybuluo.com/hanbingtao/note/433855

#### 运行结果
```
$ python perceptron.py
1 and 1 is 1
0 and 1 is 0
1 and 0 is 0
0 and 0 is 0
1 or 1 is 1
0 or 1 is 1
1 or 0 is 1
0 or 0 is 0
not 1 is 0
not 0 is 1
```

#### 线性神经元的问题

##### 有关SGD与BGD算法的问题

* SDG算法实现
    ```Python
    for i in range(self.epochs):
        for (x, y) in zip(in_vec, targets):
            out = self.activator(np.dot(x, self.weights) + self.bias)
            error = y - out
            self.weights += error * x * self.lr
            self.bias += error * self.lr
    ```

* BGD算法实现
    ```Python
    for i in range(self.epochs):
        del_w = np.zeros(self.weights.shape)
        del_b = 0
        for (x, y) in zip(in_vec, targets):
            out = self.activator(np.dot(x, self.weights) + self.bias)
            error = y - out
            del_w += error * x
            del_b += error
        self.weights += del_w * self.lr
        self.bias += del_b * self.lr
    ```
* SDG与BDG算法实现注意点
    - 一个是超参数的设定，SDG的超参数的迭代次数较少，学习率稍大。而BDG的超参数的迭代次数很大，学习率较小。
    - 第二个是SDG的权重是实时更新的，而BDG是遍历完一个样本更新一次。

    - 详见：https://www.zybuluo.com/hanbingtao/note/448086

##### 输出结果以及超参数：
* SDG:
    ```
    #学习效率为0.01, 迭代次数为10
    weights is [ 1124.06018833],bias is 85.519169
    Work 3.4 years, monthly salary = 3907.32
    Work 15 years, monthly salary = 16946.42
    Work 1.5 years, monthly salary = 1771.61
    Work 6.3 years, monthly salary = 7167.10
    ```
* BDG:
    ```
    #学习效率为0.001, 迭代次数为1500
    weights is [ 1094.60980977],bias is -298.885425
    Work 3.4 years, monthly salary = 3422.79
    Work 15 years, monthly salary = 16120.26
    Work 1.5 years, monthly salary = 1343.03
    Work 6.3 years, monthly salary = 6597.16
    ```
* 总结
    二者最终都呈现了线性关系，只是二者差距有点大。
