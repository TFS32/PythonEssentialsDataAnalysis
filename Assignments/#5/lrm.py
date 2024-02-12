import math
"""
This is a module with a Linear Regression Model

@author: Tiago Saraiva
@date: 2024-01-31
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
    for i, j in zip(x, y):
        z.append((i-j) ** 2)
    return math.sqrt(sum(z) / len(x))










