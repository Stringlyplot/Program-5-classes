class test:
    def __init__(self, value):
        self.value = value

    def test2(self):
        self.value = 3 + 2
        return self.value

location = 0
test1 = test(location)
location = test1.test2()
print(location)

def input_validate():
    
    pass


def input_validate(input_message, first_error, func_type= ""):
    while True:
        try:
            value = func_type(input(input_message))
            break
        except:
             print(first_error)
             pass
            
input_validate("Enter house model year: ", "Enter a vaild year\n", int)


"""while True:
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
"""