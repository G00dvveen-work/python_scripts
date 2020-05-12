import event_parser as ep
from config import config
import pandas as pd
import psycopg2


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


call_log_dir = './files/logs/call'
excp_log_dir = './files/logs/excp'
output_dir = './files/output'

connect()

#calls = pd.read_csv(ep.parse_call(call_log_dir, output_dir))

#exceptions = pd.read_csv(ep.parse_excp(excp_log_dir, output_dir))


#print(calls.head())
#print(exceptions['context'].value_counts())