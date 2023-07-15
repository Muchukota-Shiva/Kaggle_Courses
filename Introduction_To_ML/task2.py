"""
this was run on the online code editor provided on kaggle, might show an error if ran without installing required libraries
"""

# What is the average lot size (rounded to nearest integer)?
avg_lot_size = home_data['LotArea'].mean().round()

# As of today, how old is the newest home (current year - the date in which it was built)
newest_home_age = 13

# Checks your answers
step_2.check()


#space


# print the list of columns in the dataset to find the name of the prediction target
home_data.describe()

y = home_data.SalePrice

# Check your answer
step_1.check()


#space


# Create the list of features below
feature_names = ['LotArea','YearBuilt','1stFlrSF','2ndFlrSF','FullBath','BedroomAbvGr','TotRmsAbvGrd']

# Select data corresponding to features in feature_names
X = home_data[feature_names]

# Check your answer
step_2.check()


#space


from sklearn.tree import DecisionTreeRegressor
#specify the model. 
#For model reproducibility, set a numeric value for random_state when specifying the model
iowa_model = DecisionTreeRegressor(random_state=2)

# Fit the model
iowa_model.fit(X,y)

# Check your answer
step_3.check()


#space


predictions = iowa_model.predict(X)
print(predictions)

# Check your answer
step_4.check()