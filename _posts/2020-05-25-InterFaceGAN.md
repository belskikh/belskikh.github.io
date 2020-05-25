# InterFaceGAN: Interpreting the Disentangled Face Representation Learned by GANs

Article with the deep analysis of latent spaces of representations of the persons learnt by generative models.
Authors have shown very good way of reception of the disentangled directions in latent space, and also have shown some ways of modification of real faces on found latent attributes.

**InterFaceGAN: Interpreting the Disentangled Face Representation Learned by GANs**

[https://arxiv.org/abs/2005.09635](https://arxiv.org/abs/2005.09635)

[https://genforce.github.io/interfacegan/](https://genforce.github.io/interfacegan/)

[https://github.com/genforce/interfacegan](https://github.com/genforce/interfacegan)

![image.png](/images/InterFaceGAN%20Interpreting%20the%20Disentangled%20Face%20Re%20f0280188c12a4cb9a0a73bdc08049f66/image.png)

As we have already noticed before, if you take two different vectors z to generate an image by a face generator like StyleGAN or PGGAN, make a linear interpolation between them and generate images for samples from this range, you will see how smoothly one object of generation is transformed into another.
Thus, linear interpolation between two vectors in latent space forms the direction that the hyperplane forms.

The authors assume that for binary semantics there is such a hyperplane, which serves as a divider of latent space. On one side of this hyperplane lie objects of one class, and on the other - another (eg, a female-male, young-old, etc.).

Moving in the direction normal to this hyperplane, you can change the degree of the attribute. But there are many such hyperplanes for different attributes, and they are not orthogonal. Because of this there is an effect of confusion, when the naive movement in the direction of the normal to one attribute will lead to changes in the another.

The authors propose a method to obtain such a direction on the target attribute, so that movement along it does not lead to changes in the other attributes. They called it **conditional manipulation via subspace projection.**

![image.png](/images/InterFaceGAN%20Interpreting%20the%20Disentangled%20Face%20Re%20f0280188c12a4cb9a0a73bdc08049f66/image%201.png)

To analyze their work, the authors identified five key facial attributes: pose, smile, age, gender and eyeglasses. They then generated 500k images and labeled them with pre-trained classifiers for these attributes. For each attribute they chose 10k images with the highest scores and 10k with the lowest scores. On corresponding images of latent vectors they have trained SVM (70% training / 30% validation), having received thus dividing hyperplanes for these five attributes.
It was found that in latent space such attributes are very well separated not only on the selected subsets of data, but also on all 500k images.

![/images/InterFaceGAN%20Interpreting%20the%20Disentangled%20Face%20Re%20f0280188c12a4cb9a0a73bdc08049f66/Untitled.png](/images/InterFaceGAN%20Interpreting%20the%20Disentangled%20Face%20Re%20f0280188c12a4cb9a0a73bdc08049f66/Untitled.png)

An interesting finding was that objects generated from samples lying extremely far away from the dividing border look very unrealistic, but at the same time reflect the extremity of the selected attribute.

![image.png](/images/InterFaceGAN%20Interpreting%20the%20Disentangled%20Face%20Re%20f0280188c12a4cb9a0a73bdc08049f66/image%202.png)

The authors analyzed the entanglement of attributes by comparing the correlation of these attributes, predicted by the classifiers on the generated images, as well as comparing cosine distance of separating hyperplanes.
It turned out that some are very tangled, and some almost not.

However, the authors' method allows changing the direction even for entangled features without changing the others.

![/images/InterFaceGAN%20Interpreting%20the%20Disentangled%20Face%20Re%20f0280188c12a4cb9a0a73bdc08049f66/Untitled%201.png](/images/InterFaceGAN%20Interpreting%20the%20Disentangled%20Face%20Re%20f0280188c12a4cb9a0a73bdc08049f66/Untitled%201.png)

![/images/InterFaceGAN%20Interpreting%20the%20Disentangled%20Face%20Re%20f0280188c12a4cb9a0a73bdc08049f66/Untitled%202.png](/images/InterFaceGAN%20Interpreting%20the%20Disentangled%20Face%20Re%20f0280188c12a4cb9a0a73bdc08049f66/Untitled%202.png)

![/images/InterFaceGAN%20Interpreting%20the%20Disentangled%20Face%20Re%20f0280188c12a4cb9a0a73bdc08049f66/Untitled%203.png](/images/InterFaceGAN%20Interpreting%20the%20Disentangled%20Face%20Re%20f0280188c12a4cb9a0a73bdc08049f66/Untitled%203.png)

![/images/InterFaceGAN%20Interpreting%20the%20Disentangled%20Face%20Re%20f0280188c12a4cb9a0a73bdc08049f66/Untitled%204.png](/images/InterFaceGAN%20Interpreting%20the%20Disentangled%20Face%20Re%20f0280188c12a4cb9a0a73bdc08049f66/Untitled%204.png)

![/images/InterFaceGAN%20Interpreting%20the%20Disentangled%20Face%20Re%20f0280188c12a4cb9a0a73bdc08049f66/Untitled%205.png](/images/InterFaceGAN%20Interpreting%20the%20Disentangled%20Face%20Re%20f0280188c12a4cb9a0a73bdc08049f66/Untitled%205.png)

The possibility of editing images of real faces in two ways was also studied separately: 1) by projection of the image in a latent space and change of a latent vector in a necessary direction, 2) by generation of a synthetic dataset and training of separate pix2pixHD models for each attribute.
The second way has shown itself best of all.

![/images/InterFaceGAN%20Interpreting%20the%20Disentangled%20Face%20Re%20f0280188c12a4cb9a0a73bdc08049f66/Untitled%206.png](/images/InterFaceGAN%20Interpreting%20the%20Disentangled%20Face%20Re%20f0280188c12a4cb9a0a73bdc08049f66/Untitled%206.png)

![/images/InterFaceGAN%20Interpreting%20the%20Disentangled%20Face%20Re%20f0280188c12a4cb9a0a73bdc08049f66/Untitled%207.png](/images/InterFaceGAN%20Interpreting%20the%20Disentangled%20Face%20Re%20f0280188c12a4cb9a0a73bdc08049f66/Untitled%207.png)