def checkstandardlabel(label):
    result = "No"
    for i in label:
        if i["name"] == "bug" or i["name"] == "documentation" or i["name"] == "duplicate" or i["name"] == "enhancement" or i["name"] == "good first issue" or i["name"] == "help wanted" or i["name"] == "invalid":
            result = i["name"]
            break
    return result

def accepdata(pretitle,preDes,listlabel):
    label = checkstandardlabel(listlabel)
    if label != "No":
        insertdata(pretitle,preDes,label)

def insertdata(title,des,label):
    import psycopg2
    connection = psycopg2.connect(user = "bqcgmqbqxnmkvf",
                                  password = "d10f07f570f94dcc79d5efa406c0bee1bbaee7356175222a7961424aee5ee091",
                                  host = "ec2-107-20-198-176.compute-1.amazonaws.com",
                                  port = "5432",
                                  database = "da5rk6c5e5n5aj")

    cursor = connection.cursor()
    postgres_insert_query = """ INSERT INTO datatrain (title, description, label) VALUES (%s,%s,%s)"""
    record_to_insert = (title, des, label)
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    cursor.close()
    connection.close()