import math
"""
Created on Fri Feb  9 14:11:09 2024

@author: tiago
"""
class LinRegModel:
    """
    Linear Regression Model class
    """

    def __init__(self, slope=0, bias=0):
        self.slope = slope
        self.bias = bias

    def __repr__(self):
        a = '************************\n'
        b = "Model parameters:\n"
        c = f"Slope: {self.slope}\n"
        d = f"Bias: {self.bias}\n"
        return a + b + c + d + a

    def predict(self, x):
        """
        Receiving a list and predicting with linear regression
        """
        y = []
        for i in x:
            y.append(self.slope * i + self.bias)
        return y


def rmse(x, y):
     """
     Root-mean-squared-error function
     """
     z = []
     for i in range(len(x)):
         z.append((x[i]-y[i]) ** 2)
     return math.sqrt(sum(z) / len(x))

       