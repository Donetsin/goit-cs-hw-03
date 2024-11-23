from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://donetsin:WG61Rs9gHP7mOcXg@cluster0.orlly.mongodb.net",
    server_api=ServerApi('1')
)

def get_db():
    db = client.task_02
    return db
