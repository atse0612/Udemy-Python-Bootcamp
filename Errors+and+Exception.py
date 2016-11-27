
# coding: utf-8

# In[5]:

try:
    2 + 's'
except TypeError:
    print("There was a type error!")
finally:
    print('Finally this was printed')


# In[6]:

try:
    2 + 's'
except:
    print("There was a type error!")
finally:
    print('Finally this was printed')


# In[12]:

try:
    f = open('testfile1232','w')
    f.write('Test write this file')
except:
    print('Error in writing to the file!')
else:
    print('File write was a success')


# In[13]:

try:
    f = open('testfile1232','e')
    f.write('Test write this file')
except:
    print('Error in writing to the file!')
else:
    print('File write was a success')


# In[16]:

try:
    f = open('testfile1232','w')
    f.write('Test write this')
finally:
    print("Always execute finally code blocks!")


# In[17]:

try:
    f = open('testfile1232','w')
    f.write('Test write this')
except:
    print('There was an error!')
finally:
    print("Always execute finally code blocks!")


# In[29]:

def askint():
    try: 
        val = int(input('Please enter an integer: '))
    except:
        print('Looks like you did not enter an integer!')
        val = int(input("Try again- Please enter an integer: "))
    finally:
        print('Finally block executed!')
    print(val)    


# In[30]:

askint()


# In[31]:

askint()


# In[32]:

def askint():
    
    while True:
        try:
            val = int(input('Please enter an integer: '))
            
        except:
            print("Looks like you didn't enter an integer!")
            continue
        else:
            print('Correct, that is an integer!')
        finally:
            print('Finally block executed')
        print(val)
    
    
    


# In[ ]:

askint()


# In[ ]:



