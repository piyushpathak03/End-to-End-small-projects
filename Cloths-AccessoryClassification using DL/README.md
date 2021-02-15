# Cloths-AccessoryClassification
This project is built for classifying total 10 different type of cloths and accessories with VGG Image Classification Model.


<img src="https://github.com/manthanpatel98/Cloths-AccessoryClassification/blob/main/Readme_Images/cloth-classification.gif" width=750>

---

## About Model:
* The model is trained for classes: **'Goggles'**, **'Hat'**, **'Jacket'**, **'Shirt'**, **'Shoes'**, **'Shorts'**, **'T-Shirt'**, **'Trouser'**, **'Wallet'**,**'Watch'**.
* Each class had around 30-50 images during training.
* Images are trained with **VGG** Image Classification Model.

<img src="https://github.com/manthanpatel98/Cloths-AccessoryClassification/blob/main/Readme_Images/Fashion-Model.png">

---

## Understanding VGG:

<img src="https://github.com/manthanpatel98/Cloths-AccessoryClassification/blob/main/Readme_Images/vgg16-neural-network.jpg" width=750>

* The full name of **VGG** is the **"Visual Geometry Group"**, which belongs to the Department of Science and Engineering of **Oxford University**.

* In **[ILSVRC'14](http://www.image-net.org/challenges/LSVRC/#:~:text=The%20ImageNet%20Large%20Scale%20Visual,image%20classification%20at%20large%20scale.&text=Another%20motivation%20is%20to%20measure,indexing%20for%20retrieval%20and%20annotation.)**, VGG was **2nd in Image Classification** and **1st in Localization**.

* The original purpose of VGG's research on the depth of convolutional networks is to understand how the depth of convolutional networks affects the accuracy and large-scale image classification and recognition.

<img src="https://github.com/manthanpatel98/Cloths-AccessoryClassification/blob/main/Readme_Images/VGG-models.png" height=600>

* In order to deepen the number of network layers and to avoid too many parameters, a small 3x3 convolution kernel is used in all layers.
* Input to VGG Model is **224x224** sized **RGB** Images, contains **3x3** and **1x1** filters and number of fully connected layers differs from VGG-11 to VGG-19.
* 1x1 kernels is introduced to increase expressive power of network and reduce the amount of calculations without affecting input and output dimension.
* In VGG, concept of **using multiple small kernels in multiple stacked Conv. layers** is used insead of **using less no. of Conv. layers and large kernels**, to reduce the model size by reducing total parameters. This adds **more non-linearity** as activation function (Relu) in used multiple times in a set of Conv layes.
* Here, the receptive field of large kernel Conv. layer is same as stacked small kernels Conv. layers with **reduced parameteres**.
* The overall structure includes **5 sets of Conv.** layers followed by **Max Pooling** layers.

---



## Implementing Project:
1. **Clone Repository and Install [Anaconda](https://docs.anaconda.com/anaconda/install/).**

2. **Create Conda Environment with Python 3.6:** 

    conda create -n env_name python=3.6 

3. **Install Libraries from Requirements.txt:**

    pip install -r requirements.text

4. **Run app.py:**
    
    python app.py

This will run the app on your local machine.

---

## About me

**Piyush Pathak**

[**PORTFOLIO**](https://anirudhrapathak3.wixsite.com/piyush)

[**GITHUB**](https://github.com/piyushpathak03)

[**BLOG**](https://medium.com/@piyushpathak03)


# 📫 Follw me: 

[![Linkedin Badge](https://img.shields.io/badge/-PiyushPathak-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/piyushpathak03/)](https://www.linkedin.com/in/piyushpathak03/)

<p  align="right"><img height="100" src = "https://media.giphy.com/media/l3URDstnIjBNY7rwLB/giphy.gif"></p>



