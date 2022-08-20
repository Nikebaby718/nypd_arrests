#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[2]:


nypd_arrest = pd.read_csv(r'C:\Users\13474\Downloads\NYPD_Arrest_Data__Year_to_Date_.csv')
nypd_arrest.shape


# In[ ]:


nypd_arrest.head(3)


# In[ ]:


nypd_arrest.dtypes


# In[ ]:


pip install geopy


# In[ ]:


from geopy.geocoders import Nominatim, ArcGIS
geocoders = Nominatim(user_agent='nypd_arrest')


# In[ ]:


# goal is to get address based on lat/long per index
addresses = Nominatim(user_agent='nypd_arrest').reverse((nypd_arrest.Latitude[1], nypd_arrest.Longitude[1]))


# In[3]:


addresses.address


# In[4]:


# this gives the full address details based on the index above
addresses.raw


# In[5]:


from geopy import distance


# In[10]:


#I want to check if "ARREST_KEY" is unique to a specific crime
# or if each arrest has a unique "ARREST_KEY"
nypd_arrest['ARREST_KEY'].duplicated()


# In[11]:


nypd_arrest["ARREST_DATE"]=pd.to_datetime(nypd_arrest["ARREST_DATE"])


# In[12]:


nypd_arrest.dtypes


# In[13]:


# A quick look at what the AGE_GROUP column contains
nypd_arrest['AGE_GROUP'].describe()
##nypd-arrest['AGE_GROUP']=pd.categorical(
    ##nypd_arrest['AGE_GROUP'], categories=[])


# In[14]:


#How much incidents by age group
nypd_arrest['AGE_GROUP'].value_counts()


# In[15]:


## This takes an account of the percentage of arrest type
## we multiply the answer by .001 >> round it three dec. place
## then add % sign to it using astype() method
offense_pct = nypd_arrest['Offense_Description'].value_counts().mul(.001).round(3).astype(str) + '%'
offense_pct


# In[16]:


nypd_arrest.filter(
    items=['Offense_Description', 'AGE_GROUP']
)


# In[17]:


# Creating a variable for women arrest
nypd_arrest.query('SEX=="F" ')
female_arrest = nypd_arrest.query('SEX=="F" ')


# In[18]:


# Let's see the age groups of these women that got arrested
female_arrest["AGE_GROUP"].value_counts()


# In[19]:


# Top 10 offenses women got arrested for
female_arrest["Offense_Description"].value_counts()[:10]


# In[20]:


#Female arrest in the borough of Brooklyn
#nypd_arrest['ARREST_BORO'].describe()
female_arrest.query('ARREST_BORO=="Staten Island"')[:10]


# In[21]:


f_over_65 = (
    nypd_arrest.query('SEX=="F" & AGE_GROUP=="65+"')
    .filter(items= ['PD_DESC','Offense_Description', 'Level_of_Offense', 'ARREST_BORO', 'RACE'])
)
f_over_65


# In[22]:


f_over_65.describe()


# In[23]:


# Male to Female ratio
M_to_F=nypd_arrest['SEX'].value_counts(normalize=True).mul(100).round(2).astype(str) + '%'
M_to_F


# In[24]:


labels = ['Female', 'Male']
colors = ['#Ee149f','#3f17e8']
sizes = [17.1, 82.9]
explode = (0, 0.1) # Explode male
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode,labels=labels, shadow=True, colors=colors,autopct='%1.1f%%')
ax1.axis('equal')
plt.show


# In[25]:


nypd_arrest.duplicated()


# In[26]:


# Checking to see if any duplicated rows in the dataframe
nypd_arrest.duplicated().sum()


# In[27]:


nypd_arrest["ARREST_PRECINCT"].value_counts()


# In[31]:


pip install folium


# In[ ]:




