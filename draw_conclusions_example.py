


import pandas as pd
df = pd.read_csv('cancer_data.csv')
df


# In[2]:


df_m = df[df['diagnosis'] == 'M']
df_m.head()


# In[4]:


mask = df['diagnosis'] == 'M'
df_m = df[mask]
df_m


# In[6]:


df_m['area_mean'].describe()


# In[7]:


df_b = df[df['diagnosis'] == 'B']
df_b['area_mean'].describe()


# In[9]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

fig, ax = plt.subplots(figsize =(8,6))
ax.hist(df_b['area_mean'], alpha=0.5, label='benign')
ax.hist(df_m['area_mean'], alpha=0.5, label='malignant')
ax.set_title('Distributions of Benign and Malignant Tumor Areas')
ax.set_xlabel('Area')
ax.set_ylabel('Count')
ax.legend(loc='upper right')
plt.show();


# In[ ]:




