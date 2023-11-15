# Neural Networks and Deep Learning

## Convolutional Neural Network(CNN)

https://leovan.me/cn/2018/08/cnn/

## Recurrent Neural Network （RNN）

![v2-b0175ebd3419f9a11a3d0d8b00e28675_1440w](https://pic2.zhimg.com/80/v2-b0175ebd3419f9a11a3d0d8b00e28675_1440w.webp)

$O_t=g(V\cdot S_t)$

$S_t=\Phi(U\cdot X_t+W\cdot S_{t-1})$ $\Phi$（激活函数）

![v2-9e50e23bd3dff0d91b0198d0e6b6429a_1440w](https://pic3.zhimg.com/80/v2-9e50e23bd3dff0d91b0198d0e6b6429a_1440w.webp)

### Back propagation

#### Intro

$Cost=H(W_{11},W_{12},……,W_{mn})$

$\triangledown H=\frac{\partial H}{\partial W_{11}}e_{11}+\frac{\partial H}{\partial W_{12}}e_{12}+……+\frac{\partial H}{\partial W_{mn}}e_{mn}$

https://zhuanlan.zhihu.com/p/115571464

https://towardsdatascience.com/understanding-backpropagation-algorithm-7bb3aa2f95fd

反向传播（Backpropagation）是一种用于训练神经网络的优化算法，通过计算损失函数关于网络参数的梯度，并利用这些梯度来更新参数，以最小化损失函数。

1. **前向传播（Forward Propagation）：** 将输入数据通过神经网络进行正向传播，计算每一层的输出。
2. **计算损失（Compute Loss）：** 使用网络的输出和真实标签计算损失函数，衡量网络的性能好坏。
3. **反向传播梯度（Backward Pass）：** 从输出层开始，计算损失函数关于每个参数的梯度。这是通过使用链式法则来计算的，将梯度从输出层向输入层传播。
4. **参数更新（Update Parameters）：** 使用梯度下降或其他优化算法，通过将梯度乘以一个学习率，来更新网络参数。学习率控制了每次参数更新的步长，以避免跳过最优解。
5. **重复迭代（Repeat）：** 重复以上步骤，直到损失函数收敛到满意的程度或达到预定的训练次数。

#### 梯度的计算

计算损失函数对网络输出的梯度（即损失函数关于输出的导数）。

- 使用链式法则，将梯度从输出层传播到输入层，计算每一层的梯度。
- 根据梯度和选择的优化算法，更新每个参数。

这个过程是通过反向传播和梯度下降算法的结合来实现的，以最小化损失函数并优化神经网络的参数。

#### 参数更新

$θ_{new}=θ_{old}−α∇L(θ_{old})$

其中：

- $θ_{old}$ 是当前的参数值。
- $∇L(θ_{old}$是损失函数相对于参数的梯度。
- $α$ 是学习率，是一个小正数。

这个更新规则的直观解释是，我们沿着损失函数下降最快的方向更新参数。梯度告诉我们损失函数在当前点上升最快的方向，我们沿着梯度的反方向前进，以降低损失。

学习率的选择是关键的。如果学习率太小，收敛速度会很慢，而如果学习率太大，我们可能会跳过损失函数的最小值。因此，选择一个合适的学习率对于训练神经网络至关重要。

通常，在训练过程中，学习率可能会随着时间的推移而变化，这被称为学习率调度（learning rate scheduling）。例如，初始时可以使用较大的学习率以快速收敛，然后随着训练的进行逐渐减小学习率，以提高收敛的精度。

总的来说，学习率是一个平衡训练速度和性能的关键因素。不同的问题可能需要不同的学习率，因此它通常需要通过实验来调整。

#### Back propagation in CNN

https://mmuratarat.github.io/2019-02-07/bptt-of-rnn

#### Long Short-Term Memory

https://easyai.tech/ai-definition/rnn/

https://blog.csdn.net/u012328159/article/details/87567358

### Attention

https://www.cnblogs.com/gczr/p/14693829.html

https://zhuanlan.zhihu.com/p/379722366

![v2-740c1ab6d6600c003ca092a8e8a5668b_1440w](https://pic4.zhimg.com/80/v2-740c1ab6d6600c003ca092a8e8a5668b_1440w.webp)

