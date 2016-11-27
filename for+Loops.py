
# coding: utf-8

# In[1]:

l = [1,2,3,4,5]


# In[2]:

l


# In[5]:

for element in l:
    print(element)


# In[8]:

for num in l:
    print('something!')


# In[9]:

# MODULO


# In[10]:

10%3


# In[11]:

18%7


# In[12]:

4%2


# In[13]:

15%19


# In[14]:

7%2


# In[15]:

l


# In[16]:

for num in l:
    if num % 2 == 0:
        print(num)


# In[17]:

for num in l:
    if num % 2 == 1:
        print(num)


# In[19]:

for num in l:
    if num % 2 == 0:
        print('Here is a an even')
    else:
        print('Odd number!')


# In[20]:

for num in l:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd number!')


# In[21]:

l


# In[23]:

list_sum = 0


for num in l:
    list_sum = list_sum + num
    
print(list_sum)    


# In[24]:

list_sum = 0


for num in l:
    list_sum += num
    
print(list_sum)    


# In[25]:

s = 'This is a string'


# In[26]:

for item in s: 
    print(item)


# In[27]:

tup = (1,2,3,4,5)

for t in tup:
    print(t)


# In[28]:

tup = (1,2,3,4,5)

for item in tup:
    print(item)


# In[29]:

l = [(2,4),(6,8),(10,12)]


# In[30]:

l


# In[31]:

l[0]


# In[32]:

l[0][0]


# In[33]:

l[1][1]


# In[34]:

l[2][0]


# In[36]:

for tup in l:
    print(tup)


# In[37]:

for (t1,t2) in l:
    print(t1)


# In[44]:

for (t1,t2) in l:
    print(t1 - t2)


# In[45]:

for (t1,t2) in l:
    print(t2+t1)


# In[41]:

d = {'k1':1,'k2':2,'k3':3}


# In[42]:

d


# In[43]:

for item in d:
    print(item)


# In[53]:

for (k,v) in d.iteritems():
    print (k)
    print (v)


# In[ ]:



