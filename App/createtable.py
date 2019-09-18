import psycopg2
import logging
logging.getLogger().setLevel(logging.INFO)
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
    logging.info("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.Error) as error :
    logging.info ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            logging.info("PostgreSQL connection is closed")