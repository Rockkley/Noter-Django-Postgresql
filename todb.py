import psycopg2
from psycopg2 import Error
try:
    # Connect to an existing database
    connection = psycopg2.connect(user="user",
                                  password="password",
                                  host="host",
                                  port="port",
                                  database="database")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    try:
        insert_q = """INSERT INTO public.noter_app_category (id,title) VALUES ('CATEGORY_ID','CATEGORY_NAME');"""
        cursor.execute(insert_q)
        connection.commit()
        

    except Exception as E:
        print(E)
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")




except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
