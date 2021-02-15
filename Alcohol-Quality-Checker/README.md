# **Alcohol-Quality-Checker**
## Predicting Quality of Alcohol

<img src="https://github.com/manthanpatel98/Alcohol-Quality-Checker/blob/master/README-Resources/AlcoholQuality.jpg" width=600>

---

### **Web APP on Heroku**
<img src="https://github.com/manthanpatel98/Alcohol-Quality-Checker/blob/master/README-Resources/AlcoholQuality.gif" width=600>

**[The Project on Heroku](https://alcoholqualitychecker.herokuapp.com/)**

---
## The Dataset
![](https://github.com/manthanpatel98/Alcohol-Quality-Checker/blob/master/README-Resources/Screenshot%20(105).png)
### **[Dataset](https://github.com/manthanpatel98/Alcohol-Quality-Checker/blob/master/alcohol-quality-data.csv)**
---
## **Overview**
* The Dataset has **'density'**, **'pH'**, **'sulphates'**, **'alcohol'**, **'Quality_Category'** columns. It has **4898 rows** and **5 columns**.
* From the Dataset, we have to predict the **Quality of Alcohol**: **"High"** or **"Low"**.
* **ExtraTreesClassifier** has been used for Feature Selection.
* I have applied **Artificial Neural Network**, **Random Forest**, **Decision Tree**, **K-NN**, **Naive bayes classification** and **SVM** algorithms but at the end, **KNN** gave better results.

---
## **Machine Learning Pipelines:**
---
### **1> Feature Engineering:**
  
**a> Handling Missing Values:**
* Here, In this data, there is no requirement of handling missing values because already it is a complete dataset. 
    
**b> Feature Encoding:**   
* In this data, we do not have much categorical columns except output column.

**c> Feature Scaling & Feature Transformation:**    
* For alogorithms like K-NN , K means , all neural network etc are based on some distance equations. Hence, they require Scaling. 
* But, when i applied it, there was not much of a difference in the accuracy so there was no meaning of using it. Because not everytime,we have to use scaling or transformation. * Transformation also seemed not required for this data because the distribution is almost gaussian for the required columns.
---    
### **2> Feature Selection:**    
* There are various techniques for this but here i have used **ExtraTressClassifier**. For, this Project ExtraTressClassifier showed **2 columns** as most important **"sulfate"** and **"Alcohol Level"**.

![Feature Selection](https://github.com/manthanpatel98/Alcohol-Quality-Checker/blob/master/README-Resources/Screenshot%20(106).png)

---   

### **3,4&5> Model Selection**, **Model Creation**, **Testing**
    
* To get the proper accuracy and for the proper splitting of the train and test data, I have used **Stratified K Fold Cross Validation** as it is very efficient in splitting the dataset.
    
* Here, I have tried many algorithms like **Artificial Neural Network**, **Random Forest**, **Decision Tree**, **K-NN**, **Naive bayes classification** and **SVM**. 
* Among these, K-NN has  gaven the higher accuracy (80%).
* For this I have tried all the values k values **till 500** and **k=125** gave better results.
    
| Algorithm | Average Accuracy |
| ---- | ----|
| Random Forest | 76.19% |
| Decision Tree | 75.88% |
| K-NN | 79.48% |
| SVM | 79.7% |
| Naive bayes | 78.21% |
| ANN | 78.00% |

---
* Finally, I decided to go with KNN because as we know **SVM generally has higher variance**, whereas in KNN we can fix it by **choosing the right K value**. In my project **k=125** gave better results.
* For detailed look at Project, go to **[Alcohol-Quality.ipynb](https://github.com/manthanpatel98/Alcohol-Quality-Checker/blob/master/Alcohol-Quality.ipynb)** and **[model.py](https://github.com/manthanpatel98/Alcohol-Quality-Checker/blob/master/model.py)**

## About me

**Piyush Pathak**

[**PORTFOLIO**](https://anirudhrapathak3.wixsite.com/piyush)

[**GITHUB**](https://github.com/piyushpathak03)

[**BLOG**](https://medium.com/@piyushpathak03)


# 📫 Follw me: 

[![Linkedin Badge](https://img.shields.io/badge/-PiyushPathak-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/piyushpathak03/)](https://www.linkedin.com/in/piyushpathak03/)

<p  align="right"><img height="100" src = "https://media.giphy.com/media/l3URDstnIjBNY7rwLB/giphy.gif"></p>


