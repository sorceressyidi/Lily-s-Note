## Preknowledge

![10](10.png)

## Euler's method：

  all step size, the accuracy of approximation increases.

![1](1.png)

![2](2.png)

### Error Analysis

Refer to the BOOK

### Other Euler Methods

#### Implicit Euler Method

$y'(t_0)\approx\frac{t(t_0)-y(t_0-h)}{h}\Rightarrow y(t_1)\approx y(t_0)+hy'(t_1)=\alpha+hf(t_1,y(t_1))$

$w_0=\alpha ; w_{i+1}=w_i+hf(t_{i+1},w_{i+1})(i=0,……，n-1)$

$\tau_{i+1}=\frac{y_{i+1}-w_{i+1}}{h}==\frac{h}{2}y''(\epsilon_i)=o(h)$

#### Trapezoidal Method

$w_{i+1}=w_i+\frac{h}{2}[f(t_i,w_i)+f(t_{i+1},w_{i+1})]$

* Error $O(h^2)$ but implict!! so has to be solved iteratively(LOW!)

#### Double-step Method

$y'(t_0)=\frac{1}{2h}[y(t_0+h)-y(t_0-h)]-\frac{h^2}{6}y^{(3)}(\epsilon_1)$

$\Rightarrow y(t_2)\approx y(t_0)+2hf(t_1,y(t_1))$

$w_0=\alpha\\ w_{i+1}=w_{i-1}+2hf(t_i,w_i)$

* Two initial points are required to start moving forward .

#### modified Euler’s method:Trapezoidal Method

Modified Euler's method, also known as the Improved Euler method or Heun's method, is a numerical technique used for approximating solutions to ordinary differential equations (ODEs). It is an extension of the basic Euler's method and provides better accuracy by incorporating a simple correction.

The standard Euler's method is a first-order numerical method that uses a linear approximation to update the solution from one time step to the next. However, it can have limited accuracy, especially for ODEs with rapidly changing behavior.

The Modified Euler's method improves upon this by using a two-step process:

1. **Prediction Step:**

   Use the current information to make a preliminary estimate of the solution at the next time step.

   **Predicted Value** $(P)$:$\tilde{y}_{i+1}=y_{i}+h⋅f(t_i,y_i)$

   Here, $y_i$  is the current approximation, h is the step size, and $f(t_i,y_i)$represents the derivative of y*y* with respect to $t$ at the current point.

2. **Correction Step:**

   Use the predicted value to compute a more accurate estimate by incorporating the derivative at the **predicted point**.

   Corrected Value $(C)$:$y_{i+1}=y_i+\frac{h}{2}[f(t_i,y_i)+f(t_{i+1},\tilde{y}_{i+1})]$

   In this step, $f(t_i,y_i)$represents the derivative at the initial point, and $f(t_{i+1},y_{i+1})$ represents the derivative at the predicted point.

Modified Euler's method has a local truncation error of $O(h^3)$, which is an improvement over the $O(h^2)$ local truncation error of the basic Euler method. This makes it more accurate for a wide range of ODEs, and it is still relatively simple to implement.

## Higher-order Taylor Methods

![11](11.png)

## Runge-Kutta Methods

Runge-Kutta methods are a family of iterative numerical techniques used for solving ordinary differential equations (ODEs) or systems of ODEs. These methods provide an approximation of the solution at discrete points in the domain by iteratively updating the solution from one point to the next.

**Single-Step Method:** 

In a single-step method, the solution at the next time step $(t_{i+1},w_{i+1})$  is determined based on the information available at the current time step  $(t_{i},w_{i})$. This implies that we calculate the next point of the solution through one iteration rather than computing the entire solution curve at once.

We can improve the result by finding a better slope.

**Generalize the modified Euler’s method**

![3](3.png)

![4](4.png)

![5](5.png)

![6](6.png)

## Multistep Methods

Use a linear combination of y and y at several mesh points to better approximate $y(t_{i+1})$

$w_{i+1}=a_{m-1}w_i+a_{m-2}w_{i-1}+……+h[b_mf_{i+1}+b_{m-1}f_i+……+b_0f_{i+1-m}]$

>Newton's Forward Difference Interpolation and Newton's Backward Difference Interpolation are both methods for constructing polynomial interpolants, but they differ in terms of the direction in which they compute the differences.
>
>1. **Newton's Forward Difference Interpolation:**
>   - **Differences:** Forward interpolation starts with the given data point closest to the beginning (usually the lowest x-value) and moves forward.
>   - **Formula:** The forward difference formula is given by: $f[x_0]+f[x_0,x_1](x−x_0)+f[x_0,x_1,x_2](x−x_0)(x−x_1)+…$
>2. **Newton's Backward Difference Interpolation:**
>   - **Differences:** Backward interpolation starts with the given data point closest to the end (usually the highest x-value) and moves backward.
>   - **Formula:** The backward difference formula is given by: $f[x_n]+f[x_n,x_{n−1}](x−x_n)+f[x_n,x_{n−1},x_{n−2}](x−x_n)(x−x_{n−1})+…$
>
>In both cases, the differences $f[x_i,x_{i−1},…,x_0]$ are computed using the divided difference approach. The primary difference between the two methods lies in the direction in which these differences are calculated.
>
>**Key Points:**
>
>- Newton's Forward Difference Interpolation works from the initial data point towards the desired point.
>- Newton's Backward Difference Interpolation works from the final data point towards the desired point.
>- Both methods use divided differences to calculate the coefficients of the interpolation polynomial.
>- The choice between forward and backward interpolation may depend on the specific problem and the nature of the available data.

