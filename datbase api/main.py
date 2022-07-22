import mysql.connector as con

mydb=con.connect(host='localhost',database='api',user='root',passwd='password',use_pure=True)

query='create table info (name varchar(20),number varchar(10),email varchar(20))'
cur=mydb.cursor()
cur.execute(query)
mydb.commit()