
# coding: utf-8

# In[4]:

def square(num):
    result = num ** 2
    return result


# In[5]:

square(2)


# In[6]:

def square(num):
    return num**2


# In[7]:

square(4)


# In[8]:

def square(num): return num**2


# In[9]:

square(3)


# In[15]:

square2 = lambda num: num**2


# In[16]:

square2(10)


# In[17]:

# Check if a number is even


# In[23]:

even = lambda num: num%2 == 0


# In[24]:

even(4)


# In[25]:

def even(num):
    return num%2 == 0


# In[26]:

even(10)


# In[27]:

# Grabs the first character of the string


# In[28]:

first = lambda s: s[0]


# In[29]:

first('hello')


# In[30]:

rev = lambda s: s[::-1]


# In[31]:

rev('hello')


# In[32]:

def adder(x,y):
    return x+y


# In[33]:

adder(10,12)


# In[34]:

adder = lambda x,y: x+y


# In[35]:

adder(30,30)


# In[38]:

len_check = lambda item: len(item)


# In[39]:

len_check('how many chars does this string have')


# In[ ]:



