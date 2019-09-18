
def readfile():
    import logging
    logging.getLogger().setLevel(logging.INFO)
    import csv
    title = []
    des = []
    label = []
    with open('data.csv', mode='r') as csv_file:      
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            title.append(row['Title'])
            des.append(row['Description'])
            label.append(row['Label'])
            line_count += 1
        logging.info(f'Processed {line_count} lines.')
    return title,des,label

def insertdata():
    import logging
    logging.getLogger().setLevel(logging.INFO)
    import psycopg2
    connection = psycopg2.connect(user = "your user",
                                    password = "your password",
                                    host = "you host",
                                    port = "your port",
                                    database = "your database")
    cursor = connection.cursor()
    title,des,label = readfile()
    i = 0
    n = len(title)
    while(i<n):
        postgres_insert_query = """ INSERT INTO datatrain (title, description, label) VALUES (%s,%s,%s)"""
        record_to_insert = (title[i], des[i], label[i])
        cursor.execute(postgres_insert_query, record_to_insert)
        i = i+1
        logging.info(i)
    connection.commit()
    cursor.close()
    connection.close()

insertdata()