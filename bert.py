
# coding: utf-8

# In[ ]:


from google.colab import drive
drive.mount('/content/drive/')


# In[ ]:


get_ipython().run_line_magic('cd', '/content/drive/My Drive/colab')


# In[ ]:


get_ipython().run_line_magic('cd', 'bert')


# In[13]:


get_ipython().system('sh weibo_bert.sh')


# In[14]:


import os
import pandas as pd


if __name__ == '__main__':
    path = "weibo_output"
    pd_all = pd.read_csv(os.path.join(path, "test_results.tsv") ,sep='\t',header=None)

    data = pd.DataFrame(columns=['polarity'])
    print(pd_all.shape)

    for index in pd_all.index:
        negative_score = pd_all.loc[index].values[0]
        positive_score = pd_all.loc[index].values[1]

        if max(positive_score, negative_score) == negative_score:
            data.loc[index+1] = ["negative"]
        else:
            data.loc[index+1] = [ "positive"]

    data.to_csv(os.path.join(path, "pre_sample.tsv"),sep = '\t')

