
# coding: utf-8

# In[51]:

import pandas as pd


# In[52]:

from bs4 import BeautifulSoup as soup


# In[53]:

url = 'https://en.wikipedia.org/wiki/Benevolent_dictator_for_life'


# In[54]:

df = pd.read_html(url, header=0)


# In[57]:

bdfl = df[0]


# In[58]:

bdfl


# In[60]:

bdfl = bdfl[['Name','Project','Type']]


# In[61]:

bdfl


# In[ ]:



