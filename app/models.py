import os
from pymongo import MongoClient, errors
from datetime import datetime


# Connection string will be pulled from Azure Environment Variables
MONGO_URI = os.environ.get("MONGO_URI")

def get_db():
    client = MongoClient(MONGO_URI)
    return client['cloud_deploy_db']

def add_visit_log():
    try:
        # Set a short timeout (e.g., 3 seconds) so the user doesn't wait 30s for a 500 error
        client = MongoClient(os.environ.get("MONGO_URI"), serverSelectionTimeoutMS=3000)
        db = client['mongodb022']
        db.logs.insert_one({"timestamp": datetime.now(), "event": "Page Visit"})
    except errors.ServerSelectionTimeoutError as e:
        print(f"Database connection timed out: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_logs():
    db = get_db()
    # Fetch last 5 logs
    return list(db.logs.find().sort("timestamp", -1).limit(5))
