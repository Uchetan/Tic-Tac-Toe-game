mydb=con.connect(host='localhost',user='root',passwd='password',use_pure=True)

query='create database api'
cur=mydb.cursor()
cur.execute(query)
mydb.commit()

mydb=con.connect(host='localhost',database='api',user='root',passwd='password',use_pure=True)

query='create tabel'
cur=mydb.cursor()
cur.execute(query)
mydb.commit()