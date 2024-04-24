import csv # replaced with pandas
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv('data.csv')
ids = data['Responder_id']
# get only programming languages column
lang_responses = data['LanguagesWorkedWith']

# counter class keeps count of how many times 
# it recieved an entry of same value
language_counter = Counter()
# split programming languages on ; to get a list
for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []
# Counter can return given number of highest repeated values
for item in language_counter.most_common(15):
    # it returns a tuple of language and count,
    # so we need to extract each in separate list
    languages.append(item[0])
    popularity.append(item[1])

# so the plot will be top down
languages.reverse()
popularity.reverse()

# horizontal bar
plt.barh(languages, popularity) 

plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use")

plt.tight_layout()

plt.savefig('plot_horizontal_bar.png')

plt.show()
