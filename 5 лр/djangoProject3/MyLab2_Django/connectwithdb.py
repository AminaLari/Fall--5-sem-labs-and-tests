''''
import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="123",
    db="first_db"
)

c=db.cursor()
c.execute("INSERT INTO artists (name,country) VALUES (%s, %s);", ('Artists', 'Country'))
db.commit()
c.close()
db.close()
'''