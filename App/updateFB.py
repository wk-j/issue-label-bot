from firebase_admin import db
from datetime import datetime 
import pytz
# Fetch the service account key JSON file contents
cred = credentials.Certificate('bot.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bot-label-615f6.firebaseio.com'
})
def up(pro,num):
    ref = db.reference('DATA')
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