# Hierarchical Multi-Scale Attention for Semantic Segmentation

New SOTA on Cityscapes and Mapillary Vistas on semantic segmentation from NVIDIA, based on a new mechanism for mixing multi-scale predictions through attention, as well as on the auto labeling of poorly marked parts of the dataset.

**Hierarchical Multi-Scale Attention for Semantic Segmentation**

[https://arxiv.org/abs/2005.10821](https://arxiv.org/abs/2005.10821)

The authors draw attention to the fact that the neural net predictions on a different scale have different quality labels in different details. They call it a class confusion. Although the standard logit averaging scheme works in general, it is obviously not ideal because both good and bad predictions are mixed up.

![image.png](/images/Hierarchical_attention/image.png)

It is a good idea to learn the attention map for each scale, so that the equilibrated sum (average) becomes weighted with the learned coefficients.

Naive addition of several attention maps increases the model size and learning time, so the authors suggested another approach - during learning the model predicts the attention map for only two adjacent scales, the general map is obtained as M and (1 - M) for two scales. During training always two scales are used - 1.0 and 0.5, and the input image is also presented at different scales, so that the network is robust to all scales.

The authors called this approach Hierarchical multi-scale attention, it increases the model only by 1.25 times and not so much affects the learning rate.

During the inference, you can combine as many scales as you want, consistently feeding the model images of increasing size, combining them by the predicted mask.

![image.png](/images/Hierarchical_attention/image%201.png)

![image.png](/images/Hierarchical_attention/image%202.png)

In addition, the authors used auto-labeling, labeling a part of Cituscapes with coarse labels. They used hard labels because soft labels take up too much disk space and the training pipelining slow down on IO operations.

![image.png](/images/Hierarchical_attention/image%203.png)

In the experiments we used ResNet50 and HRNet-OCR encoders (SOTA results were obtained on it), and the decoder was taken from DeepLabV3+.

The training was carried out on 2-4 DGX nodes (8xV100), 1 image per GPU at a resolution of 1024 pixels on the smaller side.

![image.png](/images/Hierarchical_attention/image%204.png)

![image.png](/images/Hierarchical_attention/image%205.png)

![image.png](/images/Hierarchical_attention/image%206.png)