def insert(label,title,des):
    import pyrebase
    import datetime
    config = {
        "apiKey": "AIzaSyAt0kO8MDeqCWOLAMaaPxDS0yF8UkVPEdo",
        "authDomain": "bot-label-615f6.firebaseapp.com",
        "databaseURL": "https://bot-label-615f6.firebaseio.com",
        "projectId": "bot-label-615f6",
        "storageBucket": "bot-label-615f6.appspot.com",
        "messagingSenderId": "188295128754",
        "appId": "1:188295128754:web:9666ba1caef90ab87c0bab"
    }
    firebase = pyrebase.initialize_app(config)

    # Get a reference to the auth service
    auth = firebase.auth()

    # Log the user in
    #auth.create_user_with_email_and_password('test@gmail.com', 'sunner00x')
    user = auth.sign_in_with_email_and_password('test@gmail.com', 'test00x')

    # Get a reference to the database service
    db = firebase.database()

    # data to save
    data = {
        "Date": str(datetime.datetime.now()),
        "Label":label,
        "Title": title,
        "Description":des
    }
    # Pass the user's idToken to the push method
    results = db.child("DATA").push(data, user['idToken'])