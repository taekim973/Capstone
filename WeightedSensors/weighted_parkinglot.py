import random
import math

class parking_lot:
    def __init__(self, num_spaces, status):
        self.num_spaces = num_spaces
        self.status = status

    def open_spaces(self, free_spaces):
        free_spaces = self.num_spaces

class vehicle:
    def __init__(self, weight): #, ticket_number, ticket_status):
        self.weight = weight
        #self.ticket_number = ticket_number
        #self.ticket_status = ticket_status

    def parking_options(self, weight):       
        if self.weight > 30: # Indicates that it is a a vehicle, not for e.g. a person
            print("Hello, welcome to Capstone parking lot")
            override_suggestion = str(input("Do you wish to ignore the suggested nearest parking suggestion? Yes\n1. No\n2. "))
            if overrride_suggestion == "1" or override_suggestion.lower() == "yes":
                print("Proceed to your incictaed empty parking spot")
                lot_number = random.randrange(1,16) # There are 16 parking spots
            else:
                print("Proceed to the indicated nearest parking spot")
                lot_number = random.choice(tickets) # for now, algorithm for nearest parking spot using AI should be implemented later
            return lot_number
        

class parking_spot:
    def __init__(self, weight_of_spot, status):
        self.weight_of_spot = weight_of_spot
        self.status = status

    def evaluate_weight(self, weight_of_spot, status, light):
        if weight_of_spot > 30:
            status = "Taken"
            light = "Red"
        else:
            status = "Empty"
            light = "Green"
        return status + Green
    
