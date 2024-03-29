def cutDes(preDescription):
    i = 0
    for dt in preDescription:
        if len(dt)>100:
            preDescription[i] = dt[:-(len(dt)-100)]
        i = i+1
    return preDescription
def loaddata(user,password,host,port,database,table):
    import psycopg2
    import logging
    logging.getLogger().setLevel(logging.INFO)
    connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)

    cursor = connection.cursor()
    postgreSQL_select_Query = F"select * from {table}"
    logging.info(postgreSQL_select_Query)
    cursor.execute(postgreSQL_select_Query)
    data_records = cursor.fetchall() 
    title = []
    des = []
    lable = []
    for row in data_records:
        title.append(row[1])
        des.append(row[2])
        lable.append(row[3])
    des = cutDes(des)
    cursor.close()
    connection.close()
    return title,des,lable