
# coding: utf-8

# In[1]:

# Problem 1


# In[2]:

try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("An error ocurred!")


# In[3]:

# Problem 2


# In[4]:

x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("Can't divide by Zero!")
finally:
    print('All Done!')


# In[5]:

# Problem 3


# In[13]:

def ask():
    
    while True:
        try:
            n = input('Input an integer: ')
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break
            
        
    print('Thank you, you number squared is: '),n**2

       


# In[14]:

ask()


# In[15]:

ask()


# In[17]:

ask()


# In[ ]:



