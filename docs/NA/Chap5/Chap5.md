## Euler's method：

The Euler’s method is a first-order numerical procedure for solving ordinary differential equations (ODE) with a given initial value.

In Euler’s method, you can approximate the curve of the solution by the tangent in each interval (that is, by a sequence of short line segments), at steps of `h`.

*In general*, if you use small step size, the accuracy of approximation increases.

![1](1.png)

![2](2.png)

### modified Euler’s method:

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

