class Train: # is a class
    owned_by = "paskistan Railway" # class attribute
    def __init__(self, name, driver, engin_type, start_junction, end_junction): # constructor method
        self.name = name # instance attribute
        self.driver = driver # instance attribute
        self.engin_type = engin_type # instance attribute
        self.start_junction = start_junction # instance attribute
        self.end_junction = end_junction # instance attribute

ghouri_express = Train("Ghouri Express", "Usama", "locomotive", "faisalabad", "lahore")
baddar_express = Train("Baddar Express", "Shanzy", "locomotive", "lahore", "faisalabad")
green_line_express = Train("Green Line Express", "Nouman", "locomotive", "margilla", "karachi")
print(ghouri_express.name)  # Output: Ghouri Express is o
print(baddar_express.driver)  # Output: Shanzy
print(green_line_express.engin_type)  # Output: locomotive
print(ghouri_express.start_junction)  # Output: faisalabad
print(baddar_express.end_junction)  # Output: faisalabad
print(green_line_express.owned_by)  # Output: paskistan Railway 

print(ghouri_express.owned_by)  # Output: paskistan Railway 





''' ------------------------ instance method ------------------------ '''
class Passenger_train: # is a class

    def show_name(self, name): # instance method
        self.name = name # instance attribute

passenger_train = Passenger_train()
passenger_train.show_name("Ghouri Express")
print(passenger_train.name)  # Output: Ghouri Express        
''' ------------------------ class method ------------------------ '''
class Passenger_train:
    train_name = "Ghouri Express" # class attribute

    @classmethod # decorator for class method
    def show_train_info(cls): # class method
        print(f"Train Name: {cls.train_name}") 
Passenger_train.show_train_info()  # Output: Train Name: Ghouri Express


''' ------------------------ static method ------------------------ '''
class Passenger_train: # is a class
    @staticmethod # decorator for static method
    def show_train_info(): # static method
        print("This is a passenger train.")
Passenger_train.show_train_info()  # Output: This is a passenger train.
















































