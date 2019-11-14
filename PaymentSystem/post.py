from firebase import firebase
import json
firebase = firebase.FirebaseApplication('https://customer-database-b3374.firebaseio.com/', None)

name = input("Please enter fullname :")
email = input("Please enter email address: ")
plate = input("Please enter license plate number: ")

data = { 'License Plate': plate  , 'email': email, 'name': name}

result = firebase.post('/License Plates', data)
