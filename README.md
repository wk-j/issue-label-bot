## Install issueprocess
```
pip3 install -i https://test.pypi.org/simple/ issueprocess
```
## Using on Terminal

help
```
loadissue --help
trainmodel --help
```

load only repository =====file.csv will save in your Document=====
```
loadissue --token=... --name=...
```

train model =====model.data and vocabulary.data will save in your Document=====
```
trainmodel --user=... --password=... --host=... --port=... --database=... --table=...
```

## Create Database

install postgresql in your HEROKU, Can see detail of database in Heroku Postgres > Setting > View Credentials...

Create Table
edit connection in createtabel.py and run
```
python3 createtabel.py
```

Insert Table
edit connection in inserttable.py and run
```
python3 inserttable.py
```

## Deploy on Heroku

Add ENV 1. USER = your user
        2. PASS = your password
        3. HOST = your host
and edit DBconfig to your detail database and deploy

## Using

Bot Label
URL ::  https://github.com/apps/bot-label

Show Bot Working
URL :: https://bot-label-615f6.web.app
