"""
this was run on the online code editor provided on kaggle, might show an error if ran without installing required libraries
"""

import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.indexing_selecting_and_assigning import *
print("Setup complete.")


#space


# Your code here
desc = reviews['description']

# Check your answer
q1.check()


#space


first_description = reviews.description.loc[0]

# Check your answer
q2.check()
first_description


#space


first_row = reviews.loc[0]

# Check your answer
q3.check()
first_row


#space


first_descriptions = reviews.description.loc[:9]

# Check your answer
q4.check()
first_descriptions


#space


sample_reviews = reviews.loc[[1,2,3,5,8]]

# Check your answer
q5.check()
sample_reviews


#space


df = reviews.loc[[0,1,10,100],['country','province','region_1','region_2']]

# Check your answer
q6.check()
df


#space


df = reviews.loc[0:99,['country','variety']]

# Check your answer
q7.check()
df


#space


italian_wines = reviews[reviews.country == 'Italy']

# Check your answer
q8.check()


#space


top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia', 'New Zealand'])) & (reviews.points >= 95)]

# Check your answer
q9.check()
top_oceania_wines