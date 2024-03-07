#!/usr/bin/env python
# coding: utf-8

# In[1]:


thislist = ["apple", "banana", "cherry"]
print(thislist)


# In[2]:


thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


# In[3]:


thislist = ["apple", "banana", "cherry"]
print(len(thislist))


# In[5]:


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)


# In[6]:


list1 = ["abc", 34, True, 40, "male"]

print(list1)


# In[7]:


mylist = ["apple", "banana", "cherry"]
print(type(mylist))


# In[8]:


thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# In[9]:


thislist = ["apple", "banana", "cherry"]
print(thislist[1])


# In[10]:


thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


# In[11]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


# In[12]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


# In[13]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


# In[14]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


# In[15]:


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# In[16]:


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# In[17]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


# In[18]:


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


# In[19]:


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


# In[20]:


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# In[21]:


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# In[22]:


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


# In[23]:


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# In[24]:


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# In[25]:


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# In[26]:


thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)


# In[27]:


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# In[28]:


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


# In[29]:


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# In[33]:


thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)


# In[34]:


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# In[35]:


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


# In[36]:


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


# In[37]:


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


# In[38]:


thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


# In[39]:


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


# In[40]:


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


# In[41]:


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


# In[42]:


thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


# In[43]:


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


# In[44]:


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


# In[45]:


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


# In[46]:


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


# In[47]:


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# In[48]:


thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


# In[49]:


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# In[50]:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


# In[51]:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


# In[53]:


fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)


# In[54]:


a = ["apple", "banana", "cherry"]

b = ["Ford", "BMW", "Volvo"]

a.append(b)

print(a)


# In[55]:


fruits = ["apple", "banana", "cherry"]

fruits.clear()

print(fruits)


# In[56]:


fruits = ["apple", "banana", "cherry"]

x = fruits.count("cherry")

print(x)


# In[57]:


points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)

print(x)


# In[58]:


fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)


# In[59]:


fruits = ['apple', 'banana', 'cherry']

points = (1, 4, 5, 9)

fruits.extend(points)

print(fruits)


# In[60]:


fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)


# In[61]:


fruits = [4, 55, 64, 32, 16, 32]

x = fruits.index(32)

print(x)


# In[62]:


fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)


# In[63]:


fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)

print(fruits)


# In[64]:


fruits = ['apple', 'banana', 'cherry']

x = fruits.pop(1)

print(x)


# In[65]:


fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)


# In[ ]:




