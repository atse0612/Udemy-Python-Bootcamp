
# coding: utf-8

# In[3]:

# Computing the volume of a sphere


# In[4]:

def vol(rad):
    return(4.0/3)*(3.14)*(rad**3)


# In[5]:

# Checking to see if a number in range


# In[6]:

def ran_check(num,low,high):
    #Check if num is between low and high (including low and high)
    if num in range(low,high+1):  
        print(" %s is in the range" %str(num))  
    else :  
        print("The number is outside the range.")


# In[7]:

# Return Boolean


# In[8]:

def ran_bool(num,low,high):
    return num in range(low,high+1)


# In[9]:

ran_bool(3,1,10)


# In[10]:

def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])


# In[11]:

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


# In[12]:

# New Functions


# In[13]:

def unique_list(l):
    # Also possible to use list(set())
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x


# In[14]:

unique_list([1,1,1,1,2,2,3,3,3,3,4,5])


# In[15]:

def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  


# In[16]:

multiply([1,2,3,-4])


# In[17]:

# Palindrome


# In[18]:

def palindrome(s):
    
    s = s.replace(' ','') # This replaces all spaces " " with no space ''. (Fixes issues with strings that have spaces)
    return s == s[::-1] # Check through slicing


# In[19]:

palindrome('nurses run')


# In[20]:

palindrome('abcba')


# In[21]:

import string

def ispangram(str1, alphabet=string.ascii_lowercase):  
    alphaset = set(alphabet)  
    return alphaset <= set(str1.lower())  


# In[22]:

ispangram("The quick brown fox jumps over the lazy dog")


# In[23]:

string.ascii_lowercase


# In[ ]:



