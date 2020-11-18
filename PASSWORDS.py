import sqlite3

#connect to database
#conn = sqlite3.connect("Passcodes.db")

#assign cursor
#c = conn.cursor()

#c.execute("""CREATE TABLE PASSWORDS (
		#ACCOUNT text,
		#PASSWORD text
		#)""")

#conn.commit()
#conn.close()

#function for adding password
def add_pass(account,password):
	conn = sqlite3.connect("Passcodes.db")

	c = conn.cursor()

	c.execute("INSERT INTO PASSWORDS VALUES(?,?)",(account,password))

	conn.commit()
	conn.close()

#add_pass("Youtube","ABCF1234")

#function to select the password for an account
def select(account):
	conn = sqlite3.connect("Passcodes.db")

	c = conn.cursor()

	c.execute("SELECT PASSWORD FROM PASSWORDS WHERE ACCOUNT = (?)",(account,))

	i = c.fetchone()
	for a in i:
		print(a)

	conn.commit()
	conn.close()
#select('Youtube')


#function to delete an account from database
def delete(account):
	conn = sqlite3.connect("Passcodes.db")

	c = conn.cursor()

	c.execute("DELETE FROM PASSWORDS WHERE ACCOUNT = (?)",(account,))

	conn.commit()
	conn.close()

#delete('Youtube')

#function to view all accounts and passwords
def view():
	conn = sqlite3.connect("Passcodes.db")

	c = conn.cursor()

	c.execute("SELECT * FROM PASSWORDS")
	items = c.fetchall()
	for i in items:
		print(i[0] + ":",i[1])

	conn.commit()
	conn.close()


#execution
print("WELCOME TO THE PASSWORDS INTERFACE!")
print("\n\n*********************************************************\nEnter q - to quit.\nEnter add - to add an account and password.")
print("Enter select - to select a password for the account.\nEnter del - to delete an account from database.\nEnter view - to view all accounts and passwords.")
print("*********************************************************")

running = True

commands = ['q','add','select','del','view']

while running:
	command = input("Enter your command: ")

	if command not in commands:
		print("Sorry wrong command!Re-enter.")
	elif command == 'q':
		print("Bye!")
		running = False
	elif command == 'add':
		a = input("Enter accunt name: ")
		p = input("Enter password: ")
		add_pass(a,p)
		print("Added successfully!")

	elif command == 'select':
		x = input("Enter account(name) you want to select: ")
		
		try:
			select(x)
		except TypeError:
			print("No such account exists!")

	elif command == 'del':
		x = input("Enter the account you want to delete: ")
		delete(x)
		print("Deleted succcesfully.")
	elif command == 'view':
		try:
			view()
		except TypeError:
			print("No data to show!")