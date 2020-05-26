# Transforming and Projecting Images into Class-conditional Generative Networks

Property: May 26, 2020 10:28 PM
Tags: GAN

A new method of projecting an image into the latent space of class-conditional GAN, based on the combination of classical inverse optimization using ADAM with the gradient-free BasinCMA method.

It allows to achieve better optimization results in such a space, as well as to edit the class for re-generation.

**Transforming and Projecting Images into Class-conditional Generative Networks**

[https://arxiv.org/abs/2005.01703](https://arxiv.org/abs/2005.01703)

[https://github.com/minyoungg/GAN-Transform-and-Project](https://github.com/minyoungg/GAN-Transform-and-Project)

![/images/Transforming%20and%20Projecting%20Images%20into%20Class%20cond%20380093879ee447288ee82897a3b0f6ad/Untitled.png](/images/Transforming%20and%20Projecting%20Images%20into%20Class%20cond%20380093879ee447288ee82897a3b0f6ad/Untitled.png)

The authors investigated ImageNet object statistics in terms of their location in the image (used the pre-trained Mask RCNN to get the bbox), and compared the same statistics for a BigGAN model trained to generate the same 1000 classes.
It turned out that ImageNet data set has a strong bias towards the center, and BigGAN repeats this bias and aggravates it.

There seems to be a bias in the colors of the image as well.

![/images/Transforming%20and%20Projecting%20Images%20into%20Class%20cond%20380093879ee447288ee82897a3b0f6ad/Untitled%201.png](/images/Transforming%20and%20Projecting%20Images%20into%20Class%20cond%20380093879ee447288ee82897a3b0f6ad/Untitled%201.png)

This finding was the reason why the authors added size, position and color transformation to the image back projection process.
In addition, they used the found bbox to mask the foreground from the background (for better optimization), and additionally used the LPIPS loss. And the classic L1.

BigGAN gets to input a **z** vector (from Gauss) and a **c** vector (MLP over a one-hot class vector). For the reverse projection the pre-trained ResNet-151 class is obtained which serves as initialization for the **c** vector.
In the process of the return projection at first there is a search of transformations only, and then the latent code itself is already optimized, alternating methods of CMA and Adam.

After the latent codes are obtained, the authors have already learned the weights of the network itself, placing an additional restriction on the new weights to be as different from the old ones as possible.

Having received vectors z and c, you can edit vector c to change the class.

![/images/Transforming%20and%20Projecting%20Images%20into%20Class%20cond%20380093879ee447288ee82897a3b0f6ad/Untitled%202.png](/images/Transforming%20and%20Projecting%20Images%20into%20Class%20cond%20380093879ee447288ee82897a3b0f6ad/Untitled%202.png)

![/images/Transforming%20and%20Projecting%20Images%20into%20Class%20cond%20380093879ee447288ee82897a3b0f6ad/Untitled%203.png](/images/Transforming%20and%20Projecting%20Images%20into%20Class%20cond%20380093879ee447288ee82897a3b0f6ad/Untitled%203.png)

![/images/Transforming%20and%20Projecting%20Images%20into%20Class%20cond%20380093879ee447288ee82897a3b0f6ad/Untitled%204.png](/images/Transforming%20and%20Projecting%20Images%20into%20Class%20cond%20380093879ee447288ee82897a3b0f6ad/Untitled%204.png)