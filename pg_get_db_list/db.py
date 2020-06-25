import psycopg2
import pyodbc


def pg_connect(host, port, user, password, database="postgres"):
    try:
        conn = psycopg2.connect(host=host,
                                port=port,
                                user=user,
                                password=password,
                                database=database)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return -1

    if (conn):
        return conn
    else:
        return -1


def disconnect(connection):
    if connection:
        connection.close();


def mssql_connect(host, user, password, database="master"):
    try:
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+host+';DATABASE='+database+';UID='+user+';PWD='+password)
    except () as error:
        print(error)
        return -1

    if (conn):
        return conn
    else:
        return -1

