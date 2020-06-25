import db
import hashlib

pg_server = "DC2MGMT06"

db_conn = db.pg_connect(pg_server+".aobi.local", 5432, "svc_dev", "C8EAX2LQMj")
mdb_conn = db.mssql_connect("dc2tsd01.aobi.local", "sa", "Password.1", "bi_infra_dbinfo_01")
m = hashlib.md5()

cursor = db_conn.cursor()
cursor.execute("""SELECT datname from pg_database WHERE datname NOT IN ('postgres', 'template0', 'template1')""")
rows = cursor.fetchall()
for row in rows:
    db_name = row[0]
    cursor.execute("SELECT pg_database_size('"+db_name+"')")
    db_size = round(cursor.fetchone()[0]/1024/1024, 0)
    string = db_name+pg_server
    m.update(string.encode('utf-8'))
    hash_string = m.hexdigest()

    mcursor = mdb_conn.cursor()

    mcursor.execute("""INSERT INTO [bi_infra_dbinfo_01].[dbo].[db_info] (db_name, server_name, size_mb, hash, dbms_type) 
    VALUES (?,?,?,?,?)""",
    db_name, pg_server, db_size, hash_string, "PostgreSQL")

    mdb_conn.commit()

    mcursor.close()
    print(db_size)
    print(db_name, db_size)

cursor.close()
db.disconnect(db_conn)
db.disconnect(mdb_conn)
