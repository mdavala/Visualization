
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


# In[3]:


np.random.seed(42)
random_x = np.random.randint(1,100, (10,10))
random_y = np.random.randint(1,100, (10,10))


# In[9]:


data = [go.Scatter(x=random_x,
                  y=random_y,
                  mode = 'markers',
                  )]


# In[10]:


layout = go.Layout (title='My first plotly graph',
                   xaxis = dict(title='X-axis'),
                   yaxis = dict(title='Y-axis'),
                   )


# In[11]:


fig = go.Figure (data=data, layout=layout)


# In[12]:


pyo.plot (fig, filename='scatter_plot.html')


# In[ ]:


marker = dict(
                      size = 12,
                      color = 'rgb(51, 204,153)',
                      symbol = 'pentagon',
                      line = {'width':2}
                  )


# In[ ]:


hovermode = 'closest'

