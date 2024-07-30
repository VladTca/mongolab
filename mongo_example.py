from pymongo import MongoClient

user = 'root'
password = 'MTIzMzAtdm90c2F0'  # CHANGE THIS TO THE PASSWORD YOU NOTED IN THE EARLIER EXERCISE - 2
host = 'localhost'

# Create the connection URL
connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user, password, host)

# Connect to MongoDB server
print("Connecting to MongoDB server")
connection = MongoClient(connecturl)

# Select the 'training' database
db = connection.training

# Select the 'mongodb_glossary' collection
collection = db.mongodb_glossary

# Create sample documents
documents = [
    {"database": "a database contains collections"},
    {"collection": "a collection stores the documents"},
    {"document": "a document contains the data in the form of key value pairs."}
]

# Insert sample documents
print("Inserting documents into collection.")
collection.insert_many(documents)

# Query for all documents in 'training' database and 'mongodb_glossary' collection
docs = collection.find()

print("Printing the documents in the collection.")
for document in docs:
    print(document)

# Close the server connection
print("Closing the connection.")
connection.close()
