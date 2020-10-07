############# Customer Lifetime Value Prediction ################## 
            
             # Exploratory Data Analysis # 
##################################################################
#Load Libraries#
##################################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_profiling import ProfileReport
import warnings
warnings.filterwarnings("ignore")

##################################################################
#Load Data#
##################################################################
server = 'DESKTOP-GQDTTAA'
db = 'practice'

conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+db+';Trusted_Connection==yes')

sql ="""
SELECT * FROM CustomerLifeTimeValue
"""
df = pd.read_sql(sql,conn)
df

##################################################################
# Generating Profile Report#
##################################################################
from pandas_profiling import ProfileReport
DataProfile = ProfileReport(df,title="Customer Data Profile Report",explorative=True)
DataProfile

###################################################################
#Data Preprocessing# 
###################################################################
df.isna().sum()
df['Coverage'] = df['Coverage'].fillna(df['Coverage'].mode()[0])
df['Education'] = df['Education'].fillna(df['Education'].mode()[0])
df['EmploymentStatus'] = df['EmploymentStatus'].fillna(df['EmploymentStatus'].mode()[0])
df['Location.Code'] = df['Location.Code'].fillna(df['Location.Code'].mode()[0])
df['Marital.Status'] = df['Marital.Status'].fillna(df['Marital.Status'].mode()[0])
df['Monthly.Premium.Auto'] = df['Monthly.Premium.Auto'].fillna(df['Monthly.Premium.Auto'].mode()[0])
df['Number.of.Open.Complaints'] = df['Number.of.Open.Complaints'].fillna(df['Number.of.Open.Complaints'].mode()[0])
df['Number.of.Policies'] = df['Number.of.Policies'].fillna(df['Number.of.Policies'].mode()[0])
df['Policy.Type'] = df['Policy.Type'].fillna(df['Policy.Type'].mode()[0])
df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
df['Vehicle.Class'] = df['Vehicle.Class'].fillna(df['Vehicle.Class'].mode()[0])
df['Vehicle.Size'] = df['Vehicle.Size'].fillna(df['Vehicle.Size'].mode()[0])
df['Policy'] = df['Policy'].fillna(df['Policy'].mode()[0])
df['Renew.Offer.Type'] = df['Renew.Offer.Type'].fillna(df['Renew.Offer.Type'].mode()[0])
df['Sales.Channel'] = df['Sales.Channel'].fillna(df['Sales.Channel'].mode()[0])
class color:
   BOLD = '\033[1m'
   END = '\033[0m'
print(color.BOLD +'Total of Missing Values is  :: '+ color.END,df.isna().sum().sum())

### Renaming Columns ###
df = df.rename(columns={'Customer.Lifetime.Value':"Customer_Lifetime_Value",'Location.Geo':"Location_Geo",'Location.Code':"Location_Code",'Marital.Status':"Marital_Status",'Monthly.Premium.Auto':"Monthly_Premium_Auto",'Months.Since.Last.Claim':"Months_Since_Last_Claim",'Months.Since.Policy.Inception':"Months_Since_Policy_Inception",'Number.of.Open.Complaints':"Number_of_Open_Complaints",'Number.of.Policies':"Number_of_Policies",'Policy.Type':"Policy_Type",'Renew.Offer.Type':"Renew_Offer_Type",'Sales.Channel':"Sales_Channel",'Total.Claim.Amount':"Total_Claim_Amount",'Vehicle.Class':"Vehicle_Class",'Vehicle.Size':"Vehicle_Size"})

df =df.replace({'Income': {'?': ''}}, regex=False)
df['Income'] = pd.to_numeric(df['Income'])
Location_Geo1=[]
for txt in df['Location_Geo']:
    val = txt.replace(".","");
    val = txt.replace(".","");
    Location_Geo1.append(val)
Location_Geo1 = pd.DataFrame(Location_Geo1)
Location_Geo =[]
for txt in Location_Geo1[0]:
    val = txt.replace(",","");
    Location_Geo.append(val)
