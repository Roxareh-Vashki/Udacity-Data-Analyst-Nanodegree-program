#!/usr/bin/env python
# coding: utf-8

# In[1]:


# imports and load data
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
df = pd.read_csv('store_data.csv')
df.tail()


# In[ ]:


# explore data


# In[24]:


# sales for the last month
df.iloc[196:, 1:].sum().plot(kind='bar');


# In[26]:


# average sales
df.mean().plot(kind='barh');


# In[42]:


# sales for the week of March 13th, 2016
df[df['week'] == '2016-03-13'].plot(kind = 'bar');


# In[44]:


# share of sales for the latest 3-month periods
df_b = df[df['week'] >= '2017-12-01']
df_b.iloc[: , 1:].sum().plot(kind = 'bar');


# In[ ]:





# In[ ]:




