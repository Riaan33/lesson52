import numpy as np
import pandas as pd
from mathplotlib import pyplot as plt

dataframe=pd.read_csv('countries_satellites.csv')
dataframe

top_5=dataframe.head(5)
print(top_5)
name=top_5['Countries/Organization Name']
number=top_5['Satellites In Orbit']

plt.xlabel('Countries/Organization Name')
plt.xticks(rotation='vertical')
plt.ylabel('Satellites In Orbit')

label=name
value=number

plt.bar(label,value, width=0.4, colors=('red','blue','green','pink','yellow'))