### Adams-Bashforth explicit m-step technique

 **Derive from integration**

* Adams-Bashforth explicit m-step technique

**1.**Use the Newton backward-difference formula to interpolate f  on $(t_i,f_i),(t_{i-1},f_{i-1})……(t_{i+1-m},f_{i+1-m})$ and obtain $P_{m-1}(t)$ 

**2.**Or Let $t=t_i+sh\ s\in[0,1]$ we have

$\int_{t_{i}}^{t_{i+1}}f(t,y(t))dt=h\int_0^1P_{m-1}(t_i+sh)ds+h\int_0^1R_{m-1(t_i+sh)}ds$

$\Rightarrow w_{i+1}=w_i+h\int_0^1P_{m-1}(t_i+sh)ds$

**3.**  The local truncation error for a multistep method is $\tau_{i+1}(h)=y_{i+1}-(a_{m-1}y_i+……+a_0y_{i+1-m})/h-[b_mf_{i+1}+……+b_0f_{i+1-m}]$ for each $i=m-1,m……,n-1$

**Example**

**derive the Adams-Bashforth two-step explicit method.**

Note ： $h$ is step length $h=\triangle x/n$

![7](7.png)

![8](8.png)

* **Use the** **Newton forward-difference formula to interpolate f** 
* Note: Include$(t_{i+1},f_{i+1})$ to interpolate So it is **implicit**

![9](9.png)

### **Adams predictor-corrector system**

* **Step 1**  Compute the first m initial values by Runge-Kutta method.

* **Step 2** Predict by Adams-Bashforth explicit method.

* **Step 3** Correct by Adams-Moulton implicit method.

#### EXAMPLE

Consider a simple first-order ordinary differential equation given by:

$dy/dt=−y$

We will use the Adams predictor-corrector method to numerically solve this equation.

### Step 1: Compute the First m Initial Values by Runge-Kutta Method

First, we use the Runge-Kutta method to calculate the initial values. For the given equation, the Runge-Kutta scheme is:

$k_1=−y_n$

$k_2=−(y_n+0.5hk_1)$

$y_{n+1}=y_n+hk_2$

Here, $h$ is the time step.

### Step 2: Predict by Adams-Bashforth Explicit Method

The Adams-Bashforth method for a second-order equation is:

$y_{n+1}^{(p)}=y_n+h(−y_n+\frac{3}{2}y_{n−1})$

### Step 3: Correct by Adams-Moulton Implicit Method

The Adams-Moulton method for a second-order equation is:

$$y_{n+1}=y_n+h(−\frac{1}{2}y_{n+1}+\frac{3}{2}y_{n})$$

This equation needs to be solved iteratively as $y_{n+1}$ appears on both sides of the equation.

This is a simple example, and in practice, the Adams predictor-corrector method can be applied to higher-order differential equations. The specific steps and coefficients will vary based on the chosen order. In real-world applications, computational tools or programming languages may be used to perform these calculations.

* All the formulae used in the three steps must have the same order of local truncation error.

   The most popularly used system is based on the 4th-order Adams-Bashforth method as predictor and **one iteration** of the Adams-Moulton method as corrector, with the **starting values** obtained from the **4th-order Runge-Kutta method.**

### **Derive from Taylor expansion**

* derive a formula of order 4 with the form  

![12](12.png)

![13](13.png)

### Higher-Order Equations and Systems of Differential Equations

 ![14](14.png)

  ![15](15.png)

![16](16.png)

### **Stability**

#### Def

* Def one : A one-step difference equation method with local trucation error $\tau_i(h)$ is said to be consistent with the differential equation it approximates if $lim_{h\rightarrow 0}|\tau_i(h)|=0$

  For multistep methods it is also required that for $i=1,2,……m-1$

​	$lim_{h\rightarrow 0}|w_i-y_i|=0$

* A one-step difference equation method is said to be convergent with respect to the differential equation it approximates if $lim_{h\rightarrow 0}max_{1\le i\le n}|w_i-y_i|=0$

* Apply a particular method to a simple test equation,y‘ =λy, y(0) =α, where Re(λ ) < 0.Assume that roundoff error is introduced only at the initial point. If this initial error will decrease for a certain step size h, then this

  method is said to be absolutely stable with respect to **H =λh**. The set of all such H forms the region of absolute stability.

  Method A is said to be more stable than method B if the region of

  absolute stability of A is larger than that of B.

![17](17.png)

![18](18.png)

![20](20.png)

![19](19.png)

#### Def

![21](21.png)

