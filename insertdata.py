def checkstandardlabel(label):
    result = "No"
    item = label.split("-")
    for i in item:
        if i == "bug" or i == "documentation" or i == "duplicate" or i == "enhancement" or i == "good first issue" or i == "help wanted" or i == "invalid":
            result = i
            break
    return result
    
def tosingleline(lines):
    mystr = ''.join([line.strip() for line in lines])
    return mystr

def getlabels(labels):
    data1 = str(labels).split('name="')
    st = '")'
    data2 = data1[1].split(st)
    return data2[0]

def pluslabel(datalabel):
    label = ""
    labelall = []
    for j in datalabel:
        labelall.append(tosingleline(getlabels(j)))
    for la in labelall:
        label = label+"-"+la
    return label
def accepdata(pretitle,preDes,listlabel):
    linelabel = pluslabel(listlabel)
    label = checkstandardlabel(linelabel)
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