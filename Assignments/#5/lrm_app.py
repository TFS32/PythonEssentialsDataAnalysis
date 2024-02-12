import lrm_rsme_other_way
"""
This is an application that call Linear Regression Model module

@author: Tiago Saraiva
@date: 2024-01-31
"""
# Creating 2 objects for Linear Regression Model class, one with values
# For slope and bias, other using default values
object_1 = lrm_rsme_other_way.LinRegModel()
object_2 = lrm_rsme_other_way.LinRegModel(-1, 4)
x_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y_list = [4, 3, 2, 1, 0, -1, -2, -3, -4, -5]

print(object_1)
print(object_2)

print("The predictions for the first object:\n",
      object_1.predict(x_list), "\n")
print("The predictions for the second object:\n",
      object_2.predict(x_list), "\n")

print("The root-mean-squared-error for the fisrt object:\n",
      lrm_rsme_other_way.rmse(y_list, object_1.predict(x_list)), "\n")
print("The root-mean-squared-error for the second object:\n",
      lrm_rsme_other_way.rmse(y_list, object_2.predict(x_list)), "\n")
