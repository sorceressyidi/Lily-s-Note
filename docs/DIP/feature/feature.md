## Feature detection

### Feature detection:  the math

Consider shifting the window $W$ by $(u,v)$

$\begin{align*}Error(u,v)&=\sum_{(x,y)\in W}[I(x+u,y+v)-I(x,y)]^2\\ &\approx\sum_{(x,y)\in W}[I(x,y)+\frac{\partial I}{\partial x}u+\frac{\partial I}{\partial y}v-I(x,y)]^2\\ &\approx\sum_{(x,y)\in W}[u,v]\begin{bmatrix}I_x^2&I_xI_y\\I_yI_x&I_y^2\end{bmatrix}\begin{bmatrix}u\\v\end{bmatrix} \\ \end{align*}$

* Which directions will result in the largest and smallest E values?

  We can find these directions by looking at the eigenvectors of H $(\begin{bmatrix}I_x^2&I_xI_y\\I_yI_x&I_y^2\end{bmatrix})$

Eigenvalues and eigenvectors of H

![5](5.png)

* Define shifts with the smallest and largest change (E value)
* $x_+$ = direction of largest increase in E. 
* $\lambda_+$ = amount of increase in direction x+       $Hx_{+}=\lambda_{x_+}x_+$
* $x_-$ = direction of smallest increase in E. 
* $\lambda_-$ = amount of increase in direction x- .      $Hx_{-}=\lambda_{x_-}x_-$

Since $H$ is symmetric ,so $H=R^{-1}\begin{bmatrix}\lambda_1&0\\0&\lambda_2\end{bmatrix}R$

![3](3.png)

![4](4.png)

* Compute the gradient at each point in the image
* Create the $H$ matrix from the entries in the gradient
* Compute the eigenvalues. 
* Find points with large response ($\lambda_-$ > threshold)
* Choose those points where $\lambda_-$ is a local maximum as features

### The Harris operator

- $\lambda_-$  is a variant of the “Harris operator” for feature detection

$f=\frac{\lambda_1\lambda_2}{\lambda_1+\lambda_2}$

* The trace is the sum of the diagonals, i.e., $trace(H) = h_{11} + h_{22}$
* Very similar to $\lambda_-$ but less expensive (no square root)
* Called the “Harris Corner Detector” or “Harris Operator”Lots of other detectors, this is one of the most popular

### Some Properties

* Rotation Invariance

* Invariance to image intensity change

* Not invariance to scaling

### Scale Invariant Detection

![a](a.png)

* Eg. Take a local $MAXIMUM$

![b](b.png)

#### Harris-Laplacian

We define the characteristic scale as the scale that produces peak of Laplacian response

**Stage 1: Multiscale Harris Corner Detection**

1. **Image Pyramid Construction:** Begin by constructing a scale-space pyramid of the image, generating different scales by applying Gaussian smoothing and downsampling.
2. **Computation of Harris Corner Response:** At each scale, calculate the corner response using the Harris corner detection method. This typically involves computing local gradients at each pixel position, forming the autocorrelation matrix, calculating the corner response function, and identifying local maxima as keypoints.
3. **Non-Maximum Suppression:** For each scale, perform non-maximum suppression to eliminate redundant keypoints in the corner response function, retaining only the keypoints corresponding to local maxima.

**Stage 2: Scale Selection Based on Laplacian**

1. **Laplacian Scale Selection:** 

   The Laplacian is an operator used to detect edges and texture variations in an image by computing the second derivative at each point. In the context of scale selection, the Laplacian serves to measure the changes in the image at different scales.

   Example: Consider an image containing a circle. As you view this circle at different scales, its edges will exhibit varying degrees of change. By applying the Laplacian at different scales, we can observe the intensity of edge variations. 

   The optimal scale for a keypoint is where the maximum edge response occurs, indicating that the details of the keypoint are most pronounced at that scale.

2. **Keypoint Filtering:** 

   For the same corner, even with changes in scale, the corner remains detectable, indicating robustness in terms of repeatability.

   The content within the feature scale range of the same corner in images of different sizes should be consistent. 

   Therefore, the pixel locations within the feature scale range of corners in images of varying scales are proportional to the scale.(不同尺寸图片中的相同角点的特征尺度范围中的内容要相同，因此，不同尺度的图片的角点的特征尺度范围内的像素点与尺度成比例关系。)

##### Local Extrema Detection

* Maxima and minima
* Compare x with its 26 neighbors at 3 scales 



#### SIFT

