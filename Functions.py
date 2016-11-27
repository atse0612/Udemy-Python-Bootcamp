
# coding: utf-8

# In[12]:

def my_addition_func(arg1,arg2):
    """
    Here is my doc string!
    """
    print(arg1+arg2)


# In[11]:

my_addition_func(1,2)


# In[13]:

def say_hello():
    print('hello')


# In[14]:

say_hello()


# In[19]:

def greeting(name):
    print("hello " + name)


# In[20]:

greeting('Jose')


# In[21]:

def add_num(num1,num2):
    return num1+num2


# In[22]:

x = add_num(2,3)


# In[23]:

x


# In[24]:

print(add_num(2,3))


# In[25]:

x = (add_num('one','two'))


# In[28]:

x


# In[48]:

def is_prime(num):
    """
    INPUT:A number
    OUTPUT:A print statement whether or not the number is prime.
    """
    for n in list(range(2,num)):
        if num % n == 0:
            print('Not Prime')
            break
    else:
        print('The number is Prime!')


# In[54]:

is_prime(12)


# In[53]:

list(range(2,12))


# In[ ]:



