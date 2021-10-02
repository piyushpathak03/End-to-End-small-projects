#!/usr/bin/env python
# coding: utf-8

# # Heat Exchanger Price Prediction Model

# ### Import Libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ### Import dataset

# In[2]:


data = pd.read_excel('D:/Data Science/Capstone Project/ML/TTR/dataset1.xlsx')


# In[3]:


data.shape


# In[4]:


data.head()


# ### Check missing values and Data types

# In[427]:


data.info()


# Data types are okay so, no conversion required 

# In[428]:


data.isnull().sum()


# In[429]:


data.shape


# ### Lets treat the null values

# In[430]:


data.isnull().sum()


# We need to drop the null values since it invloves the technical features and replacing it with any metric 
# 
# would hamper the accuracy of the data.

# In[431]:


data_new = data.dropna()


# In[432]:


data_new.isnull().sum()


# In[433]:


data_new.info()


# In[434]:


data_new.describe()


# Lets check what product range we are dealing with

# In[435]:


pd.unique(data_new['Part Level'].values)


# The data consists total 6 products ECS (Engine Cooling System), Raditor, Core (Sub-assembly), CRFMS (Condenser Fan Motor Shroud), RFMS (Radiator Fan Motor Shroud) & Intercooler (Charged Air Cooler)

# Lets check the customer portfolio of the organisation

# In[436]:


pd.unique(data_new['Customer'].values)


# Lets know check the segment and category coloumn

# In[437]:


pd.unique(data_new['Segment'].values)


# The data consists of 5 segments

# In[438]:


pd.unique(data_new['Category'].values)


# ### Check for skewness and outliers in data.

# In[439]:


plt.figure(figsize=(20,8))

plt.subplot(1,2,1)
plt.title('Price Distribution Plot')
sns.distplot(data_new.Price)

plt.subplot(1,2,2)
plt.title('Product Price Spread')
sns.boxplot(y=data_new.Price)

plt.show()


# In[440]:


data_new.Price.describe()


# The plot seemed to be right-skewed, meaning that the most prices in the dataset are low.
# 
# There is a significant difference between the mean and the median of the price distribution.
# 
# The data points are far spread out from the mean, which indicates a high variance in the products prices.
# 
# 75% of the prices are below Rs.9895.54 remaining 25% are between Rs.9,895.54 and Rs.50,867.
# 
# There are values observed in the price distribution spread box/whiskers plot, in which there are value above Rs. 20,000. As per marketing team these values are not outliers since, the price of higher cooling capacity products will be high. 

# Need to convert the columns name for ease of syntax

# In[441]:


# change the column names
data_new.rename(index=str, columns={'TTR part num': 'partcode',
                              'Part Level' : 'part_level',
                              'Customer' : 'customer',
                              'Segment' : 'segment',
                              'End Customer' : 'end_customer',
                              'Category' : 'category',
                              'Description' : 'description',
                              'Core Thickness' : 'core_thickness',
                                'Core Width' : 'core_width',
                              'Core Height' : 'core_height',
                              'Fin Type' : 'fin_type',
                              'Tube per core' : 'tube_per_core',
                                'Tank' : 'tank',
                              'Price' : 'price'}, inplace=True)
data_new.info()


# Since partcode and description are unique values lets drop them.

# In[442]:


del data_new['partcode']


# In[443]:


del data_new['description']


# In[444]:


data_new.info()


# ### Exploration of the categorical features of the product.

# In[445]:


plt.figure(figsize=(25, 6))

plt.subplot(1,4,1)
plt1 = data_new.customer.value_counts().plot(kind='bar')
plt.title('Companies Histogram')
plt1.set(xlabel = 'Customer', ylabel='Frequency of Customer')

plt.subplot(1,4,2)
plt1 = data_new.part_level.value_counts().plot(kind='bar')
plt.title('Product Range')
plt1.set(xlabel = 'Part Level', ylabel='Frequency of Part Level')

plt.subplot(1,4,3)
plt1 = data_new.segment.value_counts().plot(kind='pie')
plt.title('Segment distribution')

plt.subplot(1,4,4)
plt1 = data_new.category.value_counts().plot(kind='pie')
plt.title('Category Distribution')

plt.show()


# 1. Most of the RFQ's recieved are from Tata Motors.
# 2. Most sold product range is Engine Cooling System whereas least sold product range Condenser Radiator Fan Motor Shroud.
# 3. Maximum RFQ's belong to Commercial vehicle segment.
# 4. It seems the organisation has dominance in domestic market along with international presence.

