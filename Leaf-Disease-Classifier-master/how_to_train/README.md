# How to Train 

This section covers on how to train the <b>LeafNet</b> network. Again, this section is further divided into 2 parts:

- YOLOv3  (Darknet)
- Deep Residual network (Resnet 50)

*<i><b>Note:</b></i> You might need a mass-file rename script file (rename.py) for training and annotating the train images for YOLOv3 (if you need).


## YOLOv3 (DarkNet 53) :

- YOLO - You look Only Once Version3 -  is used as the leaf detector for the LeafNet classifier. It is based on YOLOv3 Darknet53 pre-trained weights and makes use of transfer learning wherein the model, before, was trained on a very large dataset. 

- To train, I used the following tutorials and resources,

    - https://medium.com/@manivannan_data/how-to-train-yolov3-to-detect-custom-objects-ccbcafeb13d2 : This tutorial starts off by intoducing YOLOv3 darknet and how to train (with details and helpful commands).

    - https://medium.com/@manivannan_data/how-to-train-yolov2-to-detect-custom-objects-9010df784f36  : <b>USE</b> this tutorial <b>ONLY FOR</b> image/ data annotation, beacuse, this tutorial consists of training the model in YOLOv2.

    - https://github.com/ManivannanMurugavel/YOLO-Annotation-Tool : Make use of this annotation tool for annotation of images. 

    - https://github.com/deepakHonakeri05/darknet.git : (Forked from AlexeyAB --> pjreddy's github repository) In case if you are UNABLE to find YOLOv3 Darknet


<b>Important Note :</b> 
If you need the config files for this YOLOv3 Darknet : <b>check [config file location]</b> 
-   cfg/ leaf.cfg 
-   cfg/ leaf.data
-   cfg/ leaf.names 

[config file location] : https://github.com/deepakHonakeri05/darknet/tree/master/cfg


## Deep Residual network (Resnet 50) : 

- This part of training, is relatively simple but can be tedious task which requires training the model for 8 different classifiers. The training involves taking a pretrained Resnet network trained on imagenet dataset. This too, involves transfer learning. 

- "<b>Res50_script.ipynb</b>" Includes the model architecture and the template used in training the model. In order to train, the 8 different classifiers please use this same script and vary the number of classes and epochs as you desire.

- However, in the script of the training for Resnet model, the code is very easy to understand and it is self-explanatory. Hence, I will not be covering the architecture here.
