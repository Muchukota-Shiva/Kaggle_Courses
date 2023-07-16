"""
this was run on the online code editor provided on kaggle, might show an error if ran without installing required libraries
"""

from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))


#space


# Import the train_test_split function and uncomment
from sklearn.model_selection import train_test_split

# fill in and uncomment
train_X, val_X, train_y, val_y = train_test_split(X,y,random_state=1)

# Check your answer
step_1.check()


#space


# You imported DecisionTreeRegressor in your last exercise
# and that code has been copied to the setup code above. So, no need to
# import it again

# Specify the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit iowa_model with the training data.
iowa_model.fit(train_X,train_y)

# Check your answer
step_2.check()


#space


# Predict with all validation observations
val_predictions = iowa_model.predict(val_X)

# Check your answer
step_3.check()


#space


# print the top few validation predictions
print(val_predictions)
# print the top few actual prices from validation data
print(val_y)


#space


from sklearn.metrics import mean_absolute_error
val_mae = mean_absolute_error(val_y,val_predictions)

# uncomment following line to see the validation_mae
print(val_mae)

# Check your answer
step_4.check()