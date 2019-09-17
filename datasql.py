def cutDes(preDescription):
    i = 0
    for dt in preDescription:
        if len(dt)>100:
            preDescription[i] = dt[:-(len(dt)-100)]
        i = i+1
    return preDescription
def loaddata():
    import psycopg2
    connection = psycopg2.connect(user = "bqcgmqbqxnmkvf",
                                  password = "d10f07f570f94dcc79d5efa406c0bee1bbaee7356175222a7961424aee5ee091",
                                  host = "ec2-107-20-198-176.compute-1.amazonaws.com",
                                  port = "5432",
                                  database = "da5rk6c5e5n5aj")

    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from datatrain"
    cursor.execute(postgreSQL_select_Query)
    data_records = cursor.fetchall() 
    title = []
    des = []
    lable = []
    for row in data_records:
        title.append(row[1])
        des.append(row[2])
        lable.append(row[3])
       #print("Title = ", row[1], )
       #print("Description = ", row[2])
       #print("Label  = ", row[3], "\n")
    des = cutDes(des)
    cursor.close()
    connection.close()
    from splitClass import splitclass as sp
    sp(title,des,lable)