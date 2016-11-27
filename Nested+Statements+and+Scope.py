
# coding: utf-8

# In[4]:

x = 25

def printer():
    x = 50
    return x

print(x)


# In[6]:

print(printer())


# In[7]:

# Local


# In[8]:

# x is local here:
f = lambda x:x**2


# In[9]:

# Enclosing Function Locals


# In[11]:

name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'
    
    def hello():
        print('Hello '+name)
    
    hello()

greet()


# In[12]:

print(name)


# In[13]:

len


# In[15]:

x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)


# In[16]:

x = 50

def func():
    global x
    print('This function is now using the global x!')
    print ('Because of global x is: ', x)
    x = 2
    print ('Ran func(), changed global x to', x)

print ('Before calling func(), x is: ', x)
func()
print ('Value of x (outside of func()) is: ', x)


# In[ ]:



