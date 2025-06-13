import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyCMke0Fhrum9hhCE_z4rYgrlguhu34G3HQ",
  "authDomain": "heart-attack-prediction-d4873.firebaseapp.com",
  "databaseURL": "https://heart-attack-prediction-d4873-default-rtdb.firebaseio.com",
  "projectId": "heart-attack-prediction-d4873",
  "storageBucket": "heart-attack-prediction-d4873.firebasestorage.app",
  "messagingSenderId": "719482908255",
  "appId": "1:719482908255:web:3f903933c5f94a85e775ea",
  "measurementId": "G-FNDLB9EWYT"
};

# Initialize Firebase app only once
cred = credentials.Certificate(r"C:\Users\Vaishnavi\OneDrive\Desktop\heartattack\serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Export Firestore DB client
db = firestore.client()

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()