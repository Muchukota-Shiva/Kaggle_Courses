"""
this was run on the online code editor provided on kaggle, might show an error if ran without installing required libraries
"""

# Your code here
reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()

# Check your answer
q1.check()


#space


best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()

# Check your answer
q2.check()


#space


price_extremes = reviews.groupby('variety').price.agg([min,max])

# Check your answer
q3.check()


#space


price_extremes = reviews.groupby('variety').price.agg([min,max])
sorted_varieties = price_extremes.sort_values(by=['min','max'], ascending=False)

# Check your answer
q4.check()


#space


reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()

# Check your answer
q5.check()


#space


country_variety_counts = reviews.groupby(['country','variety']).size().sort_values(ascending=False)

# Check your answer
q6.check()