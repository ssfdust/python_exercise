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
