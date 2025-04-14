class house:
    #This sets up all the varaibles that will describe our object/ input values
    def __init__(self, location, current_price, year_built=0, original_price=0):
        self.year_built
        self.original_price
        self.location
        self.current_price
    #This will caclulate the current value of the house
    def current_value(self):
        current_value = self.original_price(1 + .08)^self.house_age

