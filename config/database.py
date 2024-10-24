from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the MongoDB credentials from the environment variables
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")

# Create the MongoDB connection URI using the loaded credentials
uri = f"mongodb+srv://{username}:{
    password}@cluster0.jbxak.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Initialize MongoDB client and access the database and collection
client = MongoClient(uri)
db = client.todo_db
collection_name = db["todo_collection"]
