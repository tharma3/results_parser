
# coding: utf-8

# In[1]:

import pandas as pd


# In[3]:

import json


# In[4]:

import requests


# In[5]:

url = 'https://int.nyt.com/applications/elections/2017/api/1/races/2017-11-07.json'


# In[21]:

race_id = 'va-47225-2017-11-07'


# In[7]:

json_blob = requests.get(url)


# In[8]:

blob = json.loads(json_blob.text)


# In[102]:

print blob['races'][race_index]


# In[12]:

race_id_dict = {}


# In[13]:

for item in range(len(blob['races'])):
    race_id = blob['races'][item]['race_id']
    votes = blob['races'][item]['votes']
    race_id_dict[race_id] = votes


# In[24]:

race_id_df = pd.DataFrame.from_dict(race_id_dict, orient='index')


# In[34]:

race_id_df = race_id_df.reset_index()


# In[36]:

race_id_df.columns = ['race_id', 'total_votes']


# In[37]:

race_id_df.head()


# In[38]:

race_id_df[race_id_df['race_id']==race_id]


# In[46]:

race_index = next(index for (index, d) in enumerate(blob['races']) if d["race_id"]==race_id)


# In[47]:

print race_index


# In[70]:

blob['races'][race_index]['counties'][0]


# In[50]:

candidate_results_dict = {}


# In[61]:

for item in range(len(blob['races'][race_index]['candidates'])):
    candidate = blob['races'][race_index]['candidates'][item]['candidate_key']
    votes = blob['races'][race_index]['candidates'][item]['votes']
    candidate_results_dict[candidate] = votes


# In[62]:

candidate_votes_df = pd.DataFrame.from_dict(candidate_results_dict, orient='index')


# In[64]:

candidate_votes_df = candidate_votes_df.reset_index()


# In[65]:

candidate_votes_df.columns = ['candidate_key','votes']


# In[66]:

candidate_votes_df


# In[71]:

county_results_dict = {}


# In[77]:

county_gillespie_dict = {}


# In[78]:

county_northam_dict = {}


# In[79]:

county_hyra_dict = {}


# In[76]:

blob['races'][race_index]['counties'][item]['results'][u'gillespiee']


# In[82]:

for item in range(len(blob['races'][race_index]['counties'])):
    county = blob['races'][race_index]['counties'][item]['name']
    total_votes = blob['races'][race_index]['counties'][item]['votes']
    gillespie_votes = blob['races'][race_index]['counties'][item]['results'][u'gillespiee']
    northam_votes = blob['races'][race_index]['counties'][item]['results'][u'northamr']
    hyra_votes = blob['races'][race_index]['counties'][item]['results'][u'hyrac']
    county_results_dict[county] = total_votes
    county_gillespie_dict[county] = gillespie_votes
    county_northam_dict[county] = northam_votes
    county_hyra_dict[county] = hyra_votes


# In[83]:

list_of_dicts = [county_results_dict, county_gillespie_dict, county_northam_dict, county_hyra_dict]


# In[89]:

county_votes_df = pd.DataFrame.from_dict(county_results_dict, orient='index')


# In[91]:

county_votes_df = county_votes_df.reset_index()


# In[92]:

county_votes_df.columns = ['county','total_votes']


# In[93]:

county_votes_df['gillespie'] = county_votes_df['county'].map(county_gillespie_dict)


# In[94]:

county_votes_df['northam'] = county_votes_df['county'].map(county_northam_dict)


# In[95]:

county_votes_df['hyra'] = county_votes_df['county'].map(county_hyra_dict)


# In[96]:

county_votes_df.head()


# In[ ]:



