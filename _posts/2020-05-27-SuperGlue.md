# SuperGlue: Learning Feature Matching with Graph Neural Networks

A well-performing graph neural network for local matchmaking and homography (alternative to RANSAC). Based on graph mechanism of attention.

**SuperGlue: Learning Feature Matching with Graph Neural Networks**

[https://arxiv.org/abs/1911.11763](https://arxiv.org/abs/1911.11763)

[https://github.com/magicleap/SuperGluePretrainedNetwork](https://github.com/magicleap/SuperGluePretrainedNetwork)
.             | .
:-------------------------:|:-------------------------:
![/images/SuperGlue%20Learning%20Feature%20Matching%20with%20Graph%20Neu%20d87aa56c978145f69d8018a07bc4c311/Untitled.png](/images/SuperGlue%20Learning%20Feature%20Matching%20with%20Graph%20Neu%20d87aa56c978145f69d8018a07bc4c311/Untitled.png)  |  ![/images/SuperGlue%20Learning%20Feature%20Matching%20with%20Graph%20Neu%20d87aa56c978145f69d8018a07bc4c311/Untitled%201.png](/images/SuperGlue%20Learning%20Feature%20Matching%20with%20Graph%20Neu%20d87aa56c978145f69d8018a07bc4c311/Untitled%201.png)



The algorithm accepts local descriptors and their positions as the input, the positions of the keypoints are pre-converted to a higher dimensional space using the Keypoint Encoder - a conventional MLP.
A pair of such local features from two images is received as the input of a graphical network, which sequentially performs self- and intra-attention operations similar to Transfmormer, using query, value and key representations.

For each feature in this way a new view is obtained, from which a score matrix is built (a matrix element is a dot product between vectors of views). Augmentations are added to this matrix to obtain resistance to occlusion and visibility of key points, and then a match between the initial attributes is found using Sinkhorn Algorithm (a differentiated version of Hungarian algorithm).
. | .
:--:|:--:
![/images/SuperGlue%20Learning%20Feature%20Matching%20with%20Graph%20Neu%20d87aa56c978145f69d8018a07bc4c311/Untitled%202.png](/images/SuperGlue%20Learning%20Feature%20Matching%20with%20Graph%20Neu%20d87aa56c978145f69d8018a07bc4c311/Untitled%202.png) | ![/images/SuperGlue%20Learning%20Feature%20Matching%20with%20Graph%20Neu%20d87aa56c978145f69d8018a07bc4c311/Untitled%203.png](/images/SuperGlue%20Learning%20Feature%20Matching%20with%20Graph%20Neu%20d87aa56c978145f69d8018a07bc4c311/Untitled%203.png)

Pipeline has shown very good results compared to classical methods, it is able to produce 15FPS on one GTX1080.
. | .
:--:|:--:
![/images/SuperGlue%20Learning%20Feature%20Matching%20with%20Graph%20Neu%20d87aa56c978145f69d8018a07bc4c311/Untitled%204.png](/images/SuperGlue%20Learning%20Feature%20Matching%20with%20Graph%20Neu%20d87aa56c978145f69d8018a07bc4c311/Untitled%204.png) | ![/images/SuperGlue%20Learning%20Feature%20Matching%20with%20Graph%20Neu%20d87aa56c978145f69d8018a07bc4c311/Untitled%205.png](/images/SuperGlue%20Learning%20Feature%20Matching%20with%20Graph%20Neu%20d87aa56c978145f69d8018a07bc4c311/Untitled%205.png)