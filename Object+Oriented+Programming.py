
# coding: utf-8

# In[1]:

l = [1,2,3]


# In[2]:

l.count(2)


# In[3]:

# OBJECTS


# In[4]:

1


# In[5]:

type([1,2,3])


# In[6]:

type({'k1':1})


# In[7]:

def square(num):
    return num**2


# In[8]:

type(square)


# In[9]:

# Classses Lecture 2


# In[10]:

class Sample(object):
    pass


# In[11]:

x = Sample()


# In[13]:

type(x)


# In[41]:

class Dog(object):
    
    # Class Object Attribute
    species = 'mammal'
    
    def __init__(self,breed,name,fur=True):
        self.breed = breed
        self.name = name
        self.fur = fur


# In[42]:

sam = Dog(breed = 'Huskie', name = 'Sammy', fur = False)


# In[43]:

sam.breed


# In[44]:

sam.species


# In[46]:

sam.name


# 

# sam.fur

# In[47]:

sam.fur


# In[1]:

# METHODS LECTURE 3


# In[60]:

class Circle(object):
    
    # class object attributes
    pi = 3.14
    
    
    def __init__(self,radius=1):
        self.radius = radius
        
    def area(self):
        # radius**2 * pi
        return (self.radius**2) * Circle.pi
    
    def set_radius(self,new_radius):
        """
        This method takes in a radius and resets the current radius of the Circle 
        """
        self.radius = new_radius
        
    def get_radius(self):
        return self.radius
    
    


# In[61]:

c = Circle(radius=10)


# In[62]:

c.pi


# In[63]:

c.radius


# In[64]:

c.pi


# In[65]:

c.area()


# In[66]:

c.set_radius(10)


# In[67]:

c.radius


# In[68]:

c.get_radius()


# In[69]:

# Lecture 4 Inheritance


# In[80]:

class Animal(object):
    
    def __init__(self):
        print("Animal Created")
        
    def whoAmI(self):
        print("Animal")
        
    def eat(self):
        print("Eating")


# In[81]:

a = Animal()


# In[82]:

class Dog(Animal):
    
    def __init__ (self):
        Animal.__init__(self)
        print("Dog created")
    
    def whoAmI(self):
        print('Dog')
        
    def bark(self):
        print("Woof!")


# In[83]:

d = Dog()


# In[85]:

d.whoAmI()


# In[86]:

# Lecture 5 Special Objects


# In[87]:

l = [1,2,3]


# In[88]:

print(l)


# In[89]:

len(l)


# In[106]:

class Book(object):
    def __init__(self,title,author,pages):
        
        
        print("A book has been created!")
        self.title = title
        self.author = author
        self.pages = pages
        
        
    def __str__(self):
        
         return "Title:%s , Author:%s, Pages:%s " %(self.title, self.author, self.pages)
        
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book is gone!")


# In[107]:

b=Book('Python','Jose','101')


# In[108]:

print(b)


# In[109]:

del(b)


# In[ ]:




# In[ ]:



