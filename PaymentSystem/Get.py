from firebase import firebase
firebase = firebase.FirebaseApplication('https://customer-database-b3374.firebaseio.com/', None)
result = firebase.get('/License Plates', None)
print (result)
