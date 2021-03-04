import sqlite3

#Connect to the database
conn = sqlite3.connect('test.db')

c = conn.cursor()
many_customers = [('wes', 'brown', 'wes@brown.com'),
                  ('steph', 'Keul', 'shize@lala.com'),
                  ('Dan', 'Pas', 'dan@pas.com')
]
# c.execute("""CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email text
# )   """)

c.execute("INSERT INTO customers VALUES ('kevin', 'yohe', 'kevin@KEVINYOHE.DEV')")
c.executemany("INSERT INTO customers VALUES(?,?,?)", many_customers)
conn.commit()



c.execute("SELECT rowid, * FROM customers")
print("FETCH ONE", c.fetchone())
c.fetchmany(3)
print(c.fetchall())




c.execute("""UPDATE customers SET first_name = 'Kevvo' 
WHERE last_name = 'yohe'
    

""")
conn.commit()
conn.close()