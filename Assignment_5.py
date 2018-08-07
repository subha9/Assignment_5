
# coding: utf-8

# In[4]:


#1. Write a function to compute 5/0 and use try/except to catch the exceptions.

def cal():
    return 5/0

try:
    cal()
except ZeroDivisionError:
    print("division error by zero!")
finally:
    print(' finally Executed')


# In[7]:


subjects=["Americans", "Indians"]
verbs=["Play", "watch"]
objects=["Baseball","cricket"]

sentence_lst = [(su+" "+ vb + " " + obj) for su in subjects for vb in verbs for obj in objects]
for sentence in sentence_lst:
 print (sentence)

