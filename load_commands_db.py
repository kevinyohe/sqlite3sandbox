import sqlite3
import json
import requests
#sqlite3 test.db "select data from commands order by random() limit 1"
#
# countries_api_res = requests.get('http://api.worldbank.org/countries?format=json&per_page=100')
# commands = countries_api_res.json()[1]
#
# print(commands)
# conn = sqlite3.connect('test.db')
# c = conn.cursor()

"switch1", "show ip int br",




def add_one(hostname, command, jsondata):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("INSERT INTO commands VALUES (?,?,?)", (hostname, command, jsondata))
    conn.commit()
    conn.close()

def get_one(hostname, command):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("SELECT jsondata FROM commands WHERE hostname = (?) AND command = (?)", (hostname,command))
    return c.fetchone() or None

add_one('test123', 'show ip mouth', '{some:stuff}')
print(get_one('test123', 'show ip mouth'))