# In[446]:


plt.figure(figsize=(20,8))

plt.subplot(1,2,1)
plt.title('End Customer')
sns.countplot(data_new.end_customer, palette=("cubehelix"))

plt.subplot(1,2,2)
plt.title('Segment vs Price')
sns.boxplot(x=data_new.segment, y=data_new.price, palette=("cubehelix"))

plt.show()


# 1. Share of business in OEM (Orignal Equipment Manufacturer) is maximum.
# 2. It seems OEM are managing their SPD (Spare Parts Division) by buying with extra schedule.
# 3. Gen set segment is highly priced segment with second highest market share in product range.
# 4. Second expensive segment is commercial vehicle with highest market share within the organisations product range.

# In[447]:


plt.figure(figsize=(20,8))

plt.subplot(1,2,1)
plt.title('Core Thickness')
sns.countplot(data_new.core_thickness, palette=("cubehelix"))

plt.subplot(1,2,2)
plt.title('Core Thickness vs Price')
sns.boxplot(x=data_new.core_thickness, y=data_new.price, palette=("cubehelix"))

plt.show()


# 1. Count of products with core_thickness is high for 48mm and second highest is 36mm.
# 2. Price range of the product for 48mm thickness core is also wide with higher count of products.
# 3. Most expensive core_thickness is 102mm but count of the products is quite less.

# Lets check the relation of technical features of the product versus the price.

# In[448]:


def scatter(x,fig):
    plt.subplot(5,2,fig)
    plt.scatter(data_new[x],data_new['price'])
    plt.title(x+' vs Price')
    plt.ylabel('Price')
    plt.xlabel(x)

plt.figure(figsize=(10,20))

scatter('core_thickness', 1)
scatter('core_width', 2)
scatter('core_height', 3)
scatter('tube_per_core', 4)

plt.tight_layout()


# In[449]:


plt.figure(figsize=(8,6))

plt.title('Tank vs Price')
sns.scatterplot(x=data_new['part_level'],y=data_new['price'],hue=data_new['tank'])
plt.xlabel('Tank')
plt.ylabel('Price')

plt.show()
plt.tight_layout()


# It seems Casting tanks are only used in a particular product and that is intercooler.
# 
# Also, we cannot relate the tank type and price of the product. Going ahead we shall drop the column tank.

# In[450]:


plt.figure(figsize = (10, 8))
sns.heatmap(data_new.corr(), annot = True, cmap="YlGnBu")
plt.show()


# There is high correlation between Core_width and tubes_per_core so, we will drop one of them to reduce the dimensions.
# 
# This would help in tackling the highly corelated features.

# Going further categorical data needs to be converted into numeric.
# 
# But before that, we need to check the feature importance.

# In[451]:


data1 = data_new[['part_level', 'segment','end_customer', 'category','core_thickness',
                  'core_width', 'core_height','tube_per_core', 'tank','price']]
data1.head()


# In[452]:


data1.columns


# Now before passing the data through our selected, lets create the dummies and convert all the categorical values into numerical ones  

# In[453]:


def dummies(x,df):
    temp = pd.get_dummies(df[x], drop_first = True)
    df = pd.concat([df, temp], axis = 1)
    df.drop([x], axis = 1, inplace = True)
    return df

data1 = dummies('part_level',data1)
data1 = dummies('segment',data1)
data1 = dummies('end_customer',data1)
data1 = dummies('category',data1)


# In[454]:


data1.head()


# In[455]:


data1.shape


# Now lets drop the target variable and other feature which had no significance with price variation

# In[456]:


X = data1.drop('price', axis=1)
X = data1.drop('tank', axis=1)
X.head()


# In[457]:


y= data1[['price']]
y.head()


# Spliting the data before passing it through the algorithm.

# In[458]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# Now lets apply Random forest model

# In[459]:


from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=1000, random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)


# Lets evaluate the model using MAE and R2 score.

# In[460]:


from sklearn import metrics

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('R2 Score:', metrics.r2_score(y_test, y_pred))


# As per the evaluation metric the R2 score is close to 1 which is good
# 
# Mean Absolute error is 62.13
# 
# Lets check whether this error can be reudeced further

# Applying standardization technique on the target variable

# In[461]:


from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)


# Splitting stadardized data once again

# In[462]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# In[463]:


from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators=1000, random_state=0)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)


# In[464]:


from sklearn import metrics

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('R2 Score:', metrics.r2_score(y_test, y_pred))


# ### As per the evaluation the R2 score is good and the error obtained has also reduced which we have achieved using standardization.