Location_Geo = pd.DataFrame(Location_Geo)
Location_Geo = Location_Geo.rename(columns={0:'Location_Geo'})

df['Location_Geo'] = Location_Geo['Location_Geo']

df =df.replace({'Location_Geo': {'NANA': '189726'}}, regex=False)

df['Location_Geo'] = pd.to_numeric(df['Location_Geo'])

df.dtypes

##################################################################
#Exploratory Data Analysis#
##################################################################
plt.rcParams["figure.figsize"] = 15,10
df.hist()
#-------------------------------------------------------------#
import plotly.express as px
fig = px.scatter(df, x="Location_Geo", y="Customer_Lifetime_Value", color="Gender")
fig.update_traces(marker=dict(size=10,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
fig.show()
#-------------------------------------------------------------#
fig = px.scatter(df, x="Monthly_Premium_Auto", y="Customer_Lifetime_Value", color="Gender")
fig.update_traces(marker=dict(size=10,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
fig.show()
#-------------------------------------------------------------#
fig = px.scatter(df, x="Monthly_Premium_Auto", y="Customer_Lifetime_Value", color="EmploymentStatus")
fig.update_traces(marker=dict(size=10,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
fig.show()
#-------------------------------------------------------------#
fig = px.scatter(df, x="Months_Since_Policy_Inception", y="Customer_Lifetime_Value", color="Gender")
fig.update_traces(marker=dict(size=10,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
fig.show()
#-------------------------------------------------------------#
fig = px.scatter(df, x="Total_Claim_Amount", y="Customer_Lifetime_Value", color="Gender")
fig.update_traces(marker=dict(size=10,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
fig.show()
#-------------------------------------------------------------#

fig = px.scatter(df, x="Total_Claim_Amount", y="Customer_Lifetime_Value", color="EmploymentStatus")
fig.update_traces(marker=dict(size=10,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
fig.show()
#-------------------------------------------------------------#
fig_dims = (15, 5)
fig, ax = plt.subplots(figsize=fig_dims)
sns.barplot(x="Gender", y="CustomerID", hue="Education", data=df,ax=ax)
#-------------------------------------------------------------#
fig_dims = (15, 5)
fig, ax = plt.subplots(figsize=fig_dims)
sns.barplot(x="Marital_Status", y="CustomerID", hue="Education", data=df,ax=ax)
#-------------------------------------------------------------#

fig = px.box(df, x="Customer_Lifetime_Value", y="EmploymentStatus", color="Gender")
fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
fig.show()
#-------------------------------------------------------------#

fig = px.box(df, x="Customer_Lifetime_Value", y="Education", color="Gender")
fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
fig.show()
#-------------------------------------------------------------#

fig = px.box(df, x="Customer_Lifetime_Value", y="Policy_Type", color="Gender")
fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
fig.show()
#-------------------------------------------------------------#
fig = px.box(df, x="Customer_Lifetime_Value", y="Policy_Type", color="EmploymentStatus")
fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
fig.show()

fig = px.box(df, x="Customer_Lifetime_Value", y="Policy_Type", color="Marital_Status")
fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
fig.show()
#-------------------------------------------------------------#

fig = px.violin(df, y="Location_Geo", x="Marital_Status", color="Gender", box=True, points="all",
          hover_data=df.columns)
fig.show()
#-------------------------------------------------------------#
fig = px.violin(df, y="Customer_Lifetime_Value", x="Gender", color="Marital_Status", box=True, points="all",
          hover_data=df.columns)
fig.show()
#-------------------------------------------------------------#

fig = px.violin(df, y="Customer_Lifetime_Value", x="Gender", color="EmploymentStatus", box=True, points="all",
          hover_data=df.columns)
fig.show()
#-------------------------------------------------------------#

fig = px.histogram(df,y="Customer_Lifetime_Value", histnorm='probability density', color="Gender")
fig.show()


fig = px.histogram(df,y="Income", histnorm='probability density', color="Gender")
fig.show()
#-------------------------------------------------------------#

fig = px.histogram(df,y="Total_Claim_Amount", histnorm='probability density', color="Gender")
fig.show()
#-------------------------------------------------------------#
fig = px.histogram(df,y="Location_Geo", histnorm='probability density', color="Gender")
fig.show()
#-------------------------------------------------------------#
fig = px.histogram(df,x="Total_Claim_Amount",y='Education',histnorm='probability density', color="Gender")
fig.show()
#-------------------------------------------------------------#
fig = px.histogram(df,x="Total_Claim_Amount",y='Gender',histnorm='probability density', color="Education")
fig.show()
#-------------------------------------------------------------#
fig = px.histogram(df,x="Total_Claim_Amount",y='EmploymentStatus',histnorm='probability density', color="Gender")
fig.show()
#-------------------------------------------------------------#

fig = px.histogram(df,x="Total_Claim_Amount",y='Gender',histnorm='probability density', color="EmploymentStatus")
fig.show()
#-------------------------------------------------------------#
##################################################################
# Pivot Table  Analysis #
##################################################################
pd.pivot_table(df,index=["Education"], values=["Customer_Lifetime_Value","Total_Claim_Amount"])

pd.pivot_table(df,index=["Gender"], values=["Customer_Lifetime_Value","Total_Claim_Amount"])

pd.pivot_table(df,index=["Gender","Marital_Status"], values=["Customer_Lifetime_Value","Total_Claim_Amount"])

pd.pivot_table(df,index=["EmploymentStatus"], values=["Customer_Lifetime_Value","Total_Claim_Amount"])

pd.pivot_table(df,index=["Policy_Type","Gender"], values=["Customer_Lifetime_Value","Total_Claim_Amount"])

pd.pivot_table(df,index=["Policy_Type","EmploymentStatus"], values=["Customer_Lifetime_Value","Total_Claim_Amount"])

pd.pivot_table(df,index=["Policy","Gender"], values=["Customer_Lifetime_Value","Total_Claim_Amount"])

pd.pivot_table(df,index=["Policy","EmploymentStatus"], values=["Customer_Lifetime_Value","Total_Claim_Amount"])

##################################################################
# Cross Tabulation Analysis #
##################################################################
def compute_Tabulation(x,y):
    val = pd.crosstab(x,y)
    return val

compute_Tabulation(df['Policy_Type'],df['Marital_Status'])

compute_Tabulation(df['Policy_Type'],df['Marital_Status']).plot(kind='bar')

compute_Tabulation(df['Policy_Type'],df['Gender'])

compute_Tabulation(df['Policy_Type'],df['Gender']).plot(kind='bar')

compute_Tabulation(df['Policy_Type'],df['EmploymentStatus'])

compute_Tabulation(df['Policy_Type'],df['EmploymentStatus']).plot(kind='bar')

compute_Tabulation(df['Policy_Type'],df['Location_Code'])

compute_Tabulation(df['Policy_Type'],df['Location_Code']).plot(kind='bar')

compute_Tabulation(df['Gender'],df['Marital_Status'])

compute_Tabulation(df['Gender'],df['Marital_Status']).plot(kind='bar')

###############################################################
# Grouped Cross Tabulation Analysis #
###############################################################

married = df[df['Marital_Status']=='Married']
class color:
   BOLD = '\033[1m'
   END = '\033[0m'
print(color.BOLD +'Tabulation of Only Married People'+ color.END)
compute_Tabulation(married['Policy_Type'],married['EmploymentStatus'])


compute_Tabulation(married['Policy_Type'],married['EmploymentStatus']).plot(title='All are Married',kind='bar')


married = df[df['Marital_Status']=='Single']
# class color:
#    BOLD = '\033[1m'
#    END = '\033[0m'
print(color.BOLD +'Tabulation of Only Single People'+ color.END)
compute_Tabulation(married['Policy_Type'],married['EmploymentStatus'])


compute_Tabulation(married['Policy_Type'],married['EmploymentStatus']).plot(title='All are Single',kind='bar')

#-------------------------------------------------------------#

married = df[df['Marital_Status']=='Married']
male = married[married['Gender']=='M']
# class color:
#    BOLD = '\033[1m'
#    END = '\033[0m'
print(color.BOLD +'Tabulation of Only Married Male People'+ color.END)
compute_Tabulation(male['Policy_Type'],male['EmploymentStatus'])


compute_Tabulation(male['Policy_Type'],male['EmploymentStatus']).plot(kind='bar')
#-------------------------------------------------------------#

married = df[df['Marital_Status']=='Married']
female = married[married['Gender']=='F']
# class color:
#    BOLD = '\033[1m'
#    END = '\033[0m'
print(color.BOLD +'Tabulation of Only Married Female People'+ color.END)
compute_Tabulation(female['Policy_Type'],female['EmploymentStatus'])


compute_Tabulation(female['Policy_Type'],female['EmploymentStatus']).plot(kind='bar')
#-------------------------------------------------------------#

Employed = df[df['EmploymentStatus']=='Employed']
# class color:
#    BOLD = '\033[1m'
#    END = '\033[0m'
print(color.BOLD +'Tabulation of Only Employed People'+ color.END)
compute_Tabulation(Employed['Policy_Type'],Employed['Marital_Status'])


compute_Tabulation(Employed['Policy_Type'],Employed['Marital_Status']).plot(title='All are Employed',kind='bar')
#-------------------------------------------------------------#

UnEmployed = df[df['EmploymentStatus']=='Unemployed']
# class color:
#    BOLD = '\033[1m'
#    END = '\033[0m'
print(color.BOLD +'Tabulation of Only UnEmployed People'+ color.END)
compute_Tabulation(UnEmployed['Policy_Type'],UnEmployed['Marital_Status'])


compute_Tabulation(UnEmployed['Policy_Type'],UnEmployed['Marital_Status']).plot(kind= 'bar')
#-------------------------------------------------------------#

Employed = df[df['EmploymentStatus']=='Employed']
Employed_Male = Employed[Employed['Gender']== 'M']
# class color:
#    BOLD = '\033[1m'
#    END = '\033[0m'
print(color.BOLD +'Tabulation of Only Employed Male People'+ color.END)
compute_Tabulation(Employed_Male['Policy_Type'],Employed_Male['Marital_Status'])


compute_Tabulation(Employed_Male['Policy_Type'],Employed_Male['Marital_Status']).plot(kind='bar')
#-------------------------------------------------------------#

Employed = df[df['EmploymentStatus']=='Employed']
Employed_FeMale = Employed[Employed['Gender']== 'F']
# class color:
#    BOLD = '\033[1m'
#    END = '\033[0m'
print(color.BOLD +'Tabulation of Only Employed Male People'+ color.END)
compute_Tabulation(Employed_FeMale['Policy_Type'],Employed_FeMale['Marital_Status'])


compute_Tabulation(Employed_FeMale['Policy_Type'],Employed_FeMale['Marital_Status']).plot(kind='bar')
#-------------------------------------------------------------#

UnEmployed = df[df['EmploymentStatus']=='Unemployed']
UnEmployed_Male = UnEmployed[UnEmployed['Gender']== 'M']
# class color:
#    BOLD = '\033[1m'
#    END = '\033[0m'
print(color.BOLD +'Tabulation of Only UnEmployed Male People'+ color.END)
compute_Tabulation(UnEmployed_Male['Policy_Type'],UnEmployed_Male['Marital_Status'])


compute_Tabulation(UnEmployed_Male['Policy_Type'],UnEmployed_Male['Marital_Status']).plot(kind='bar')
#-------------------------------------------------------------#

UnEmployed = df[df['EmploymentStatus']=='Unemployed']
UnEmployed_FeMale = UnEmployed[UnEmployed['Gender']== 'F']
# class color:
#    BOLD = '\033[1m'
#    END = '\033[0m'
print(color.BOLD +'Tabulation of Only UnEmployed FeMale People'+ color.END)
compute_Tabulation(UnEmployed_FeMale['Policy_Type'],UnEmployed_FeMale['Marital_Status'])


compute_Tabulation(UnEmployed_FeMale['Policy_Type'],UnEmployed_FeMale['Marital_Status']).plot(kind='bar')
#-------------------------------------------------------------#
####################################################################
# Chi Square Test #
####################################################################
from scipy.stats import chi2_contingency,chi2

def Chi_Square_Test(x,y,confidence_interval):
    cross_table = pd.crosstab(x,y,margins=True)
    statistic_val,prob_val,dof,expected = chi2_contingency(cross_table)
    print("Chi_Square Value = {0}".format(statistic_val))
    print("P-Value = {0}".format(prob_val))
    alpha = 1 - confidence_interval
    
    if prob_val > alpha:
        print(">> Accepting Null Hypothesis <<")
        print(color.BOLD +"No Relationship"+ color.END)
    else:
        print(">> Rejecting Null Hypothesis <<")
        print(color.BOLD + "Significant Relationship" + color.END)


class color:
   BOLD = '\033[1m'
   END = '\033[0m'
print("===================================================================")
print(color.BOLD +"1) Chi Square Test for  Education and Coverage"+ color.END)
print("===================================================================")
Chi_Square_Test(df['Education'],df['Coverage'],0.95)
print("===================================================================")
print(color.BOLD +"2) Chi Square Test for  Education and EmploymentStatus"+ color.END)
print("===================================================================")
Chi_Square_Test(df['Education'],df['EmploymentStatus'],0.95)
print("===================================================================")
print(color.BOLD +"3) Chi Square Test for  EmploymentStatus and Gender"+ color.END)
print("===================================================================")
Chi_Square_Test(df['EmploymentStatus'],df['Gender'],0.95)
print("===================================================================")
print(color.BOLD +"4) Chi Square Test for  Location_Code and Marital_Status"+ color.END)
print("===================================================================")
Chi_Square_Test(df['Location_Code'],df['Marital_Status'],0.95)
print("===================================================================")
print(color.BOLD +"5) Chi Square Test for  Policy_Type and Policy"+ color.END)
print("===================================================================")
Chi_Square_Test(df['Policy_Type'],df['Policy'],0.95)
print("===================================================================")
print(color.BOLD +"6) Chi Square Test for  Policy_Type and Renew_Offer_Type"+ color.END)
print("===================================================================")
Chi_Square_Test(df['Policy_Type'],df['Renew_Offer_Type'],0.95)
print("===================================================================")
print(color.BOLD +"7) Chi Square Test for  Vehicle_Class and Renew_Offer_Type"+ color.END)
print("===================================================================")
Chi_Square_Test(df['Vehicle_Class'],df['Renew_Offer_Type'],0.95)
print("===================================================================")
print(color.BOLD +"8) Chi Square Test for  Vehicle_Class and Policy_Type"+ color.END)
print("===================================================================")
Chi_Square_Test(df['Vehicle_Class'],df['Policy_Type'],0.95)
print("===================================================================")
print(color.BOLD +"9) Chi Square Test for  Policy_Type and EmploymentStatus"+ color.END)
print("===================================================================")
Chi_Square_Test(df['Policy_Type'],df['EmploymentStatus'],0.95)
print("===================================================================")
print(color.BOLD +"10) Chi Square Test for  Vehicle_Class and Coverage"+ color.END)
print("===================================================================")
Chi_Square_Test(df['Vehicle_Class'],df['Coverage'],0.95)
print("===================================================================")
print(color.BOLD +"11) Chi Square Test for  Policy_Type and Coverage"+ color.END)
print("===================================================================")
Chi_Square_Test(df['Policy_Type'],df['Coverage'],0.95)
print("===================================================================")
print(color.BOLD +"12) Chi Square Test for  Education and Renew_Offer_Type"+ color.END)
print("===================================================================")
Chi_Square_Test(df['Education'],df['Renew_Offer_Type'],0.95)
