
# coding: utf-8

# In[1]:


fruits = {'banana':3,'apple':2, 'mango':1, 'kiwi':5}


# In[2]:


type(fruits)


# In[35]:


for key, value in fruits.items():
	print(value * key)


# In[40]:


fruits_list = [value * key]


# In[41]:


fruits_list

