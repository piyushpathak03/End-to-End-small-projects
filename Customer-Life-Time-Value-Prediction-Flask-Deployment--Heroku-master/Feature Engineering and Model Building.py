
############# Customer Lifetime Value Prediction ################## 
            
        # FEATURE ENGINEERING AND MODEL BUILDING  # 
##################################################################
# Load Libraries #
##################################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_profiling import ProfileReport
import warnings
warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', 35)
##################################################################
# Load Data #
##################################################################

df = pd.read_csv("CLV_Train.csv")
df

df.describe()
##################################################################
# Data Preprocessing #
##################################################################

df['Lati'], df['Longi'] = df['Location.Geo'].str.split(',', 1).str
df

df.isna().sum()

df.dtypes
##################################################################
# FEATURE ENGINEERING #
##################################################################

### Creating Feature With  Latitude ans Longitude Using  || HAVERSINE FORMULA ||

df['Lati']= pd.to_numeric(df['Lati'],errors='coerce')
df['Longi']= pd.to_numeric(df['Longi'],errors='coerce')

import math
df['LAT_rad'], df['LON_rad'] = np.radians(df['Lati']), np.radians(df['Longi'])
df['dLON'] = df['LON_rad'] - math.radians(-56.7213600)
df['dLAT'] = df['LAT_rad'] - math.radians(37.2175900)
df['distance'] = 6367 * 2 * np.arcsin(np.sqrt(np.sin(df['dLAT']/2)**2 + math.cos(math.radians(37.2175900)) * np.cos(df['LAT_rad']) * np.sin(df['dLON']/2)**2))


df['Vehicle.Class'] = pd.get_dummies(df['Vehicle.Class'])
df['Sales.Channel'] = pd.get_dummies(df['Sales.Channel'])
df['Renew.Offer.Type'] = pd.get_dummies(df['Renew.Offer.Type'])
df['Policy'] = pd.get_dummies(df['Policy'])
df['Policy.Type'] = pd.get_dummies(df['Policy.Type'])
df['Marital.Status'] = pd.get_dummies(df['Marital.Status'])
df['Gender'] = pd.get_dummies(df['Gender'])
df['EmploymentStatus'] = pd.get_dummies(df['EmploymentStatus'])
df['Location.Code'] = pd.get_dummies(df['Location.Code'])


df['Vehicle.Class'] = df['Vehicle.Class'].astype(int)
df['Sales.Channel'] = df['Sales.Channel'].astype(int)
df['Renew.Offer.Type'] = df['Renew.Offer.Type'].astype(int)
df['Policy'] = df['Policy'].astype(int)
df['Policy.Type'] = df['Policy.Type'].astype(int)
df['Marital.Status'] = df['Marital.Status'].astype(int)
df['Gender'] = df['Gender'].astype(int)
df['EmploymentStatus'] = df['EmploymentStatus'].astype(int)
df['Location.Code'] = df['Location.Code'].astype(int)

df = df.drop(['LAT_rad','LON_rad','dLON','dLAT','Lati','Longi','Location.Geo','CustomerID'],axis=1)

df['Monthly.Premium.Auto'] = df['Monthly.Premium.Auto'].fillna(df['Monthly.Premium.Auto'].mean())
df['Number.of.Open.Complaints'] = df['Number.of.Open.Complaints'].fillna(df['Number.of.Open.Complaints'].mean())
df['Number.of.Policies'] = df['Number.of.Policies'].fillna(df['Number.of.Policies'].mean())
df['Vehicle.Size'] = df['Vehicle.Size'].fillna(df['Vehicle.Size'].mean())
df['distance'] = df['distance'].fillna(df['distance'].mean())

df['Coverage'] = df['Coverage'].fillna(df['Coverage'].mode()[0])
df['Education'] = df['Education'].fillna(df['Education'].mode()[0])

# Label Encoding

def Label_Encoding(x):
    from sklearn.preprocessing import LabelEncoder
    from sklearn import preprocessing
    category_col =[var for var in x.columns if x[var].dtypes =="object"] 
    labelEncoder = preprocessing.LabelEncoder()
    mapping_dict={}
    for col in category_col:
        x[col] = labelEncoder.fit_transform(x[col])
        le_name_mapping = dict(zip(labelEncoder.classes_, labelEncoder.transform(labelEncoder.classes_)))
        mapping_dict[col]=le_name_mapping
    return mapping_dict
Label_Encoding(df)


plt.rcParams["figure.figsize"] = 20,18
df.hist()

# Removing Outliers

dff= df
q1 =dff['Customer.Lifetime.Value'].quantile(.25)
q3 = dff['Customer.Lifetime.Value'].quantile(.75)
iqr = q3-q1

df_out = dff[~((df['Customer.Lifetime.Value'] < (q1 - 1.5 *iqr))  |  (dff['Customer.Lifetime.Value'] > (q3+ 1.5 * iqr)))]
df_out

