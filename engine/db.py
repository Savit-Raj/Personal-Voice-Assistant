import sqlite3

con = sqlite3.connect("voyage.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null, 'figma', 'Figma')"
# cursor.execute(query)
# con.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null, 'edc', 'https://www.edcbitmesra.in/')"
# cursor.execute(query)
# con.commit()

# primary_key_value = 3
# cursor.execute('DELETE FROM web_command WHERE id = ?', (primary_key_value,))
# con.commit()
# con.close()

# open = "spotify"
# cursor.execute('SELECT path FROM sys_command WHERE name IN (?)',(open,))
# result = cursor.fetchall()
# print(result[0][0])

query = "CREATE TABLE IF NOT EXISTS contacts(id integer primary key, name VARCHAR(255), mobile_no VARCHAR(255))"
cursor.execute(query)

query = "INSERT INTO contacts VALUES (null, 'pranav', '9693169743')"
cursor.execute(query)
con.commit()

# query = 'papa'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])