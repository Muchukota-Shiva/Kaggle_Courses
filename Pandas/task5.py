"""
this was run on the online code editor provided on kaggle, might show an error if ran without installing required libraries
"""

# Your code here
dtype = reviews.points.dtype

# Check your answer
q1.check()


#space


point_strings = reviews.points.astype(str)

# Check your answer
q2.check()


#space


missing = reviews[reviews.price.isnull()]
n_missing_prices = len(missing)

# Check your answer
q3.check()


#space


reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)

# Check your answer
q4.check()