from datetime import datetime
current_year = datetime.now().year


class house:
    #This sets up all the varaibles that will describe our object/ input values
    def __init__(self, location = "none", year_built=0, original_price=0):
        self.location = location
        self.year_built = year_built
        self.original_price = original_price
    #This will caclulate the current value of the house
    #methods what the object(house choice) can do
    def current_value(self):
        #calculates the age of the house
        house_age = current_year - self.year_built
        #calculates the original price of the house when first built
        self.current_value = self.original_price*(1 + .08)**house_age
        print("Current Value Of House:", round(self.current_value, 2))
        return self.current_value
    

    def money_earned(self):
        profit = self.current_value - self.original_price
        print("Total Value You Will Earn:", round(profit, 2))
        return profit
    
class input_validation:
    def __init__(self, value, error_message):
        self.value = value
        self.error_message = error_message

    def format(self):
        while True:
            try:
                self.value = "tell"
                pass
            except:
                pass
        pass
#same as above
while True:
    try:
        location = str(input("Location: "))
        break
    except:
        print("Enter valid location\n")
#same as above
while True:
    #checks if code runs correctly
    try:
        year_created = int(input("Enter house model year: "))
        #checks if year_created is not above the date made
        if year_created > current_year:
            print("Invalid input try again\n")
        else:
            break
    except:
        print("Enter valid year\n")

#loop checks if item is valid/ input validation
while True:
    #checks to see if this code runs fine
    try: 
        price = float(input("\nEnter price of the house: "))
        if price < 0:
            print("Invalid number\n")
        else:
            break
    # If not this pops up
    except:
        print("Enter a number please\n")   

print(f"\nHouse information: \nyear built: {year_created}\nPurchase Price: {price}\nLocation: {location}\n")
house1 = house(location, year_created, price)
house1.current_value()
house1.money_earned()



