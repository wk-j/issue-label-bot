def checkstandardlabel(label):
    result = "No"
    for i in label:
        if i["name"] == "bug" or i["name"] == "documentation" or i["name"] == "duplicate" or i["name"] == "enhancement" or i["name"] == "good first issue" or i["name"] == "help wanted" or i["name"] == "invalid":
            result = i["name"]
            break
    return result

def accepdata(pretitle,preDes,listlabel,dtlist):
    label = checkstandardlabel(listlabel)
    if label != "No":
        insertdata(pretitle,preDes,label,dtlist)

def insertdata(title,des,label,dtlist):
    import psycopg2
    connection = psycopg2.connect(user = dtlist[0],
                                  password = dtlist[1],
                                  host = dtlist[2],
                                  port = dtlist[3],
                                  database = dtlist[4])

    cursor = connection.cursor()
    postgres_insert_query = """ INSERT INTO %s (title, description, label) VALUES (%s,%s,%s)"""
    record_to_insert = (dtlist[5],title, des, label)
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    cursor.close()
    connection.close()