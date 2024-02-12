class Employee():
    """This class contains employee data."""
    def __init__(self, id, name, income):
        self.name = name
        self.id = id
        self.income = income

    def income_taxes(self):
        """This function calculates taxes based on income."""
        rate = 0.20
        return rate * self.income
