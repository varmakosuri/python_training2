import sqlite3
def get_connection(database=None):
	database = database if database else "db1.db"
	con = sqlite3.connect(database)
	cur  =con.cursor()
	return con,cur

def browse_students(id=None):
	try:
		data  =[]
		if id:
			query = "select * from students where id={0}".format(id)
		else:
			query = "select * from students"
		con,cur  =get_connection()
		cur.execute(query)
		data = cur.fetchall()
	except Exception as err:
		print err
	finally:
		cur.close()
		con.close()
	return data

def browse(table):
	try:
		data=[]
		query = "select * form {0}".format(table)
		con,cur  =get_connection()
		cur.execute(query)
		data = cur.fetchall()
	except Exception as err:
		print err
	finally:
		cur.close()
		con.close()
	return data
def create_table():
	try:
		query= "create table students(id int, name varchar(250))"
		con,cur=get_connection()
		cur.execute(query)
	except Exception as err:
		print err
	finally:
		cur.close()
		con.close()
def insert_dummy_data():
	try:
		con,cur = get_connection()
		for i in range(1000):
			q="insert into students values({0},'name{0}')".format(i)
			cur.execute(q)
	except Exception as err:
		print err
	else:
		con.commit()
	finally:
		cur.close()
		con.close()

			




if __name__=="__main__":
	#create_table()
	insert_dummy_data()