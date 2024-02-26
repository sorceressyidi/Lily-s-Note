## Preliminaries

* Refer to Slides

**Idea of self-supervision:**

* Obtain labels from raw unlabeled data itself 
* Predict parts of the data from other parts

## Task-specific Models

### Unsupervised Learning of Depth and Ego-Motion

![1](1.png)

####  Depth Estimation Network

> Specifically, at training time, we have access to two images $I^l$ and $I^r$ , corresponding to the left and right color images from a calibrated stereo pair, captured at the same moment in time. 
>
> Instead of trying to directly predict the depth, we attempt to find the **dense correspondence field** $d_r$ that, when applied to the left image, would enable us to reconstruct the right image. We will refer to the reconstructed image $I^l(d_r)$ as $\tilde{I}^r$​. Similarly, we can also estimate the left image given the right one, $\tilde{I}^l =I^r(d_l)$.
>
>  Assuming that the images are rectified , $d$ corresponds to the image disparity - a scalar value per pixel that our model will learn to predict. Given the baseline distance $b$ between the cameras and the camera focal length $f$, we can then trivially recover the depth $\hat{d}$ from the predicted disparity, $\hat{d}=bf/d$​​​.

**Simultaneously** infer both disparities (left-to-right and right-to-left), using only the left input image, and obtain better depths by enforcing them to be consistent with each other.

* Naively learning to generate the right image by sampling from the left

![2](2.png)

#### Digging Into Self-Supervised Monocular Depth Estimation

![3](3.png)

### Unsupervised Learning of Optical Flow



## Pretext Tasks

## Contrastive Learning

