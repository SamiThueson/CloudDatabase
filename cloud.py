import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

# Setup Google Cloud Key - The json file is obtained by going to
# Project Settings, Service Accounts, Create Service Account, and then
# Generate New Private Key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]  = "private_key.json"


# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'cloud-database-60d3f',
})

db = firestore.client()  # this connects to our Firestore database


def display_doc(db):
    '''Displays the chosen document'''
    name = input("Enter a city name: ")

    # Make sure that the city does exists in the database
    result = db.collection('places').document(name).get()
    if not result.exists:
      print("Item does not exist!")
      return

    # Display the results of the query
    doc = db.collection('places').document(name)
    res = doc.get().to_dict()
    print(res)    

def insert_doc(db):
    '''This creates/inserts into the collection'''
    name = input("Please enter city name: ")
    lat = input("Latitude: ")
    long = input("Longtitude: ")
    where_to_go = input("Where to go: ")

    # Check to make sure it doesn't already exists!
    result = db.collection("places").document(name).get()
    if result.exists:
      print("Item already exists!")
      return

    # Build a dictionary
    city = {"lat": lat,
            "long": long,
            "where_to_go": where_to_go}

    # Insert the city
    db.collection('places').document(name).set(city)
    
def modify_doc(db):
    '''Modifies a specified document'''
    name = input("Enter a city name: ")
    field = input("Field to be updated (lat, long, or where_to_go): ")
    value = input("Update information: ")

    # Make sure that the city does exists in the database
    result = db.collection('places').document(name).get()
    if not result.exists:
      print("Item does not exist!")
      return

    # Update the field
    db.collection('places').document(name).update({
        field : value
    })

def add_field(db):
    '''Add a single field to a document'''
    name = input("Enter a city name: ")
    field = input("Field to be added: ")
    value = input("Value in field: ")

    # Make sure that the city does exists in the database
    result = db.collection('places').document(name).get()
    if not result.exists:
      print("Item does not exist!")
      return

    # Add the field
    db.collection('places').document(name).set({
        field: value}, merge=True)

def delete_doc(db):
    '''This deletes a whole document'''
    name = input("Enter a city name: ")

    # Make sure that the city does exists in the database
    result = db.collection('places').document(name).get()
    if not result.exists:
      print("Item does not exist!")
      return

    # Delete the city
    db.collection('places').document(name).delete()

def delete_field(db):
    '''You can also delete a single field'''
    name = input("Enter a city name: ")
    field = input("Field to be deleted (lat, long, or where_to_go): ")

    # Make sure that the city does exists in the database
    result = db.collection('places').document(name).get()
    if not result.exists:
      print("Item does not exist!")
      return

    # Delete the field
    db.collection('places').document(name).update({
        field: firestore.DELETE_FIELD})

def main():
    choice = None
    while choice != "0":
        print()
        print("0) Exit")
        print("1) Insert a New City")
        print("2) Display a City")
        print("3) Modify a City")
        print("4) Add a field to a City")
        print("5) Delete a City")
        print("6) Delete a field in a City")
        choice = input(f"> ")
        print()
        if choice == "1":
            insert_doc(db)
        elif choice == "2":
            display_doc(db)
        elif choice == "3":
            modify_doc(db)
        elif choice == "4":
            add_field(db)
        elif choice == "5":
            delete_doc(db)
        elif choice == "6":
            delete_field(db)


if __name__ == "__main__":
    main()