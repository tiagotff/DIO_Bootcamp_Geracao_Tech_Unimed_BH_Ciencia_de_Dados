# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DxPx7jCtJhVGTYgGVClS982GM3_RBXye
"""

#Bibliotecas
import pandas as pd

url1 = 'https://raw.githubusercontent.com/Muralimekala/python/master/Resp2.csv'

df1 = pd.read_csv(url1)
df1.head()

url2 = 'https://raw.githubusercontent.com/Muralimekala/python/master/Salaries.csv'

sf = pd.read_csv(url2)
sf.head()

#Luigi
!pip install luigi

import luigi

luigi