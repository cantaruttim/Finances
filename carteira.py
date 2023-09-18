#!/usr/bin/env python
# coding: utf-8

# In[6]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import pandas as pd


# In[4]:


link = 'https://fundamentus.com.br/resultado.php'
url = requests.get(link)

# confirma se houve conexão com o site em questão
if url.status_code == 200:
    print('Conexão realizada com sucesso!')
else:
    print("Conexão não realizada com sucesso!")


# In[12]:


link2 = 'https://fundamentus.com.br/resultado.php'

# Abrindo o navegador
navegador = webdriver.Chrome()
navegador.get(link2)
time.sleep(5)


# In[13]:


table = navegador.find_element(By.ID,
                'resultado').text


# In[14]:


print(table)


# In[ ]:





# In[ ]:




