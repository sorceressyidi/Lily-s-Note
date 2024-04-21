# Video Understanding

## Late Fusion Approach
* Fusing the features from different modalities at the end of the network.
> FC layers may result in overfitting

![7](7.png)
![1](1.png)
![2](2.png)

## Early Fusion Approach
* Stakcing through channel dimension.
* Fuse the features Using 2D convolutions.($3T\times D$ )

![3](3.png)
* One layer of temporal processing may not be enough!
![4](4.png)

## **Comparison**
### General Comparison
![5](5.png)
![6](6.png)

### 2D Conv (Early Fusion) vs 3D Conv (3D CNN)
> Details see Slides.
* 2D : perceptive of features of time at once and slide over the space feature. No temporal shift-invariance! Needs to learn separate filters for the same motion at different times in the clip.

* 3D : Temporal shift-invariant since each filter slides **over time !**

### C3D : The VGG of 3D CNNs
![8](8.png)

### Measuring Motion : Optical Flow
#### Two Stream Networks
![9](9.png)
#### Modeling long-term temporal structure
![10](10.png)
* Sometimes don’t backprop to CNN to save memory; pretrain and use it as a feature extractor : Like using pretrained C3D as a feature extractor.
#### Recurrent Convolutional Network
![11](11.png)
![12](12.png)
> Actually not too much used because of the time complexity.(Not good for parallelization) 
>**Sequential processing is not good for parallelization.**

#### Spatio-Temporal Self-Attention (Non Local Block)

![13](13.png)

> Trick:Add non-local blocks to 3D CNNs , initilize the weights of the non-local block with all zeros, and fine-tune the network. 
> ![14](14.png)

#### Inflating 2D Networks to 3D (I3D)
> Refer to the slides for details.
> Trick: Pretrain 2D CNNs and inflate them to 3D CNNs by repeating the weights along the temporal dimension.

![15](15.png)

