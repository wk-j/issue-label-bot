def insert(label,title,des):
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db
    import datetime

    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('bot.json')
    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://bot-label-615f6.firebaseio.com'
    })
    ref = db.reference('DATA')
    ref.push({
        "Date": str(datetime.datetime.now()),
        "Label":label,
        "Title":title,
        "Description":des
    })