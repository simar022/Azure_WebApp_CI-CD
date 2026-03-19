import os
from pymongo import MongoClient
from datetime import datetime

# Connection string will be pulled from Azure Environment Variables
MONGO_URI = os.environ.get("MONGO_URI")

def get_db():
    client = MongoClient(MONGO_URI)
    return client['cloud_deploy_db']

def add_visit_log():
    db = get_db()
    db.logs.insert_one({
        "timestamp": datetime.now(),
        "event": "Page Visit"
    })

def get_logs():
    db = get_db()
    # Fetch last 5 logs
    return list(db.logs.find().sort("timestamp", -1).limit(5))
