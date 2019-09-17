import psycopg2

try:
    connection = psycopg2.connect(user = "your user",
                                    password = "your password",
                                    host = "you host",
                                    port = "your port",
                                    database = "your database")

    cursor = connection.cursor()
    create_table_query = '''CREATE TABLE datatrain
          (ID SERIAL PRIMARY KEY,
          Title           TEXT    NOT NULL,
          Description         TEXT    NOT NULL,
          Label           TEXT    NOT NULL); '''
    
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")