<font face = 'Times New Roman'>

# Neural Networks

**Problem: Linear Classifiers aren’t that powerful**

![1](1.png)

* Image Features: Color Histogram (Neglect space information)
* Image Features: Histogram of Oriented Gradients (HoG)

![2](2.png)

* Image Features: Bag of Words (Data-Driven!)

![3](3.png)

* To show how much does each visual words appear in the image 

![4](4.png)

## Neural Networks

* 2-layer Neural Network

  $f = W_2 max(0,W_1x)$   $W_2 \in R^{C\times H}$   $W_1 \in R^{H\times D}$   $x\in R^D$​​

  * Fully connected network $(NLP)$

  ![5](5.png)

* 3-layer Neural Network

  $f = W_3 max(0,W_2 max(0,W_1 x))$​ $W_3 \in E^{C\times H_2}$  $W_2 \in R^{H_2\times H_1}$  $x\in R^D$

![6](6.png)

### Activation Functions

![7](7.png)

> Remeber the two-head horse ? (now we can recongnize them !)

![8](8.png)

```python
import numpy as np
from numpy.random import randn
# initialize weights and data
N,Din,H Dout = 64,1000,100,10
x,y = randn(N,Din),randn(N,Dout)
w1,w2 = randn(Din,H),randn(H,Dout)
# compute loss(sigmoid activation)
for t in range(10000):
  h = 1.0/(1.0+np.exp(-x.dot(w1)))
  y_pred = h.dot(w2)
  loss = np.square(y_pred-y).sum()
#Compute gradients
  dy_pred = 2.0 * (y_pred - y)
  dw2 = h.T.dot(dy_pred)
  dh = dy_pred.dot(w2.T)
  dw1 = x.T.dot(dh*h*(1-h))
#SGD step
  w1 -= 1e-4 * dw1
  w2 -= 1e-4 *dw2
```

![1](1.jpg)

### Space Warping

![9](9.png)

![10](10.png)

![11](11.png)

### Universal Approximation

* A neural network with one hidden layer can approximate any function $f: R_N \to R_M$ with arbitrary precision

* Output is a sum of shifted, scaled ReLUs

  ![12](12.png)

* With 4K hidden units we can build a sum of K bumps

* **Reality check: Networks don’t really learn bumps!**

  > Universal approximation tells us: Neural nets can represent any function
  >
  > Universal approximation DOES NOT tell us:
  >
  > * Whether we can actually learn any function with SGD
  >
  > - How much data we need to learn a function
  >
  > Remember: kNN is also a universal approximator!

### Convex Functions

![13](13.png)

## Backpropagation

* Please Refer To PPT

![14](14.png)

* Good porperties for sigmoid

  ![15](15.png)

![16](16.png)

> For the input that is actually the "max" the local gradient is 1
>
> the gradient of the other is 0

* code

  ![17](17.png)

* Backprop Implementation: Modular API

![18](18.png)

![19](19.png)

### Backprop with Vectors

![20](20.png)

* Example one

  ![21](21.png)

### Backprop with Matrices (or Tensors)

![22](22.png)

* Explicitly demonstrate the matrices is demanding! **Work Implicitly!!**

  ![23](23.png)

* Find the correlation

![24](24.png)

$y_{1,1}=x_{1,1}w_{1,1}+x_{1,2}w_{1,2}+x_{1,3}w_{1,3}$

$\frac{dy_{1,1}}{dx_{1,1}}=w_{1,1}$​

* Similarly $\frac{dy_{1,2}}{dx_{1,1}}=w_{1,2}$​  

  $\frac{dy_{2,1}}{dx_{1,1}}=0$​ 

* Thus 

  ![25](25.png)

  $\frac{dL}{dx_{1,1}}=(\frac{dy}{dx_{1,1}})·(\frac{dL}{dy})=(w1,;)·(\frac{dL}{dy_1,;})=3*2 + 2*3 +1*(-3)+(-1)*9$ ​

  ![26](26.png)

  

  

$\frac{dL}{dx_{2,3}}=(\frac{dy}{dx_{2,3}})·(\frac{dL}{dy})=(w3,;)·(\frac{dL}{dy_2,;})=3*(-8)+2*1+1*4+(-2)*6$​

#### Summary

![27](27.png)

![29](29.png)

![30](30.png)

### Higher-Order Derivatives

 ![31](31.png)

![32](32.png)

</font>
