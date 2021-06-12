from __future__ import annotations
from firebase_admin import credentials
from firebase_admin import db
import firebase_admin
from typing import List

class DatabaseConnection:
    def save(self, time_stamp):
        if not firebase_admin._apps:
            cred = credentials.Certificate("firebaseKey.json")
            firebase_admin.initialize_app(cred, {'databaseURL': "https://alarmonthedoorsystem-default-rtdb.firebaseio.com/"})
        ref = db.reference(f'/intrusions')
        json_timestamp = {"Timestamp":f"{time_stamp}"}
        ref.push(json_timestamp)

   

