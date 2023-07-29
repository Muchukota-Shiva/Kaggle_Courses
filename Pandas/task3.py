"""
this was run on the online code editor provided on kaggle, might show an error if ran without installing required libraries
"""

import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.summary_functions_and_maps import *
print("Setup complete.")

reviews.head()


#space


median_points = reviews.points.median()

# Check your answer
q1.check()


#space


countries = reviews.country.unique()

# Check your answer
q2.check()


#space


reviews_per_country = reviews.country.value_counts()

# Check your answer
q3.check()


#space


centered_price = reviews.price - reviews.price.mean()

# Check your answer
q4.check()


#space


bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']

# Check your answer
q5.check()


#space


n_trop=reviews.description.map(lambda desc:"tropical" in desc).sum()
n_fruity=reviews.description.map(lambda desc:"fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

# Check your answer
q6.check()


#space


def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns')

# Check your answer
q7.check()