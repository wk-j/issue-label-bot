
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime 
import pytz
# Fetch the service account key JSON file contents
cred = credentials.Certificate('bot.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bot-label-615f6.firebaseio.com'
})
def insert(label,title,project,number):
    tz_Bankok = pytz.timezone('Asia/Bangkok')
    datetime_Bankok = datetime.now(tz_Bankok)
    ref = db.reference('DATA')
    ref.push({
        "Date": str(datetime_Bankok),
        "Label":label,
        "Title":title,
        "Project":project,
        "Number":number
    })