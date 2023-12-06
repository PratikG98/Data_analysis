#!/usr/bin/env python
# coding: utf-8

# # Apple iphone Sales Analysis Project

# In[100]:


#Analyzing the data of top 10 iphones based on rating

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv('apple_products.csv') # reading csv file
print(data.head(5))

#checking for null and missing vals

print(data.isnull().sum()) # clean data

#checking the stats of data

print(data.describe())

#comparing the no. of ratings of top 10 iphones 

highest_rated = data.sort_values(by=['Star Rating'],ascending = False) #sorting phones based on star rating 
highest_rated_10=highest_rated.head(10) #finding top 10 iphones
print(highest_rated_10['Product Name'])

iphones = highest_rated_10['Product Name'].value_counts()
label = iphones.index
counts = highest_rated_10['Number Of Ratings']
figure1 = px.bar(highest_rated_10,x=label,y=counts,
                title = 'Number of ratings of top 10 highest rated iphones' )
#figure.update_layout(xaxis_title='iphones') #hiding the additional x label
figure1.show()

#comparing the no. of reviews of top 10 iphones 

counts_r = highest_rated_10['Number Of Reviews']
figure2 = px.bar(highest_rated_10,x=label,y=counts_r,
                title = 'Number of reviews of top 10 highest rated iphones' )
figure2.show()

#comparing the sales price of iphones with number of ratings and the trend

figure3 = px.scatter(data_frame = data , x = 'Number Of Ratings' , y = 'Sale Price' ,
                    size = 'Discount Percentage' , trendline = 'ols' ,
                    title = 'Relationship between Sale Price and Number of Ratings')
figure3.show()

#comparing the discount percentage of iphones with number of ratings and the trend

figure4 = px.scatter(data_frame = data , x = 'Number Of Ratings' , y = 'Discount Percentage' ,
                    size = 'Sale Price' , trendline = 'ols' ,
                    title = 'Relationship between Discount Percentage and Number of Ratings')
figure4.show()


# In[92]:


figure = px.bar(highest_rated_10,x='Product Name',y=counts,
                labels={'Product Name' : 'iphones'},
                title = 'Number of ratings of top 10 highest rated iphones' )
figure.show()


# In[89]:


df_final = pd.DataFrame(columns=['labels_data'])
df_final['labels_data'] = label.format()
print(type(final_labels),final_labels)
figure = px.bar(df_final,x='labels_data',y=counts,
                labels={'labels_data' : 'iphones'},
                title = 'Number of ratings of top 10 highest rated iphones' )
figure.show()


# In[94]:


data


# In[ ]:




