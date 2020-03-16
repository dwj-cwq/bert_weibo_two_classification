
# coding: utf-8

# In[43]:


import os
import pandas as pd

file_path = os.path.join('GLUE_DIR/WEIBO/', 'weibo_senti_100k.csv')
file = pd.read_csv(file_path, encoding = 'utf-8')
test_data = []
train_data = []
development_data = []
index_0 = 0
index_1 = 0


# In[44]:


print(test_data)


# In[45]:


for index, line in enumerate(file.values):
    if line[0] == 1 and index_1 < 1000:
        test_data.append(line)
        index_1 += 1
    if line[0] == 1 and index_1 >= 1000 and index_1 < 2000:
        development_data.append(line)
        index_1 += 1
    if line[0] == 0 and index_0 < 1000:
        test_data.append(line)
        index_0 += 1
    if line[0] == 0 and index_0 >= 1000 and index_0 < 2000:
        development_data.append(line)
        index_0 += 1
    else:
        train_data.append(line)


# In[47]:


print(line)
print(index_0)
print(index_1)
print(len(test_data))


# In[41]:


df = pd.DataFrame(train_data)
df.to_csv('GLUE_DIR/WEIBO/train_data.csv', index=False)
df = pd.DataFrame(test_data)
df.to_csv('GLUE_DIR/WEIBO/test_data.csv', index=False)
df = pd.DataFrame(development_data)
df.to_csv('GLUE_DIR/WEIBO/development_data.csv', index=False)


# In[42]:


print(len(file))
print(len(train_data))

