import firebase_admin
from firebase_admin import credentials, db
import json
import os

# Load Firebase credentials from environment variable
firebase_cred_json = os.getenv('serviceAccountKey.json')

# Convert the JSON string into a dictionary
cred_dict = json.loads(firebase_cred_json)

# Create credentials object
cred = credentials.Certificate(cred_dict)

# Initialize Firebase Admin SDK
firebase_admin.initialize_app(cred, {
    'databaseURL': os.getenv('https://blog-f8552-default-rtdb.firebaseio.com/')  # Get DB URL from environment variables
})
