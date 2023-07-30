"""
this was run on the online code editor provided on kaggle, might show an error if ran without installing required libraries
"""

# Your code here
renamed = reviews.rename(columns={'region_1':'region','region_2':'locale'})

# Check your answer
q1.check()


#space


reindexed = reviews.rename_axis('wines', axis='rows')

# Check your answer
q2.check()


#space


combined_products = pd.concat([gaming_products, movie_products])

# Check your answer
q3.check()


#space


powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))

# Check your answer
q4.check()