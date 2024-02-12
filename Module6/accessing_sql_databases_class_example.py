import sqlite3
"""
This program is showing an example of how connect to a SQL database

@author: Tiago Saraiva
@date: 2024-01-26
"""
# Create the database
conn = sqlite3.connect("weather.sqlite")
print("Opened the database successfully")

cur = conn.cursor()
cur.execute("drop table samples;")
cur.execute("""create table samples
           (id integer primary key autoincrement not null,
            date text not null,
            location text not null,
            min_temp
            real not null,
            max_temp
            real not null,
            avg_temp
            real not null);""")
print("Table created successfully.")

sql = """insert into samples
      (date, location, min_temp , max_temp , avg_temp)
      values (?, ?, ?, ?, ?)"""
data = ('2018 05 24', 'Winnipeg, MB', -10.6, 12.2, 6.4)
cur.execute(sql, data)
conn.commit()
print("Added sample successfully.")

for row in cur.execute("select * from samples"):
    print(row)
    
cur.close
conn.close()
