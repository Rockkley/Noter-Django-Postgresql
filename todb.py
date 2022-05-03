import psycopg2
from psycopg2 import Error
try:
    # Connect to an existing database
    connection = psycopg2.connect(user="cajwldeplhefhv",
                                  password="0f73d446b9a2a698ff1092fedf1803410d0e51cdeccf98244d7af2f43d318348",
                                  host="ec2-3-229-252-6.compute-1.amazonaws.com",
                                  port="5432",
                                  database="d7fuflcfvb40n2")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    insert_q = """INSERT INTO noter_app_category (title, id) VALUES ('Genius Ideas','1');"""
    cursor.execute(insert_q)

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")