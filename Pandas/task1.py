"""
this was run on the online code editor provided on kaggle, might show an error if ran without installing required libraries
"""

import pandas as pd
pd.set_option('display.max_rows', 5)
from learntools.core import binder; binder.bind(globals())
from learntools.pandas.creating_reading_and_writing import *
print("Setup complete.")


#space


# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.
fruits = pd.DataFrame({'Apples':[30] , 'Bananas':[21]})

# Check your answer
q1.check()
fruits


#space


# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruit_sales.
fruit_sales = pd.DataFrame({'Apples':[35,41] , 'Bananas':[21,34]}, index=['2017 Sales','2018 Sales'])

# Check your answer
q2.check()
fruit_sales


#space


ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')

# Check your answer
q3.check()
ingredients


#space


reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col=0)

# Check your answer
q4.check()
reviews


#space


# Your code goes here
animals.to_csv('cows_and_goats.csv')
# Check your answer
q5.check()