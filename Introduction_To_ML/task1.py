"""
this was run on the online code editor provided on kaggle, might show an error if ran without installing required libraries
"""

# Set up code checking
from learntools.core import binder
binder.bind(globals())
from learntools.machine_learning.ex2 import *
print("Setup Complete")


#space


import pandas as pd

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

# Fill in the line below to read the file into a variable home_data
home_data = pd.read_csv(iowa_file_path)

# Call line below with no argument to check that you've loaded the data correctly
step_1.check()


#space


# Print summary statistics in next line
home_data.describe()

# What is the average lot size (rounded to nearest integer)?
avg_lot_size = home_data['LotArea'].mean().round()

# As of today, how old is the newest home (current year - the date in which it was built)
newest_home_age = 13

# Checks your answers
step_2.check()


#space


