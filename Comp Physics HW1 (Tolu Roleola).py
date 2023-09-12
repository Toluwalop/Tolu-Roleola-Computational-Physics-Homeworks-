#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Question 1)
name = "Toluwalope Roleola"
def myname(name):
    if len(name) > 0:
        return name
    
        
print(myname(name))
    
    


# In[5]:


#Question 2)
m = 5
v = 10
def Kinectic_Energy(m, v):
    KE = 0.5 *m* (v**2)
    return KE

print(Kinectic_Energy(m, v))


# In[6]:


#Question 3)
#Solving by hand, the answer is 0.7
(2.0 + 3*(1/2)) / 5


# In[ ]:


#Question 4)
'''the outputs of the code below should be 
5
5
 -5 10
'''


# In[7]:


x = 5
y = x
x +=1
print(y)
x=y
print(x)
y += x
x -= y
print(x,y)


# In[42]:


#Question 5)
print('x\tx\tx\tx\nx\tx\tx\tx\nx\tx\tx\tx\nx\tx\tx\tx')
#\t acts like the tab button and add extra space in front of the string


# In[28]:


#Question 6)
x = 4
y = 5
z = x
x = y
y = z


print(x)
print(y)

# x= y amd y = x does not work, because you python interpretes this as updataing the value of x with the value of y and then making y equal to that same value 


# In[ ]:


# Question 7) Give the type and value of the result of each expression or state when an error occurs:
a. 13 - 5 = 8 (integer)
b. 2.2 + 0.8 = 3.0 (float)
c. 5 * 4 = 20 (int)
d. 5.0 * 4 = 20.0 (float)
e. 12 // 3 = 4 (int)
f. 12.0 / 3 = 4.0 (float)
g. 5 * ‘a’ = error
h. ‘a’ + ‘b’ = error
i. ‘a’ + 1 = error
j. 5 % 2 = 1
k. 4 % 7 = 4
l. -4 % 7 = 3
m. (1 + 2) * (‘a’ + ‘b’) = error
n. ‘ab’ - ‘b’ = error
o. 5 / 0 = error