##################################################################
# TRAIN TEST SPLIT #
##################################################################
x= df_out.drop(['Customer.Lifetime.Value'],axis=1)
y = df_out['Customer.Lifetime.Value']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=42)

import statsmodels.api as sm
model2 =sm.OLS(y_train,x_train).fit()

model2.summary()

##################################################################
# FEATURE SELECTION #
##################################################################

from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestRegressor
estimator = RandomForestRegressor()
selector = RFE(estimator,6,step=1)
selector = selector.fit(x_train,y_train)
rank =pd.DataFrame(selector.ranking_,columns=['Importance'])

Columns = pd.DataFrame(x_train.columns,columns=['Columns'])
RFE = pd.concat([rank,Columns],axis=1)
RFE.sort_values(["Importance"], axis=0, 
                 ascending=True, inplace=True) 
RFE

xx_train = x_train.drop(['Renew.Offer.Type','Gender','Sales.Channel','Marital.Status','Policy.Type','Vehicle.Class','EmploymentStatus','Policy','Location.Code','Coverage'],axis=1)

x_test = x_test.drop(['Renew.Offer.Type','Gender','Sales.Channel','Marital.Status','Policy.Type','Vehicle.Class','EmploymentStatus','Policy','Location.Code','Coverage'],axis=1)

##################################################################
# MODEL BUILDING #
##################################################################

import statsmodels.api as sm
model2 =sm.OLS(y_train,xx_train).fit()

model2.summary()


# Linear Regression 
## RMSE 	==> 3779.78
## RScore 	==> 0.27
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(xx_train,y_train)
lr_y_pred=lr.predict(x_test)

from sklearn import metrics
lr_RMSE = np.sqrt(metrics.mean_squared_error(y_test,lr_y_pred))
lr_RMSE

from sklearn.metrics import r2_score
lr_r2_score = r2_score(y_test,lr_y_pred)
lr_r2_score


# Random Forest
## RMSE 	==> 1298.78
## RScore 	==> 0.80
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=1000,random_state=3)
reg=regressor.fit(xx_train,y_train)

rf_y_pred=regressor.predict(x_test)


from sklearn import metrics
rf_RMSE = np.sqrt(metrics.mean_squared_error(y_test,rf_y_pred))
print('RMSE::',rf_RMSE)

from sklearn.metrics import r2_score
rf_RScore = r2_score(y_test,rf_y_pred)
print('R Score::',rf_RScore)


# Random Forest Model Parameter Optimization 1
## RMSE 	==> 998.56
## RScore 	==> 0.88
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=1000,random_state=3,max_depth=9)
reg=regressor.fit(xx_train,y_train)

rf_y_pred=regressor.predict(x_test)


from sklearn import metrics
rf_RMSE = np.sqrt(metrics.mean_squared_error(y_test,rf_y_pred))
print('RMSE::',rf_RMSE)

from sklearn.metrics import r2_score
rf_RScore = r2_score(y_test,rf_y_pred)
print('R Score::',rf_RScore)


# Random Forest Model Parameter Optimization 2
## RMSE 	==> 994.28
## RScore 	==> 0.90
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=1000,random_state=3,max_depth=13)
reg=regressor.fit(xx_train,y_train)

rf_y_pred=regressor.predict(x_test)


from sklearn import metrics
rf_RMSE = np.sqrt(metrics.mean_squared_error(y_test,rf_y_pred))
print('RMSE::',rf_RMSE)

from sklearn.metrics import r2_score
rf_RScore = r2_score(y_test,rf_y_pred)
print('R Score::',rf_RScore)


# Random Forest Model Parameter Optimization 3
## RMSE 	==> 990.47
## RScore 	==> 0.90
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=1000,random_state=29,max_depth=13)
reg=regressor.fit(xx_train,y_train)

rf_y_pred=regressor.predict(x_test)


from sklearn import metrics
rf_RMSE = np.sqrt(metrics.mean_squared_error(y_test,rf_y_pred))
print('RMSE::',rf_RMSE)

from sklearn.metrics import r2_score
rf_RScore = r2_score(y_test,rf_y_pred)
print('R Score::',rf_RScore)


# Random Forest Model Parameter Optimization 4
## RMSE 	==> 988.78
## RScore 	==> 0.90
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=1000,random_state=29,max_depth=13)
reg=regressor.fit(xx_train,y_train)

rf_y_pred=regressor.predict(x_test)


from sklearn import metrics
rf_RMSE = np.sqrt(metrics.mean_squared_error(y_test,rf_y_pred))
print('RMSE::',rf_RMSE)

from sklearn.metrics import r2_score
rf_RScore = r2_score(y_test,rf_y_pred)
print('R Score::',rf_RScore)



# Random Forest Model Parameter Optimization 5
## RMSE 	==> 986.33
## RScore 	==> 0.90
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=1000,random_state=29,max_depth=13)
reg=regressor.fit(xx_train,y_train)

rf_y_pred=regressor.predict(x_test)


from sklearn import metrics
rf_RMSE = np.sqrt(metrics.mean_squared_error(y_test,rf_y_pred))
print('RMSE::',rf_RMSE)

