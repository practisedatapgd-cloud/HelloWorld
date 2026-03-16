#!/usr/bin/env python
# coding: utf-8

# In[3]:


from IPython.display import Image
import pandas as pd


# In[2]:


Image(url='https://tse4.mm.bing.net/th/id/OIP.s9yEtqXfsRdCeM-39octmgHaGI?rs=1&pid=ImgDetMain&o=7&rm=3')


# In[4]:


df = pd.read_csv('http://bit.ly/titanic-vis-ml')


# In[7]:


print(df.shape)
df.head(10)


# In[8]:


df.tail(1)


# In[10]:


df.loc[0:2,['Name','Age']].head()


# In[11]:


names = df.Name
ages = df['Age']
print(names)
print(ages)


# In[12]:


type(df)


# In[15]:


print(df.iloc[5,1:4])
df.iloc[:3,:]


# In[25]:


first_name=df.iloc[1,3:4]
print(first_name)


# In[ ]:


df_manual=pd.DataFrame(columns=['a','b','c'],data=[[1,2,3],[4,5,6]])


# In[26]:


df.describe()


# In[28]:


df.Age.describe(percentiles=[.25,.5,.75,.95,.99])


# In[ ]:


df.describe(i)

