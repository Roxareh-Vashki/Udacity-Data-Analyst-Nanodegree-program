

# In[1]:


import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
df_census = pd.read_csv('census_income_data.csv')
df_census.head()


# In[4]:


df_a = df_census[df_census['income'] == ' >50K']
df_b = df_census[df_census['income'] == ' <=50K']


# In[5]:


ind = df_a['education'].value_counts().index
df_a['education'].value_counts()[ind].plot(kind='bar');


# In[7]:


ind = df_b['education'].value_counts().index
df_b['education'].value_counts()[ind].plot(kind='bar');


# In[8]:


ind = df_a['workclass'].value_counts().index
df_a['workclass'].value_counts()[ind].plot(kind='pie', figsize=(8,8));


# In[10]:


df_a['age'].hist();


# In[12]:


df_a['age'].describe()


# In[13]:


df_b['age'].hist();


# In[14]:


df_b['age'].describe()