from sklearn.metrics import r2_score
rf_RScore = r2_score(y_test,rf_y_pred)
print('R Score::',rf_RScore)


# Random Forest Model Parameter Optimization 6
## RMSE 	==> 985.73
## RScore 	==> 0.90
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=100,random_state=29,max_depth=12)
reg=regressor.fit(xx_train,y_train)

rf_y_pred=regressor.predict(x_test)


from sklearn import metrics
rf_RMSE = np.sqrt(metrics.mean_squared_error(y_test,rf_y_pred))
print('RMSE::',rf_RMSE)

from sklearn.metrics import r2_score
rf_RScore = r2_score(y_test,rf_y_pred)
print('R Score::',rf_RScore)

###########################################  BEST MODEL   ###################################
# Random Forest Model Parameter Optimization 6  ======>  || BEST MODEL ||
## RMSE 	==> 983.54
## RScore 	==> 0.90
from sklearn.ensemble import RandomForestRegressor
regressor1 = RandomForestRegressor(n_estimators=100,random_state=29,max_depth=10)
reg=regressor1.fit(xx_train,y_train)

rf_final_pred=regressor1.predict(x_test)


from sklearn import metrics
rf_RMSE = np.sqrt(metrics.mean_squared_error(y_test,rf_final_pred))
print('RMSE::',rf_RMSE)

from sklearn.metrics import r2_score
rf_RScore = r2_score(y_test,rf_final_pred)
print('R Score::',rf_RScore)
##############################################################################################

# KNN Regressor
## RMSE 	==> 994.28
## RScore 	==> 0.90
from sklearn.neighbors import KNeighborsRegressor
clf = KNeighborsRegressor(n_neighbors = 1,  weights = 'distance', p=1)
reg.fit(xx_train, y_train)
KNN_pred = reg.predict(x_test)
from sklearn import metrics
KNN_RMSE = np.sqrt(metrics.mean_squared_error(y_test,KNN_pred))
print('RMSE::',KNN_RMSE)
from sklearn.metrics import r2_score
KNN_r2_score = r2_score(y_test,KNN_pred)
print('R Score::',KNN_r2_score)


# Decision Tree Regressor
## RMSE 	==> 1204.28
## RScore 	==> 0.86
from sklearn.tree import DecisionTreeRegressor
Dtree_reg = DecisionTreeRegressor(max_depth=4,
                           min_samples_split=5,
                           max_leaf_nodes=10)
clf =Dtree_reg.fit(xx_train,y_train)
Dtree_pred = Dtree_reg.predict(x_test)
from sklearn import metrics
Dtree_RMSE = np.sqrt(metrics.mean_squared_error(y_test,Dtree_pred))
print('RMSE::',Dtree_RMSE)
from sklearn.metrics import r2_score
Dtree_r2_score = r2_score(y_test,Dtree_pred)
print('R Score::',Dtree_r2_score)



# Grid Search Cross Validation Random Forest
## RMSE 	==> 971.34
## RScore 	==> 0.91
from sklearn.model_selection import GridSearchCV

param_grid = [
{'n_estimators': [10, 25], 'max_features': [5, 10], 
 'max_depth': [10, 50, None], 'bootstrap': [True, False]}
]

grid_search_forest = GridSearchCV(regressor1, param_grid, cv=10, scoring='neg_mean_squared_error')
grid_search_forest.fit(xx_train, y_train)


cvres = grid_search_forest.cv_results_
for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
    print(np.sqrt(-mean_score), params)


grid_best= grid_search_forest.best_estimator_.predict(x_test)
grid_mse = metrics.mean_squared_error(y_test, grid_best)
grid_rScore = r2_score(y_test, grid_best)
grid_rmse = np.sqrt(grid_mse)
print('The best model from the grid search has a RMSE of', round(grid_rmse, 2))
print('The best model from the grid search has a RMSE of', round(grid_rScore, 2))



# Grid Search Cross Validation Random Forest Optimization 1
## RMSE 	==> 966.76
## RScore 	==> 0.91
from sklearn.model_selection import GridSearchCV

param_grid = [
{'n_estimators': [10, 50], 'max_features': [5, 30], 
 'max_depth': [10, 100, None], 'bootstrap': [True, False]}
]

grid_search_forest = GridSearchCV(regressor1, param_grid, cv=10, scoring='neg_mean_squared_error')
grid_search_forest.fit(xx_train, y_train)


cvres = grid_search_forest.cv_results_
for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
    print(np.sqrt(-mean_score), params)



grid_best= grid_search_forest.best_estimator_.predict(x_test)
grid_mse = metrics.mean_squared_error(y_test, grid_best)
grid_rScore = r2_score(y_test, grid_best)
grid_rmse = np.sqrt(grid_mse)
print('The best model from the grid search has a RMSE of', round(grid_rmse, 2))
print('The best model from the grid search has a RScore of', round(grid_rScore, 2))
