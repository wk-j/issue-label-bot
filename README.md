## Install issueprocess
```
- issueprocess
pip3 install -i https://test.pypi.org/simple/ issueprocess
```
## Using on Terminal
```
loadissue --help
- load only repository
loadissue --token=... --name=...
=====file.csv will save in your Document=====
trainmodel --help
- train model
trainmodel --user=... --password=... --host=... --port=... --database=... --table=...
=====model.data and vocabulary.data will save in your Document=====
```
## Create Database
```
install postgresql in your HEROKU, Can see detail of database in Heroku Postgres > Setting > View Credentials...
=============================
Create Table
edit connection in createtabel.py and run
python3 createtabel.py

Insert Table
edit connection in inserttable.py and run
python3 inserttable.py
```
## Deploy on Heroku
```
Add ENV 1. USER = your user
        2. PASS = your password
        3. HOST = your host
and edit DBconfig to your detail database and deploy
```
## Using
Bot Label
```
URL ::  https://github.com/apps/bot-label
```
