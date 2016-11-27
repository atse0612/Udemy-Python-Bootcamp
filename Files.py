
# coding: utf-8

# In[1]:

pwd


# In[4]:

f = open('Test File.txt')


# In[5]:

f.read()


# In[6]:

f.read()


# In[7]:

f.seek(0)


# In[8]:

f.read()


# In[9]:

f.seek(0)


# In[10]:

f.readlines()


# In[11]:

get_ipython().run_cell_magic('writefile', 'new.txt', 'First line\nSecond line')


# In[15]:

for lines in open('new.txt'):
    print(lines)


# In[17]:

for words in open('new.txt'):
    print(words)


# In[ ]:



