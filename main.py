import mysql.connector
from passlib.hash import pbkdf2_sha256
import os

db = mysql.connector.connect(
	host='127.0.0.1',  # leave localhost else remote ip
	user='',  # db username
	passwd='',  # db password
	database=''  # name of the database
)
print("Welcome to my app ")
print("""Choose the below options 

1. See all Users
2. Register your account
3. Login into your account
4. Change your account password 
5. Delete your account
6. Exit
""")


def see_all():
	c = db.cursor(buffered=True)
	sql = "SELECT user_ FROM login"  # login (Name of the table in db)
	c.execute(sql)
	for tb in c:
		print(str(tb)[2:-3])
	sql = " SELECT COUNT(user_) FROM login "
	c.execute(sql)
	print("No of users : " + str(c.fetchone())[1:-2])


# see_all() "*****************************************"

def login_in_your_acc():
	c = db.cursor(buffered=True)
	user_name = input("Enter id : ")
	sql = "SELECT pass FROM login WHERE user_=%s"
	password = input("Enter passw : ")
	
	c.execute(sql, (user_name,))
	try:
		
		hash_ = str(c.fetchone())[2:-3]
		
		# print(hash)
		if pbkdf2_sha256.verify(password, hash_):
			print("Login success")
		else:
			print("Wrong Username/Password")
	except:
		print("Invalid id or pass !!")


#############################################################################
def add_user():
	c = db.cursor(buffered=True)
	username = input("Enter a username : ")
	password = input("Enter a password : ")
	hash_ = pbkdf2_sha256.hash(password)
	try:
		sql = "INSERT INTO login VALUES(%s,%s)"
		c.execute(sql, (username, hash_,))
		db.commit()
		print("Successfully added")
	except:
		print("Username already exists ")
		add_user()


def change_pass_word():
	c = db.cursor(buffered=True)
	user_name = input("Enter id : ")
	password = input("Enter password : ")
	
	try:
		
		sql = "SELECT pass FROM login WHERE user_=%s"
		c.execute(sql, (user_name,))
		hash_ = str((c.fetchone()))[2:-3]
		# print(hash_)
		if pbkdf2_sha256.verify(password, hash_):
			password = input("Enter your new password : ")
			hash_ = pbkdf2_sha256.hash(password)
			sql = "UPDATE login set pass=%s WHERE user_=%s"
			c.execute(sql, (hash_, user_name,))
			db.commit()
			print("Changed Successfully !")
		else:
			print("Wrong Username/Password")
	except:
		print("Wrong Username/Password")


def del_acc():
	c = db.cursor(buffered=True)
	user_name = input("Enter id : ")
	password = input("Enter passw : ")
	sql = "SELECT pass FROM login WHERE user_=%s"
	c.execute(sql, (user_name,))
	hash_ = str(c.fetchone())[2:-3]
	if pbkdf2_sha256.verify(password, hash_):
		sql = "SELECT * FROM login WHERE user_=%s"
		c.execute(sql, (user_name,))
		if c.fetchone() is None:
			print("Wrong username or password !!")
		
		# break
		else:
			sql = "DELETE FROM login WHERE user_=%s;"
			c.execute(sql, (user_name,))
			db.commit()
			print("Deleted Successfully !")
	else:
		print("Wrong username or password !!")


def selection():
	option = int(input("Enter your choice : "))
	os.system('cls')
	if option == 1:
		see_all()
		selection()
	elif option == 2:
		add_user()
		selection()
	elif option == 3:
		login_in_your_acc()
		selection()
	elif option == 4:
		change_pass_word()
		selection()
	elif option == 5:
		del_acc()
		selection()
	elif option == 6:
		exit(0)
	else:
		print("Invalid choice")


selection()
