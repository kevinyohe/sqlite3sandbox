import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute("CREATE TABLE commands (id varchar(3), device string, command string, data json)")
conn.commit()
conn.close()
