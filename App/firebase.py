
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime 
import pytz
# Fetch the service account key JSON file contents
cred = credentials.Certificate('bot.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bot-label-36a1f.firebaseio.com'
})
ref = db.reference('DATA')

def insert(label,title,project,number):
    tz_Bankok = pytz.timezone('Asia/Bangkok')
    datetime_Bankok = datetime.now(tz_Bankok)
    ref.push({
        "Date": str(datetime_Bankok),
        "Label":label,
        "Title":title,
        "Project":project,
        "Number":number,
        "Status":"Open"
    })
def up(pro,num):
    dt = ref.get()
    idkey = ''
    for data in ref.get():
        if pro == dt[data]['Project'] and num == dt[data]['Number']:
            idkey = data
            print(idkey)
    data_ref = ref.child(idkey)
    data_ref.update({
        'Status': 'Close'
    })